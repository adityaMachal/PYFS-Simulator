from file_system import FileSystem

class CommandLineInterface:
    def __init__(self):
        self.fs = FileSystem()
        self.running = True
        self.commands = {
            'ls': self.cmd_ls,
            'pwd': self.cmd_pwd,
            'mkdir': self.cmd_mkdir,
            'touch': self.cmd_touch,
            'cd': self.cmd_cd,
            'rm': self.cmd_rm,
            'mv': self.cmd_mv,
            'tree': self.cmd_tree,
            'help': self.cmd_help,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'clear': self.cmd_clear
        }

    def cmd_ls(self, args):
        if args:
            return self.fs.ls(args[0])
        return self.fs.ls()

    def cmd_pwd(self, args):
        return self.fs.pwd()

    def cmd_mkdir(self, args):
        if not args:
            return "Usage: mkdir <directory_name>"
        return self.fs.mkdir(args[0])

    def cmd_touch(self, args):
        if not args:
            return "Usage: touch <filename>"
        return self.fs.touch(args[0])

    def cmd_cd(self, args):
        if not args:
            return self.fs.cd("/")
        return self.fs.cd(args[0])

    def cmd_rm(self, args):
        if not args:
            return "Usage: rm [-r] <name>"
        recursive = False
        name = args[0]
        if args[0] == "-r":
            if len(args) < 2:
                return "Usage: rm -r <name>"
            recursive = True
            name = args[1]
        return self.fs.rm(name, recursive)

    def cmd_mv(self, args):
        if len(args) < 2:
            return "Usage: mv <source> <destination>"
        return self.fs.mv(args[0], args[1])

    def cmd_tree(self, args):
        max_depth = None
        if args and args[0].isdigit():
            max_depth = int(args[0])
        return self.fs.tree(max_depth)

    def cmd_help(self, args):
        help_text = """
File System Simulator Commands:

Navigation:
  ls [path]         - List directory contents
  cd <path>         - Change directory (use '..' for parent, '/' for root)
  pwd               - Print current directory path

File Operations:
  mkdir <name>      - Create a new directory
  touch <name>      - Create a new file
  rm <name>         - Remove file or empty directory
  rm -r <name>      - Remove directory recursively
  mv <src> <dest>   - Move file or directory

Display:
  tree [depth]      - Show directory tree structure
  help              - Show this help message
  clear             - Clear the screen

System:
  exit/quit         - Exit the simulator

Examples:
  mkdir documents
  cd documents
  touch readme.txt
  ls
  tree
  cd ..
  rm -r documents
"""
        return help_text

    def cmd_exit(self, args):
        self.running = False
        return "Goodbye!"

    def cmd_clear(self, args):
        return "\n" * 50

    def parse_command(self, input_line):
        parts = input_line.strip().split()
        if not parts:
            return None, []
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        return command, args

    def execute_command(self, command, args):
        if command in self.commands:
            try:
                return self.commands[command](args)
            except Exception as e:
                return f"Error executing command: {str(e)}"
        else:
            return f"Unknown command: {command}. Type 'help' for available commands."

    def run(self):
        print("=" * 60)
        print("🗂️  Welcome to the File System Simulator!")
        print("   Built with Tree Data Structures in Python")
        print("=" * 60)
        print("Type 'help' for available commands or 'exit' to quit.")
        print()
        while self.running:
            try:
                current_path = self.fs.pwd()
                prompt = f"fs:{current_path}$ "
                user_input = input(prompt)
                if not user_input.strip():
                    continue
                command, args = self.parse_command(user_input)
                if command:
                    result = self.execute_command(command, args)
                    if result:
                        print(result)
            except KeyboardInterrupt:
                print("\n\nUse 'exit' or 'quit' to leave the simulator.")
            except EOFError:
                print("\n\nGoodbye!")
                break

if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.run()
