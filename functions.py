<<<<<<< HEAD
importlist = """
    selenium
    bs4
    requests
    sys
    matplotlib
    numpy
"""
=======
from bs4 import BeautifulSoup
import numpy as np, requests, selenium, sys, matplotlib.pyplot as plt 

def safe_print(data):
    # can also use 'replace' instead of 'ignore' for errors= parameter
    print(str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


def safe_transfer(data):

    data = (str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    return data

def type_print(data):

    safe_print(type(data), "\n", str(data), "\n", len(data))

def cleanse(list_set, keywords = {" ":1}):
        
        for x in list(keywords.keys()):
            print(x)
            list_set = [list_set[y].replace(x, "")for y in range(0, len(list_set), keywords[x])]
    
        return list_set




def scrap_web(url, parser, content_parse = {"Name": False, "Year": False, "Salary":False, "Position": False, "Employer":False}):

    def safe_transfer(data):
        data = (str(data).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        return data
    #temporary to test true or false
    #content_parse = {"Name": True, "Year": True, "Salary":True, "Position": True, "Employer":True}

    soup = BeautifulSoup(safe_transfer(requests.get(url).text), parser)
    data = [(x.text.strip().replace("\n", "").replace("\r", "")).replace(",", "") for x in soup.find("tbody").find_all("td")]
    

    return data


    
    
    
>>>>>>> d39dc3395ce181bc64205d41a9b975d3f9f0a273
