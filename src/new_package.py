from os import mkdir
from sys import exit as kill
from colorama import Fore
from platform import system
from time import time

makefile = """# Pyproj Package Packaging Makefile
build:
    python3 setup.py sdist bdist_wheel
release:
    twine upload dist/*
"""

batchfile = """:: Pyproj Package Packaging Batchfile
if %1 == build goto build
if %1 == release goto release
if NOT %1 == build goto exit
if NOT %1 == release goto exit

:build
python setup.py sdist bdist_wheel
exit

:release
twine upload dist/*
exit

:exit
exit
"""

def newPackage():
    try:
        pkgName = input("Package Name: ")
        pkgAuthor = input("Package Author: ")
        pkgDesc = input("Short Package description: ")
        pkgKWs = input("Package Keywords (seperate by comma): ")
        pkgLicense = input("Package License: ")
        setuppy = f"""# Package Packaging Script
from setuptools import setup, find_packages
        
readme = open("README.md", "r").read()

setup (
    name="{pkgName}",
    version="1.0.0",
    description="{pkgDesc}",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{pkgAuthor}",
    packages=find_packages(),
    keywords={pkgKWs.split(",")},
    license="{pkgLicense}"
)

"""

        print("Creating your package ...")
        start = time()
        mkdir(pkgName)
    except FileExistsError:
        print(f"[❌] {Fore.RED}Directory with name {pkgName} already exists!{Fore.RESET}")
        kill()
    except Exception:
        print(f"[❌] {Fore.RED}Can't create package!{Fore.RESET}")
        kill()

    initpy = open(f"{pkgName}/__init__.py", "w")
    initpy.write("# This is the main file for your package.")
    initpy.close()

    giti = open(".gitignore", "w")
    giti.write(f"/dist\n/{pkgName}.egg-info\n/build\n__pycache__")
    giti.close()

    gita = open(".gitattributes", "w")
    gita.write("* text=auto")
    gita.close()

    readme = open("README.md", "w")
    readme.write(f"# {pkgName}\n{pkgDesc}")
    readme.close()

    setuppyfile = open("setup.py", "w")
    setuppyfile.write(setuppy)
    setuppyfile.close()
    
    if system() == "Linux":
        print(f"Detected Operating System {Fore.CYAN}Linux{Fore.RESET}, creating Makefile ...")
        open("Makefile", "w").write(makefile)
    elif system() == "Darwin":
        print(f"Detected Operating System {Fore.CYAN}Darwin{Fore.RESET}, creating Makefile ...")
        open("Makefile", "w").write(makefile)
    elif system() == "Windows":
        print(f"Detected Operating System {Fore.CYAN}Windows{Fore.RESET}, creating Batchfile ...")
        open("pyproj-make.bat", "w").write(batchfile)
    else:
        print("[❌] Was not able to detect system, no file for automation will be created.")
    
    print(f"[✅] Package-creation process {Fore.GREEN}completed{Fore.RESET} within {Fore.CYAN}{time() - start:.2f}{Fore.RESET} seconds!")