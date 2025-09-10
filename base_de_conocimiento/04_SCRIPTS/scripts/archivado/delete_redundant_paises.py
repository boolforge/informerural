import os
import sys
import shutil

def delete_directory_recursively(directory_path):
    """
    Deletes a directory and all its contents recursively.
    This function walks the directory tree from the bottom up,
    deleting files first, then the now-empty directories.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at '{directory_path}'", file=sys.stderr)
        return False

    print(f"Starting deletion of '{directory_path}'...")
    error_count = 0

    try:
        # Walk the tree from the bottom up
        for root, dirs, files in os.walk(directory_path, topdown=False):
            # Delete files
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Error deleting file {file_path}: {e}", file=sys.stderr)
                    error_count += 1

            # Delete directories
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    os.rmdir(dir_path)
                except OSError as e:
                    print(f"Error deleting directory {dir_path}: {e}", file=sys.stderr)
                    error_count += 1

        # Delete the top-level directory itself
        os.rmdir(directory_path)

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return False

    if error_count == 0:
        print("Directory deletion process completed successfully.")
        return True
    else:
        print(f"Directory deletion process completed with {error_count} errors.")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_redundant_paises.py <path_to_directory>", file=sys.stderr)
        sys.exit(1)

    target_dir = sys.argv[1]
    delete_directory_recursively(target_dir)
