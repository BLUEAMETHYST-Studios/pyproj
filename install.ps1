New-Item "C:/Users/$Env:USERNAME/AppData/Local/pyproj" -ItemType "directory"
xcopy.exe "dist" "C:/Users/$Env:USERNAME/AppData/Local/pyproj"
[Environment]::SetEnvironmentVariable("Path", $Env:PATH + ";C:/Users/$Env:USERNAME/AppData/Local/pyproj;", "User")