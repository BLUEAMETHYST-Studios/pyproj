from json import loads, JSONDecodeError
from colorama import Fore
from sys import exit as kill

def wt(): # wt = wrong type
    print(f"[❌] {Fore.RED}One or more keys in out.json have an invalid type as values!{Fore.RESET}")
    kill()

def check_json(json):
    try:
        j = loads(json)
        if not isinstance(j["general"]["main-executable"], str):
            wt()
        if not isinstance(j["general"]["out-name"], str):
            wt()
        if not isinstance(j["general"]["console-application"], bool):
            wt()
        if not isinstance(j["general"]["onefile"], bool):
            wt()
        if not isinstance(j["general"]["only-ascii"], bool):
            wt()
        if not isinstance(j["general"]["clean-cache"], bool):
            wt()
        if not isinstance(j["windows-osx-specific"]["disable-windowed-traceback"], bool):
            wt()
        if not isinstance(j["windows-specific"]["prompt-uac"], bool):
            wt()
        if not isinstance(j["osx-specific"]["argv-emulation"], bool):
            wt()
        if not isinstance(j["custom-arguments"], list):
            wt()
    except KeyError:
        print(f"[❌] {Fore.RED}One or more required key(s) isn't exisiting in the out.json file!{Fore.RESET}")
        kill()