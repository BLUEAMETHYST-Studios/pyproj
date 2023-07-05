# Pyproj Builder for Linux Systems

clean:
	rm pyproj.spec
	rm -rf build
	rm -rf dist
build:
	pyinstaller --noconfirm --onefile --console --name "pyproj" "src/main.py"
install:
	if [ "$(id -u)" != "0" ]; then
    	echo -e "\e[31mPlease execute as root (sudo)!\e[0m"
    	exit 1
	fi
	cp dist/pyproj /usr/bin/pyproj
	chmod +x /usr/bin/pyproj
uninstall:
	if [ "$(id -u)" != "0" ]; then
    	echo -e "\e[31mPlease execute as root (sudo)!\e[0m"
    	exit 1
	fi
	rm /usr/bin/pyproj
