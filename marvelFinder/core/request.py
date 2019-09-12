# -*- coding: utf-8 -*-
import requests
import os
import configparser

class RequestMarvel:
    def marvelApi(dynamicPath):
        config = configparser.ConfigParser()
        configPath = os.path.abspath("./marvelFinder/core/config.ini")
        config.read(configPath)
        url = config.get("api", "MARVEL_BASE_PATH") + dynamicPath + config.get("api", "MARVEL_APIKEY")
        response = requests.get(url).json()
        data = response['data']['results']
        return data
        