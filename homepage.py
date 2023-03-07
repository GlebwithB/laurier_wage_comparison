from functions import importlist
import requests, selenium, requests, os, sys, matplotlib.pyplot as plt, numpy as np
from bs4 import BeautifulSoup
import os


for module in importlist.split():
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[-len(importlist.split())], locals(), globals())
del module


url = "https://www.ontariosunshinelist.com/employers/wilfrid-laurier-university"
request = requests.get(url).text

