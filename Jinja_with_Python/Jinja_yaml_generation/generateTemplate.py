#!/usr/bin/python

import yaml
from yaml.loader import SafeLoader

from jinja2 import Environment, FileSystemLoader

import os

# Reading the config.yaml to get the values to pass to .j2 file
def readYAML():
    with open('config.yaml') as f:
        values = yaml.load(f, Loader=SafeLoader)
    return values

# To check if the resultFile folder exists and create the SVC-service-name.yaml files
def resultFileCheck():
     
        loc = './resultFile'
        values = readYAML()

        if (os.path.exists(loc)):
            print("[INFO]resultFile Folder exists. Delete.")
            return 1
        else:
            print("[INFO]Creating resultFile.")
            os.mkdir(loc)
            if (os.path.exists(loc)):
                for service in values["services"]:
                    filePath=loc+'/'+'SVC-'+service['name']+'.yaml'
                    if (os.path.exists(filePath)):
                        open(filePath, 'x')
            print("[INFO]resultFile created.")
    
 
if __name__ == "__main__":
    
    # Load templates files from the template folder
    env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('component_tmpl.j2')

    values = readYAML()
    res = resultFileCheck()

    if res == 1:
        print("[WARNING] DELETE resultFile FOLDER TO GENERATE YAML.")
    else:
        print("[INFO]Generating YAML.")
        for service in values["services"]:
            file = open("resultfile/SVC-"+service['name']+".yaml", "w")
            file.write(template.render(service))
            file.close()
        print("[INFO]YAML generated.")