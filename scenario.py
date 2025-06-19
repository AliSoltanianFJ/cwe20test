user_input = input("Enter filename: ")
# open the file and read the contents
try:
    with open(user_input, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
