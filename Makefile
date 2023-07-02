# Pyproj Builder for Linux Systems

clean:
	rm pyproj.spec
	rm -rf build
	rm -rf dist
build:
	pyinstaller --noconfirm --onefile --console --name "pyproj" "src/main.py"
install:

uninstall:
