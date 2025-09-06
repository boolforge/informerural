import argparse
import os
import sys

def create_file(path, content_file=None):
    """Creates a new file. If --content-file is provided, writes content from that file."""
    try:
        dir_path = os.path.dirname(path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        content = ''
        if content_file:
            with open(content_file, 'r', encoding='utf-8') as f:
                content = f.read()

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"File '{path}' created successfully.", file=sys.stderr)
    except Exception as e:
        print(f"Error creating file '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def read_file(path):
    """Reads the content of a file and prints it to stdout."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def overwrite_file(path, content_file):
    """Overwrites a file with content from a specified content file."""
    try:
        content = ''
        if not content_file:
             print(f"Error: --content-file is required for overwrite.", file=sys.stderr)
             sys.exit(1)
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"File '{path}' overwritten successfully.", file=sys.stderr)
    except Exception as e:
        print(f"Error overwriting file '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def delete_file(path):
    """Deletes a file."""
    try:
        os.remove(path)
        print(f"File '{path}' deleted successfully.", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error deleting file '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to parse arguments and call the appropriate file operation."""
    parser = argparse.ArgumentParser(description="A robust, portable script to manage file operations.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    # Create command
    parser_create = subparsers.add_parser('create', help='Create a new file.')
    parser_create.add_argument('path', type=str, help='The path for the new file.')
    parser_create.add_argument('--content-file', type=str, help='Path to a file containing the content for the new file.')

    # Read command
    parser_read = subparsers.add_parser('read', help='Read a file.')
    parser_read.add_argument('path', type=str, help='The path to the file to read.')

    # Overwrite command
    parser_overwrite = subparsers.add_parser('overwrite', help='Overwrite a file.')
    parser_overwrite.add_argument('path', type=str, help='The path to the file to overwrite.')
    parser_overwrite.add_argument('--content-file', required=True, type=str, help='Path to a file containing the new content.')

    # Delete command
    parser_delete = subparsers.add_parser('delete', help='Delete a file.')
    parser_delete.add_argument('path', type=str, help='The path of the file to delete.')

    args = parser.parse_args()

    if args.command == 'create':
        create_file(args.path, args.content_file)
    elif args.command == 'read':
        read_file(args.path)
    elif args.command == 'overwrite':
        overwrite_file(args.path, args.content_file)
    elif args.command == 'delete':
        delete_file(args.path)

if __name__ == '__main__':
    main()
