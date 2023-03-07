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

