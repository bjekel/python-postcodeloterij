# -*- coding:utf-8 -*-

import os
import time
import logging
import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from requests.compat import json
import urllib.parse

_LOGGER = logging.getLogger(__name__)

BASE_URL = 'https://www.postcodeloterij.nl/web/rest/gdrm/getmywinnings/npl/P_MT_P'

class Prize(object):
    def __init__(self, key, hasWon, description, imageUrl):
        self._key = key
        self._hasWon = hasWon
        self._description = description
        self._imageUrl = imageUrl

class PostcodeLoterij(object):
    def __init__(self, postalCode, month, year):
        self._postalCode = postalCode
        self._month = month
        self._year = year

    def buildUrl(self):
        payload = {'postalCode': self._postalCode, 'resultSize': 1}
        params = urllib.parse.urlencode(payload)
        url = BASE_URL + self._year + self._month + '?' + params
        return url

    def getPrizes(self):
        response = requests.get(self.buildUrl())
        json = response.json()
        wonPrizesJson = json['wonprizes']
        enrichedDataJson = json['enricheddata']

        wonPrizes = []

        for prize in wonPrizesJson:
            data = [x for x in enrichedDataJson if x['contentid'] == prize['contentid']][0]
            wonPrizes.append(Prize(prize['key'], prize['haswon'], prize['descr'], data['offsetimgurl']))

        return wonPrizes