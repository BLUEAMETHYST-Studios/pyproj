## The fast way (but not the most reliable one)

Read the [QUICK_INSTALL.md](https://github.com/BLUEAMETHYST-Studios/pyproj/blob/main/QUICK_INSTALL.md) file to get a single command, which downloads, builds and installs Pyproj.

# Installation - Windows

## Building it yourself

1. If you haven't already, get Python.
2. After the installation check if Python311/scripts is in your Path Variable, if not add it.
3. Execute the following command within your terminal:

```
pip install pyinstaller && pip install colorama
```

4. Clone the source code of this project
5. Open **Powershell** and locate to the newly created directory containing the source code
6. Enter the following commands within **Powershell**:

```powershell
Set-ExecutionPolicy unrestricted
.\build.ps1
.\install.ps1
```

# Installation - GNU/Linux


**(Might work on MacOS, but not confirmed)**

## Building it yourself

**THE ENTIRE BUILDING PROCESS WILL BE DONE WITHIN A TERMINAL**

1. Python 3 is usually preinstalled on GNU/Linux, if not install it.
2. Install pip, the Python Packager Manager, if you haven't already.
3. Install the dependencies by entering those commands:

```
pip install pyinstaller
pip install colorama
```

4. Clone the repository

```sh
git clone https://github.com/BLUEAMETHYST-Studios/pyproj.git
```

5. Locate into the newly by Git created directory
6. Enter the following commands to install pyproj

```sh
make build
sudo make install
```