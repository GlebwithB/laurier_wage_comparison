from bs4 import BeautifulSoup
import numpy as np, requests, selenium, sys, matplotlib.pyplot as plt 
from functions import safe_print, safe_transfer, type_print, cleanse, scrap_web

url, parser = "https://www.sunshineliststats.com/Employer/9/2021/?n=wilfridlaurieruniversity", "html.parser"

data = (scrap_web(url, parser))