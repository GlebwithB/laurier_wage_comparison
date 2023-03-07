from bs4 import BeautifulSoup
import numpy as np
import requests
import selenium
import sys


def safe_print(data):
    # can also use 'replace' instead of 'ignore' for errors= parameter
    print(str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


def safe_transfer(data):

    data = (str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    return data

def type_print(data):

    safe_print(type(data), "\n", str(data), "\n", len(data))

def cleanse(list_set, keywords = {"":1}):
        for key in keywords.keys:
            for item in (list_set, keywords[key]):
                item.replace(key, "")




def scrap_web(url, parser, content_parse = {"Name": False, "Year": False, "Salary":False, "Position": False, "Employer":False}):

    def safe_transfer(data):
        data = (str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        return data

    


    #temporary to test true or false
    #content_parse = {"Name": True, "Year": True, "Salary":True, "Position": True, "Employer":True}

    soup = BeautifulSoup(safe_transfer(requests.get(url).text), parser)
    data = [(x.text.strip().replace("\n", "").replace("\r", "")) for x in soup.find("tbody").find_all("td")]
    

    return data


    
    
    
