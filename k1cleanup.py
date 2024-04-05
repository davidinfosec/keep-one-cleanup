import os
import shutil

def clean_directory(root_dir, keep_file):
    """
    Walks through all directories within the specified root directory
    and deletes all files and directories except the specified keep_file.

    :param root_dir: The root directory to clean up
    :param keep_file: The file to keep, everything else will be deleted
    """
    if not os.path.isdir(root_dir) or not os.path.exists(os.path.join(root_dir, keep_file)):
        print("Root directory or keep file path is invalid. Please edit the script and specify valid paths.")
        return
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Loop through each file in the directory
        for filename in filenames:
            if filename != keep_file:
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        # If you also want to delete empty directories or directories that
        # only contained files that were deleted, you can loop through dirnames
        # and delete them. Be cautious, as this will delete directories that are now
        # empty because of the script's actions.
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            # Check if the directory is empty
            if not os.listdir(dir_path):
                shutil.rmtree(dir_path)
                print(f"Deleted directory: {dir_path}")

# Define the root directory and the file you want to keep
root_dir = r""
keep_file = ""

# Clean the directory
clean_directory(root_dir, keep_file)
