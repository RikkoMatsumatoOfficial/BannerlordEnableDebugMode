import os
import pathlib as p
import FileAttr as file_attribution
import shutil as ud
import getpass
from os import _exit as exit
def SetEngineConfigAsDebug():
    engineconf = str("engine_config.txt")
    if p.Path(engineconf):
        print("Succesfully Founded File!!!")
        with open(engineconf, "r") as f:
            for file in f:
                print(file)
                confirm = input("Do you Confirm this Configuration? ")
                if(confirm == "y"):
                    username = str(getpass.getuser())
                    bannerlord_doc = str("C:\\Users\\{}\\Documents\\Mount and Blade II Bannerlord".format(username))
                    if(p.Path("C:\\Users\\{}\\Documents\\Mount and Blade II Bannerlord".format(username) + "\\Configs\\engine_config.txt")):
                        print("Founded this File(Original engine_config.txt)!!!")
                        os.remove("C:\\Users\\{}\\Documents\\Mount and Blade II Bannerlord".format(username) + "\\Configs\\engine_config.txt")
                        ud.copy("engine_config.txt", "C:\\Users\\{}\\Documents\\Mount and Blade II Bannerlord".format(username) + "\\Configs\\engine_config.txt")
                        file_attribution.SetFileAttribute(bytes("C:\\Users\\{}\\Documents\\Mount and Blade II Bannerlord".format(username) + "\\Configs\\engine_config.txt", "utf-8"), 0x1) # 0x1 is Only Read File!!!
                        os.remove("engine_config.txt")
                        print("Successfully Added Debug Mode!!! Created by RikkoMatsumatoOfficial!!!")
                        exit(443)
    else:
        print("Not Founded engine_config.txt!!!")
        exit(321)
                        
