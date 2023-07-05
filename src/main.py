from sys import argv, exit as kill
from colorama import Fore, init

init(autoreset=True)

if len(argv) < 2:
    print(f"{Fore.RED}[ERROR] Not enough arguments!{Fore.RESET}")
    print("Use the --help or -h argument for help.")
    kill()

def mkDir():
    try:
        newdir(argv[3])
    except IndexError:
        print(f"{Fore.RED}[ERROR] Not enough arguments!{Fore.RESET}")
        print("Set the 4th argument to the name of your project.")
        kill()

if "--help" or "-h" in argv:
    from help import pyproj_help
    pyproj_help()

if "--version" or "-v" in argv:
    print("Pyproj Version Beta 1.0.0")

if argv[1] == "new":
    try:
        if argv[2] == "default":
            from newdir import *
            mkDir()
            from new_app import *
        elif argv[2] == "package":
            from newdir import *
            mkDir()
            from new_package import *
            newPackage()
        else:
            print(f"{Fore.RED}[ERROR] Not enough arguments!{Fore.RESET}")
            print("Set the 2nd argument to one of the following:")
            print("")
            print("default - A normal Python application")
            print("package - A Python Package made to be uploaded to PyPi")
            kill()
    except Exception as x:
        print(f"{Fore.RED}[ERROR] Unknown unexpected exception.{Fore.RESET}")
        if input('Enter "x" to view the reason: ') == "x":
            print(x)
        kill()
elif argv[1] == "build":
    from outjson import *
    parse_and_make()



    