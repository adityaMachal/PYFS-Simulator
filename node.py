class Node:
    def __init__(self, name, node_type="directory", parent=None):
        self.name = name
        self.type = node_type
        self.parent = parent
        self.children = {} if node_type == "directory" else None

    def is_directory(self):
        return self.type == "directory"

    def is_file(self):
        return self.type == "file"

    def add_child(self, child):
        if not self.is_directory():
            raise ValueError("Cannot add child to a file")
        if child.name in self.children:
            raise ValueError(f"'{child.name}' already exists")
        self.children[child.name] = child
        child.parent = self

    def remove_child(self, name):
        if not self.is_directory():
            raise ValueError("Cannot remove child from a file")
        if name not in self.children:
            raise ValueError(f"'{name}' not found")
        child = self.children[name]
        del self.children[name]
        child.parent = None
        return child

    def get_child(self, name):
        if not self.is_directory():
            return None
        return self.children.get(name)

    def get_path(self):
        if self.parent is None:
            return "/"
        path_parts = []
        current = self
        while current.parent is not None:
            path_parts.append(current.name)
            current = current.parent
        if not path_parts:
            return "/"
        path_parts.reverse()
        return "/" + "/".join(path_parts)
