import os

directory = input("Enter the directory to list: ")
# run the command to list files in the directory
os.system(f"ls -l {directory}")
