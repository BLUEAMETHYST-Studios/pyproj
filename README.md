# Pyproj

Python Project Maker and Builder

## Installation

Read the [INSTALLATION.md](https://github.com/BLUEAMETHYST-Studios/pyproj/blob/main/INSTALLATION.md) file.

## Using Pyproj

### Creating a simple Python application

```
pyproj new default {name}
```

### Creating a new Python Package for PyPi

```
pyproj new package {name}
```

### Building a normal Python application

```
pyproj build
```

### Building a Python package

**Windows:**

```
pyproj-make build
```

**GNU/Linux or MacOS:**

```
make build
```

### Releasing your Python package

#### **NOTE: THE PACKAGE MUST BE BUILT FIRST, BEFORE RELEASING IT**

**Windows:**

```
pyproj-make release
```

**GNU/Linux or MacOS:**

```
make release
```