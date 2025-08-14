from node import Node

class FileSystem:
    def __init__(self):
        self.root = Node("root")
        self.current_directory = self.root

    def ls(self, path=None):
        target_dir = self.current_directory if path is None else self._resolve_path(path)
        if target_dir is None:
            return "Path not found"
        if not target_dir.is_directory():
            return f"'{path}' is not a directory"
        if not target_dir.children:
            return "Directory is empty"
        items = []
        for name, child in sorted(target_dir.children.items()):
            if child.is_directory():
                items.append(f"{name}/")
            else:
                items.append(name)
        return "\n".join(items)

    def pwd(self):
        return self.current_directory.get_path()

    def mkdir(self, dirname):
        try:
            if not dirname or '/' in dirname:
                return "Invalid directory name"
            new_dir = Node(dirname, "directory")
            self.current_directory.add_child(new_dir)
            return f"Directory '{dirname}' created"
        except ValueError as e:
            return str(e)

    def touch(self, filename):
        try:
            if not filename or '/' in filename:
                return "Invalid file name"
            new_file = Node(filename, "file")
            self.current_directory.add_child(new_file)
            return f"File '{filename}' created"
        except ValueError as e:
            return str(e)

    def cd(self, path):
        if path == "..":
            if self.current_directory.parent is not None:
                self.current_directory = self.current_directory.parent
                return f"Changed to: {self.pwd()}"
            else:
                return "Already at root directory"
        elif path == "/" or path == "~":
            self.current_directory = self.root
            return f"Changed to: {self.pwd()}"
        else:
            target = self._resolve_path(path)
            if target is None:
                return f"Directory '{path}' not found"
            if not target.is_directory():
                return f"'{path}' is not a directory"
            self.current_directory = target
            return f"Changed to: {self.pwd()}"

    def rm(self, name, recursive=False):
        if name not in self.current_directory.children:
            return f"'{name}' not found"
        target = self.current_directory.children[name]
        if target.is_file():
            self.current_directory.remove_child(name)
            return f"File '{name}' removed"
        elif target.is_directory():
            if not recursive and target.children:
                return f"Directory '{name}' is not empty. Use 'rm -r {name}' to remove recursively"
            if recursive:
                self._recursive_remove(target)
            self.current_directory.remove_child(name)
            return f"Directory '{name}' removed"

    def _recursive_remove(self, node):
        if node.is_directory():
            children_names = list(node.children.keys())
            for child_name in children_names:
                child = node.children[child_name]
                self._recursive_remove(child)
                node.remove_child(child_name)

    def mv(self, source_name, dest_path):
        if source_name not in self.current_directory.children:
            return f"'{source_name}' not found"
        source_node = self.current_directory.children[source_name]
        dest_dir = self._resolve_path(dest_path)
        if dest_dir is None:
            return f"Destination '{dest_path}' not found"
        if not dest_dir.is_directory():
            return f"Destination '{dest_path}' is not a directory"
        if source_node.name in dest_dir.children:
            return f"'{source_node.name}' already exists in destination"
        self.current_directory.remove_child(source_name)
        dest_dir.add_child(source_node)
        return f"Moved '{source_name}' to '{dest_path}'"

    def tree(self, max_depth=None):
        lines = []
        current_name = self.current_directory.name + ("/" if self.current_directory.is_directory() else "")
        lines.append(current_name)
        if self.current_directory.is_directory() and self.current_directory.children:
            items = sorted(self.current_directory.children.items())
            for i, (child_name, child) in enumerate(items):
                is_last = (i == len(items) - 1)
                self._tree_helper(child, "", is_last, lines, max_depth, 1)
        return "\n".join(lines)

    def _tree_helper(self, node, prefix, is_last, lines, max_depth, depth):
        if max_depth is not None and depth > max_depth:
            return
        connector = "└── " if is_last else "├── "
        name = node.name + ("/" if node.is_directory() else "")
        lines.append(prefix + connector + name)
        if node.is_directory() and node.children:
            items = sorted(node.children.items())
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, (child_name, child) in enumerate(items):
                is_child_last = (i == len(items) - 1)
                self._tree_helper(child, new_prefix, is_child_last, lines, max_depth, depth + 1)

    def _resolve_path(self, path):
        if path.startswith("/"):
            current = self.root
            if path == "/":
                return current
            parts = path.strip("/").split("/")
        else:
            current = self.current_directory
            parts = path.split("/")
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if current.parent is not None:
                    current = current.parent
            else:
                if current.is_file() or part not in current.children:
                    return None
                current = current.children[part]
        return current
