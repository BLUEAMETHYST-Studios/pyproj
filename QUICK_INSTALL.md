# Quick Installation Methods

## INFO: ALSO ONLY POSSIBLE WHEN DEPENDENCIES ARE INSTALLED

## Windows

1. Open Powershell and enter this command:

```powershell
cd C:/Users/$Env:USER && curl https://github.com/BLUEAMETHYST-Studios/pyproj/archive/refs/heads/main.zip -s -L -o "pyproj.zip" && Expand-Archive -Force pyproj.zip C:/Users/$Env:USER/pyproj-extracted && cd C:/Users/$Env:USER/pyproj-extracted/pyproj-main && Set-ExecutionPolicy unrestricted && .\build.ps1 && .\install.ps1 && cd C:/Users/$Env:USER && Remove-Item pyproj.zip && Remove-Item pyproj-extracted
```

## Linux

1. Open the terminal and enter this command:

```sh
curl https://github.com/BLUEAMETHYST-Studios/pyproj/archive/refs/heads/main.zip -s -L -o "/home/$USER/pyproj.zip" && unzip ~/pyproj.zip -d ~/pyproj-extracted && cd ~/pyproj-extracted/pyproj-main && make build && sudo make install && cd ../.. && rm -f pyproj.zip && rm -rf pyproj-extracted
```