#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import platform

class MacCleaner:
    def __init__(self, __dir_path=os.path.dirname(os.path.realpath(__file__))):
        if platform.system() == "Darwin":
            self.__user_name = os.getlogin()
            if os.path.exists("/usr/local/bin/MacCleaner") == False:
                os.system("chmod 700 " + __file__)
                shutil.copy(__file__, "/usr/local/bin/MacCleaner")
                print("MacCleaner is installed:")

    def __delete_folder(self, __folder_path):
        new_path = __folder_path.replace(" ", "")
        if os.path.exists(__folder_path):
            if " " in __folder_path:os.rename(__folder_path, new_path)
            os.system(f"rm -rf {new_path}/*")
            print("cleaned: " + new_path)
    def _clean(self):
        self.__delete_folder(f"/Users/{self.__user_name}/Library/Developer/Xcode/DerivedData")
        self.__delete_folder(f"/Users/{self.__user_name}/Library/Developer/Xcode/iOS Device Support")
        self.__delete_folder(f"/Users/{self.__user_name}/.AppLogsSymLinksForCleanMe")
        self.__delete_folder(f"/Users/{self.__user_name}/.AppCacheSymLinksForCleanMe")
        self.__delete_folder(f"/Users/{self.__user_name}/Library/Caches")
        self.__delete_folder(f"/Users/{self.__user_name}/Library/Logs")


if __name__ == "__main__":
    gm = MacCleaner()
    gm = gm._clean()
