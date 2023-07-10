from json import loads

def parsejson(json):
    j = loads(json)
    args = ["pyinstaller", "--noconfirm"]
    args.append("--name")
    args.append(j["general"]["out-name"])

    if j["general"]["console-application"]:
        args.append("--console")
    else:
        args.append("--windowed")

    if j["general"]["onefile"]:
        args.append("--onefile")
    else:
        args.append("--onedir")

    if j["general"]["only-ascii"]:
        args.append("--ascii")

    if j["general"]["clean-cache"]:
        args.append("--clean")

    if j["windows-osx-specific"]["disable-windowed-traceback"]:
        args.append("--disable-windowed-traceback")
    
    if j["windows-specific"]["prompt-uac"]:
        args.append("--uac-admin")

    if j["osx-specific"]["argv-emulation"]:
        args.append("--argv-emulation")

    for carg in j["custom-arguments"]:
        args.append(carg)

    args.append(j["general"]["main-executable"])

    return args