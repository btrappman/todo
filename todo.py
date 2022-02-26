import sys
import datetime

def main():
    try:
        # Load todo list into dictionary
        todoList = {}
        
        # User command
        if len(sys.argv) == 0:
            help()
        else:
            command = sys.argv[1]

        # Commands
        if command == "add" and len(sys.argv) == 3: # Add new todo item
            newTodo = sys.argv[2]
            add(newTodo)    
        elif command == "ls" and len(sys.argv) == 2: # Lists current items
            ls(todoList)
        elif command == "rm" and len(sys.argv) == 3: # Deletes item 
            numItem = sys.argv[2]
            rm(numItem, todoList)
        #elif command == "done" and len(sys.argv) ==3: # Mark item as complete
            #numItem = sys.argv[2]
            #done()
        elif command == "help": # Print help menu
            help()
        else:
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
        print(f"No pending todo items")

# Prints todo list
def ls(todoList):
    try:
        load(todoList)
        for x, y in todoList.items():
            print(f"{x}: {y}")
    except Exception as e:
        print(f"Error: could not access todo list")

# Deletes todo item
def rm(itemNum, todoList):
    try:
        load(todoList)
        itemNum = int(itemNum)
        with open("todo.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)

            # Re-write items to file, omitting desired item to delete
            for i in lines:
                if i.strip("\n") != todoList[itemNum]:
                    file.write(i)
            
            # Deletes original (left over) list
            file.truncate()

        print(f"Successfully deleted item #{itemNum}")

    except Exception as e:
        print(f"Item #{itemNum} does not exist. Nothing deleted.")   

#def done(itemNum, todoList):
    #try:
        #update(itemNum, todoList)

# Displays usage
def help():
    # Triple quotes allow strings that span multiple lines
    help = """Usage:
    $ ./todo add "todo item"        # Add new todo item
    $ ./todo ls                     # Lists current todo items
    $ ./todo rm NUMBER              # Deletes todo item
    $ ./todo done NUMBER            # Mark todo item as complete
    $ ./todo help                   # Usage"""

    print(help)
    sys.exit(1)

# TODO: purge # completed

# Runs main
if __name__ == "__main__":
    main()