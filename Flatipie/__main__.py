

#from rich import print

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


        subprocess.run("cls")
        yesorno = (f"\nThe EXE file is saved in {exe_path}. Would you like to create resource version for it? (Y/N): ")

        if yesorno == "Y" or yesorno == "YES" or yesorno == "yes":
            self.create_resources(exe_path, name, author, version, description, copyrightInfo)

        elif yesorno == "N" or yesourno == "NO" or yesorno == "no":
            print("Okay, closing the build function. Thank you for using FLatipie.")
        

    def create_resources(self, exe, name, author, version, description, copyrightInfo):
        #verpatch.exe script.exe 1.0.0.0 /va /pv 1.0.0.0 /s description "Your product description" /s product "Your product name" /s copyright "Your company name, 2016" /s company "Your company name"
        verpatch_path = os.dirname(os.abspath(__file__)) + "\\bin\\verpatch.exe"

        exe_file = exe

        if os.path.isdir(exe):
            for filename in os.listdir(exe):
                if filename.endswith(".exe"):
                    exe_file = exe + f"\{filename}"


        if copyrightInfo is None:
            now = datetime.datetime.now()
            copyrightInfo = f"Copyright (c) {projectAuthor}, {now.year}. All rights reserved"

        command = f"{verpatch_path} {exe_file} {version} /va /pv {version} /s description {description} /s product {name} /s copyright {copyrightInfo} /s company {author}"
        subprocess.run(command)

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
        
        #print(package)
        #yesno = input("is this ok?: ")
        #if yesno == "yes":
        
        with open(path, "w") as f:
            f.write(package)

        #else:
        #    pass

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

        #print("\n[-] Creating {} file @ {}".format(file, self.path))
        projectpath = f"{self.path}\\{projectName}"
        package_path = f"{projectpath}\\package.json"
        self.copy_files(projectpath)
        self.create_package_json(package_path, projectName, projectVersion, projectAuthor, projectDescription)
            
            

#copy(r"C:\Users\DSPC GUEST.Admin\Desktop\Flat\test")
#create_directory(r"C:\Users\DSPC GUEST.Admin\Desktop\Flat\test")

def usage():
    print(f"""

Welcome to Flatify {__import__("Flatipie").__version__}

Usage:

create | Build your project
run | Run your package (requires package.json)
build | Create executable files for your project (requires package.json)
create_resources | Compile .qrc files to py (requires package.json)

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