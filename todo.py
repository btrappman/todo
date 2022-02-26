import sys
import datetime

def main():
    try:
        # Load todo list into dictionary
        todoList = {}
        load(todoList)

        # User command
        if len(sys.argv) == 0:
            help()
        else:
            command = sys.argv[1]

        # Commands
        if command == "add" and len(sys.argv) == 3: # Add new todo item
            newTodo = sys.argv[2]
            add(newTodo)    
        elif command == "ls":
            ls(todoList)
        elif command == "help": # Print help menu
            help()
        
        # Check successful add()
        #with open("todo.txt", "r") as file:
            #print(file.read())
    
    except Exception as e:
        print(f"Error: {e}")
        help()

# Add new todo item
def add(newItem):
    # with open() as file properly opens and closes file
    with open("todo.txt", "a") as file:
        file.write(newItem)
        file.write("\n")
    newItem = '"' + newItem + '"'
    print(f"Successfully added: {newItem}")

# Loads todo list into dictionary
def load(todoList):
    try:
        with open("todo.txt", "r") as file:
            itemNum = 1
            for line in file:
                line = line.strip("\n")
                todoList.update({itemNum: line})
                itemNum = itemNum + 1
    except:
        print(f"Could not access todo list")

# Prints todo list
def ls(todoList):
    try:
        for x, y in todoList.items():
            print(f"{x}: {y}")
    except Exception as e:
        print(f"No current items")

# Displays usage
def help():
    # Triple quotes allow strings that span multiple lines
    help = """Usage:
    $ ./todo add "todo item"        # Add new todo item
    $ ./todo ls                     # Lists current todo items
    $ ./todo help                   # Usage"""

    print(help)
    sys.exit(1)

# Runs main
if __name__ == "__main__":
    main()