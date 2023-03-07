import pandas as pd, selenium, requests, numpy as np, matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from functions import safe_print, safe_transfer, type_print

url = "https://www.sunshineliststats.com/Employer/9/2021/?n=wilfridlaurieruniversity"
html = safe_transfer(requests.get(url).text)

