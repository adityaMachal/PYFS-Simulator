# PYFS-Simulator
A Python-based file system simulator with a tree data structure, interactive CLI, and support for creating, navigating, and managing files and directories.    
# Features
- 📂 Directory Management – Create, remove, and navigate directories.
- 📄 File Management – Create and delete files.

- 🗂 Tree Structure – Hierarchical representation of files and directories using a custom Node class.

- 🖥 CLI Interface – User-friendly terminal commands to interact with the simulator.

- 🔗 Path Navigation – Retrieve full paths of files or folders.
# Project Structure
```perl
file-system-simulator/
│
├── main.py           # Entry point for running the simulator
├── cli.py            # Handles user command input
├── file_system.py    # Core file system logic
├── node.py           # Node class for directories and files
└── README.md         # Project documentation
```
# Installation & Usage
1️⃣ Clone the Repository    
```bash
git clone https://github.com/adityaMachal/PYFS-Simulator.git
cd PYFS-Simulator
```
2️⃣ Run the Simulator    
```bash
python main.py
```
# Example Commands
| Command        | Description                          |
|----------------|--------------------------------------|
| `mkdir <name>` | Create a new directory               |
| `touch <name>` | Create a new file                    |
| `ls`           | List contents of current directory   |
| `cd <name>`    | Change directory                     |
| `cd ..`        | Go back to parent directory          |
| `pwd`          | Show current directory path          |
| `rm <name>`    | Remove a file or directory           |
| `exit`         | Quit the simulator                   |

# How It Works
- Tree Data Structure – Each directory is a Node that can have children.
- Files vs Directories – Differentiated by type attribute (file or directory).
- CLI Interface – Parses user commands and maps them to file system operations.

# Future Enhancements
- Add support for file content storage and editing.
- Implement mv and cp commands.
- Add persistent storage to save the file system state.

# License
This project is licensed under the MIT License.
