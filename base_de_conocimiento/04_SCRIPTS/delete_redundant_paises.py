import os
import sys
import shutil

def delete_directory_recursively(directory_path):
    """
    Deletes a directory and all its contents recursively.
    This function is designed to be more robust than a simple shell command,
    especially in environments with limitations on the number of files that
    can be handled in a single operation.

    It walks the directory tree from the bottom up, deleting files first,
    then the now-empty directories.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at '{directory_path}'")
        return

    print(f"Starting deletion of '{directory_path}'...")
    error_count = 0

    for root, dirs, files in os.walk(directory_path, topdown=False):
        # Delete files in the current directory
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)
                # print(f"Deleted file: {file_path}")
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")
                error_count += 1

        # Delete subdirectories in the current directory (they should be empty now)
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
                # print(f"Deleted directory: {dir_path}")
            except OSError as e:
                print(f"Error deleting directory {dir_path}: {e}")
                error_count += 1

    # Finally, delete the top-level directory itself
    try:
        os.rmdir(directory_path)
        print(f"Successfully deleted top-level directory: {directory_path}")
    except OSError as e:
        print(f"Error deleting top-level directory {directory_path}: {e}")
        error_count += 1

    if error_count == 0:
        print("Directory deletion process completed successfully.")
    else:
        print(f"Directory deletion process completed with {error_count} errors.")

if __name__ == "__main__":
    # The script is hardcoded to the specific redundant directory to avoid accidental deletion
    # of other important directories.
    target_directory = "base_de_conocimiento/paises"

    # For safety, let's get the absolute path and verify it's the one we want
    abs_path = os.path.abspath(target_directory)

    if "base_de_conocimiento/paises" not in abs_path:
        print(f"SAFETY CHECK FAILED: The target path '{abs_path}' does not seem to be the correct one.")
        sys.exit(1)

    delete_directory_recursively(target_directory)
