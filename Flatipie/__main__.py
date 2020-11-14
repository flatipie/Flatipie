



import os, sys
import shutil
import datetime
import json
import subprocess

class Resources(object):
    def __init__(self, path):
        self.path = path

    def compile_rc(self):
        try:
            w = open(self.path + "\\package.json", "r")
        except FileNotFoundError:
            print("package.json is missing in the directory")

        data = json.load(w)
        rc_path = data["resources"]["resource_file"]
        compiled_path = data["resources"]["compiled_path"]

        subprocess.run("pyrcc5 -o {} -root {}".format(compiled_path, rc_path))
        

class Run(object):
    def __init__(self, path):
        self.path = path

    def run_package(self):
        try:
            w = open(self.path + "\\package.json", "r")
        except FileNotFoundError:
            print("package.json is missing in the directory")

        data = json.load(w)
        script = data["main"]
        print("Thank you for using Flatpie - {} https://github.com/zenqiwp".format(__import__("Flatipie").__version__))
        subprocess.run(f"python {script}")
        

class Build(object):
    def __init__(self, path):
        self.path = path
        self.verpatch = os.path.dirname(os.path.abspath(__file__)) + "\\bin\\verpatch.exe"

    def create_exe(self):
        
        

        try:
            # print(self.path + "\\package.json")
            d = open(self.path + "\\package.json")
        except FileNotFoundError:
            print("package.json is missing in the directory")

        data = json.load(d)
        d.close()

        
        name = data["name"]
        script = data["main"]
        icon = data["build"]["icon"]
        file_to_add = data["build"]["add_data"]
        exe_path = data["build"]["exe_path"]
        version = data["version"]
        author = data["author"]
        description = data["description"]
        copyrightInfo = data["copyright"]

        if icon == None:
            icon = "src/resources/icon.ico"

        isOnedir = data["build"]["onedir"]


        
        if isOnedir == True:
            subprocess.run("pyinstaller -F -w -i {} --name {} --add-data {} --distpath {} {}".format(icon, name, file_to_add, exe_path, script))

        else:
            subprocess.run("pyinstaller -w -i {} --name {} --add-data {} --distpath {} {}".format(icon, name, file_to_add, exe_path, script))

class Create(object):
    def __init__(self, path):
        self.path = path
        self.abs_path = os.path.dirname(os.path.realpath(__file__))

    def create_package_json(self, path, name, version, author, description):
        now = datetime.datetime.now()
        copyrightInfo = f"Copyright (c) {author}, {now.year}. All rights reserved"

        package = """{
    "name": "%s",
    "version": "%s",
    "author": "%s",
    "description": "%s",
    "copyright": "%s",
    "main": "main.py",
    "build": {
        "exe_path": "./bin",
        "icon": "src/resources/icon.ico",
        "add_data": "src;.",
        "onedir": true
    },
    "resources": {
        "resource_file": "resources/rc.qrc",
        "compiled_path": "resources/rc.py"
    } 
}
"""%(name, version, author, description, copyrightInfo)
        
 
        
        with open(path, "w") as f:
            f.write(package)

    def create_directory(self, dir_path):
        try:
            os.mkdir(dir_path)
            os.mkdir(dir_path + r"\src")
            os.mkdir(dir_path + r"\src\resources")
            os.mkdir(dir_path + "\\src\\resources\\icons")
        
        except OSError:
            print("The project folder named '{}' already exist".format(dir_path))

    def copy_files(self, path):
        self.create_directory(path)
        
        try:
            shutil.copy(f"{self.abs_path}\\create\\src\\app.py", path + r"\src")
            shutil.copy(f"{self.abs_path}\\create\\main.py", path)
            shutil.copy(f"{self.abs_path}\\create\\src\\resources\\rc.qrc", path + "\\src\\resources")
            shutil.copy(f"{self.abs_path}\\create\\src\\resources\\icons\\icon.ico", path + "\\src\\resources\\icons")

        except Exception:
            self.create_files(path)

    def create_files(self, path):
        return path

    def create_project(self):
        
        projectName = input("[-] Project Name: ")
        projectVersion = input("[-] Project Version: ")
        projectDescription = input("[-] Description: ")
        projectAuthor = input("[-] Author: ")

        projectpath = f"{self.path}\\{projectName}"
        package_path = f"{projectpath}\\package.json"
        self.copy_files(projectpath)
        self.create_package_json(package_path, projectName, projectVersion, projectAuthor, projectDescription)
            
            



def usage():
    import requests

    try:
        req = requests.get("https://raw.githubusercontent.com/flatipie/Flatipie/main/update.json").json()
        is_update = req["update"]
        update_info = req["updateInfo"]
        
    except Exception:
        update_info = "The system cannot check for the updates at this time"
    
    print(f"""
        db8          |   
        Y8P          | 
                     | Welcome to Flatipie 
88888b. 888 .d88b.   | Version {__import__("Flatipie").__version__}
888 "88b888d8P  Y8b  | 
888  88888888888888  | A easiest way to create modern qt applications
888 d88P888Y8b.      | 
88888P" 888 "Y8888   | Whats NEW? 
888                  |    
888                  |  {update_info}
888                  |
                     |

Usage:

create  - Create your project
run     - Run your project (contains package.json)
build   - Build your project to EXE file (contains package.json)

""")



def pie():
    try:
        if sys.argv[1] == "create":
            project = Create(os.getcwd())
            project.create_project()
        
        elif sys.argv[1] == "run":
            run = Run(os.getcwd())
            run.run_package()
        
        elif sys.argv[1] == "build":
            builder = Build(os.getcwd())
            builder.create_exe()

        elif sys.argv[1] == "compile_resources":
            rc = Resources(os.getcwd())
            rc.compile_rc()
        
        else:
            usage()

    except IndexError:
        usage()
        

if __name__ == "__main__":
    pie()
