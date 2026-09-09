# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder

import os

print(f"current working dir is {os.getcwd()}")

print(os.listdir())

print(os.mkdir("NEW_FOLDER"))