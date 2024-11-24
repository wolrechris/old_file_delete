import os
import time

# Default values (will be overwritten by environment variables)
DELETE_FOLDERS = False # Delete empty folders
DELETION_AGE = 172800 # Age of files in seconds that will be deleted (default: 172800s = 48h)

# Configuration
path = "/delete"
dir_names = []

def delete_files(folder, n_seconds, del_dirs):
    now = time.time()
    for root, dirs, files in os.walk(folder, topdown=False):
        # Delete files older than n_hours
        for file in files:
            file_path = os.path.join(root, file)
            file_age = now - os.path.getmtime(file_path)
            if file_age > n_seconds:
                print(f"Deleting file: {file_path} (Age: {file_age/3600:.2f} hours)")
                os.remove(file_path)
        
        # Optionally delete empty directories
        if del_dirs:
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):  # Check if the directory is empty
                    print(f"Deleting empty directory: {dir_path}")
                    os.rmdir(dir_path)

    # Check if the root folder itself is empty
    if del_dirs and not os.listdir(folder):
        print(f"Deleting root folder as it's empty: {folder}")
        os.rmdir(folder)


# Parse and handle DELETE_FOLDERS and DELETION_AGE env variables
env_var_delete_folders = os.getenv('DELETE_FOLDERS')
env_var_deletion_age = os.getenv('DELETION_AGE')

if env_var_delete_folders is None:
    print("Environment variable 'A' is not set. Using default value: ", DELETE_FOLDERS)
    rm_dirs = DELETE_FOLDERS
else:
    rm_dirs = env_var_delete_folders.lower() in ['true', '1', 'yes', 'on']

if env_var_deletion_age is None:
    print("Environment variable 'B' is not set. Using default value:", DELETION_AGE)
    rm_age = DELETION_AGE
else:
    try:
        rm_age = int(env_var_deletion_age)
    except ValueError:
        print(f"Invalid value for environment variable 'B': {env_var_deletion_age}. Using default value:", DELETION_AGE)
        rm_age = DELETION_AGE

# Save list of dirs to be deleted
if os.path.exists(path):
    # Some failsaves
    if(path in ["", "/", "~"]):
        print(f"Forbidden directory was found as path to be deleted: {path}. Exiting...")
        exit(1)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dir_names.append(item)

    # Print the list of directory names
    print("Directories found:", dir_names)
else:
    print(f"The path '{path}' does not exist.")
    exit(1)

# Run the cleanup function
for subdir in dir_names:
    print(f"Iterating through {subdir}...")
    delete_files(subdir, rm_age, rm_dirs)