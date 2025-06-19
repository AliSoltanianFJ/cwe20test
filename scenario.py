import os

directory = input("Enter the directory to list: ")
# run the command to list files in the directory
command = f"ls -l {directory}"
os.system(command)
