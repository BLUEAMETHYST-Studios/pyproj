from os import mkdir, getcwd
from sys import exit as kill
from colorama import Fore
from platform import system
from time import time

start = time()

gitattributes = """
* text=auto
""".replace("\n", "", 1)

gitignore = """
/dist
/build
*.spec
*.exe
*.dll""".replace("\n", "", 1)

outjson = """
["pyinstaller", "--noconfirm", "--onefile", "--console", "--name", "OUTPUT", "src/main.py"]""".replace("\n", "", 1)

try:
    mkdir("src")
    open(".gitattributes" ,"w").write(gitattributes)
    open(".gitignore").write(gitignore)
    open("README.md", "w").write("# " + {getcwd().split("/")[-1]} + "\nA Python application.")
    if system() == "Windows":
        print(f"Detected Operating System {Fore.CYAN}Windows{Fore.RESET}, setting EXE-Output as default output ...")
        outjson = outjson.replace("OUTPUT", "output.exe")
    elif system() == "Linux":
        print(f"Detected Operating System {Fore.CYAN}Linux{Fore.RESET}, setting Linux-Binary-Output as default output ...")
        outjson = outjson.replace("OUTPUT", "output")
    elif system() == "Darwin":
        print(f"Detected Operating System {Fore.CYAN}Darwin{Fore.RESET}, setting MacOS-Appbundle as default output ...")
        outjson = outjson.replace("OUTPUT", "output.app")
    open("out.json", "w").write(outjson)
    open("src/main.py", "w").write('print("Hello Python!")')
except Exception:
    print(f"{Fore.RED}[ERROR] Can't create package!{Fore.RESET}")
    kill()

print(f"Application-creation process completed within {time() - start:.2f} seconds!")