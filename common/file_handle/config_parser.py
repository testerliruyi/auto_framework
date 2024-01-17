"""
重写解析对象
"""
import configparser


class MyConfigParser(configparser.ConfigParser):
    def _init_(self,defaults=None):
        configparser.ConfigParser.init_(self,defaults=None)

    def optionxform(self,optionstr):
        return optionstr