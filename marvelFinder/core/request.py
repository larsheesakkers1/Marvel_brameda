# -*- coding: utf-8 -*-
from django.conf import settings
import requests

class RequestMarvel:
    def marvelApi(dynamicPath):
        url = settings.MARVEL_BASE_PATH + dynamicPath + settings.MARVEL_APIKEY
        response = requests.get(url).json()
        data = response['data']['results']
        return data
        