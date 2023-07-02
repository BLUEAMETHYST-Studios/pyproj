def pyproj_help():
    print("""
==========[ PyProj Help ]==========

Creating a new project:

$ pyproj new {type} {name}

Supported types:

- default
- package

-----------------------------------
Building an existing project:

If project is default:

$ pyproj build

If project is package:

On Windows:

To build your package:

$ pyproj-make build

To release your package:

$ pyproj-make release

On Linux or Darwin:

To build your package:

$ make build

To release your package:

$ make release



""")