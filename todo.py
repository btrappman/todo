import sys
import datetime

def main():
    # Incorrect nunmber of arguments
    if len(sys.argv) == 1:
        help()
        sys.exit(1)

    # Help 
    command = sys.argv[1]
    if command == "help":
        help()

    print("success")

# Displays usage
def help():
    # Triple quotes allow strings that span multiple lines
    help = """Usage:
    $ ./todo help       # Usage"""

    print(help)

# Runs main
if __name__ == "__main__":
    main()