from cli import CommandLineInterface
import sys

def main():

    try:
        print("Starting File System Simulator...")
        print("Loading tree data structure implementation...")
        cli = CommandLineInterface()
        cli.run()

    except ImportError as e:
        print(f"Import Error: {e}")
        print("Make sure all required files are in the same directory:")
        print("- node.py")
        print("- file_system.py")
        print("- cli.py")
        print("- main.py")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()
