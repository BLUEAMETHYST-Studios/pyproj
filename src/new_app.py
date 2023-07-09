from os import mkdir, getcwd
from sys import exit as kill
from colorama import Fore
from platform import system
from time import time

start = time()

print("Creating new application ...")

gitattributes = """
* text=auto
""".replace("\n", "", 1)

gitignore = """
/dist
/build
*.spec
*.exe
*.dll""".replace("\n", "", 1)

if system() == "Windows":
    outname = "output.exe"
elif system() == "Linux":
    outname = "output"
elif system() == "Darwin":
    outname = "output.app"
else:
    outname = "output.o"

outjson = """
{
    "general": {
        "main-executable":"src/main.py",
        "out-name":"OUTNAME",
        "console-application":true,
        "onefile":true,
        "only-ascii":false,
        "clean-cache":false
    },

    "windows-osx-specific": {
        "disable-windowed-traceback":false
    },

    "windows-specific": {
        "prompt-uac":false
    },

    "osx-specific": {
        "argv-emulation":false
    },

    "custom-arguments":[]
}""".replace("\n", "", 1).replace("OUTNAME", outname)

try:
    mkdir("src")

    gita = open(".gitattributes" ,"w")
    gita.write(gitattributes)
    gita.close()

    giti = open(".gitignore", "w")
    giti.write(gitignore)
    giti.close()

    readme = open("README.md", "w")
    readme.write("# " + getcwd().split("/")[-1] + "\nA Python application.")
    readme.close()

    outj = open("out.json", "w")
    outj.write(outjson)
    outj.close()

    mainpy = open("src/main.py", "w")
    mainpy.write('print("Hello World!")')
    mainpy.close()

except Exception:
    print(f"[❌] {Fore.RED}Can't create package!{Fore.RESET}")
    kill()

print(f"[✅] Application-creation process {Fore.GREEN}completed{Fore.RESET} within {Fore.CYAN}{time() - start:.2f}{Fore.RESET} seconds!")