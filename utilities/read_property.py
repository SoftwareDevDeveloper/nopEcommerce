import configparser

config = configparser.RawConfigParser()
config.read("./base/init")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common.info", "email")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
