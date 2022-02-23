import sys
import datetime

def main():
    # Incorrect nunmber of arguments
    #if len(sys.argv) == 1:
        #help()
    try:
        # User command
        command = sys.argv[1]

        # Add new todo item
        if command == "add" and len(sys.argv) != 3:
            help()
        elif command == "add":
            newTodo = sys.argv[2]
            add(newTodo)
            
        # Print help menu
        if command == "help":
            help()
        
        # Check successful add()
        with open("todo.txt", "r") as file:
            print(file.read())

        # Test successful run
        print("success")
        sys.exit(0)
    
    except Exception as e:
        print(f"Error: {e}")
        help()

# Add new todo item
def add(newItem):
    with open("todo.txt", "a") as file:
        file.write(newItem)
        file.write("\n")
    newItem = '"' + newItem + '"'
    print(f"Successfully added: {newItem}")

# Loads todo list into dictionary
# TODO: 
def load():
    with open("todo.txt", "r") as file:
        itemNum = 1
        for line in file:
            line = line.strip("\n")


# Displays usage
def help():
    # Triple quotes allow strings that span multiple lines
    help = """Usage:
    $ ./todo add "todo item"        # Add new todo item
    $ ./todo help                   # Usage"""

    print(help)
    sys.exit(1)

# Runs main
if __name__ == "__main__":
    main()