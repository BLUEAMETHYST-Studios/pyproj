clean:
	rm pyproj.spec
	rm -rf build
	rm -rf dist
build:
	pyinstaller --noconfirm --onefile --console --name "pyproj" "src/main.py"
install:
	cp dist/pyproj /usr/bin/pyproj
	chmod +x /usr/bin/pyproj
uninstall:
	rm -f /usr/bin/pyproj
