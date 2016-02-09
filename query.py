import urllib2
import re
import time
import datetime
import json
import glob
from collections import defaultdict
    
class Query:
    def __init__(self, server, baseUrl, apiKey, params):
        self.server = server
        self.apiKey = apiKey
        self.params = params
        self.baseUrl = baseUrl
        self.url = self.generateUrl()
    
    def generateUrl(self):
        formatValues = [self.server] + self.params + [self.apiKey]
        url = self.baseUrl.format(*formatValues)
        return url
    
    def fetchData(self):
        response = None
        try:
            response = urllib2.urlopen(self.url)
        except:
            return None
        html = response.read()
        response.close()
        return html
