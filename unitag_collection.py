from bs4 import BeautifulSoup
import numpy as np, requests, selenium, sys, matplotlib.pyplot as plt 
from functions import safe_print, safe_transfer, type_print, cleanse, scrap_web
from laurier_base import data

base = "https://www.sunshineliststats.com/Employer/9/2021/?n="
name_scrap = "https://www.sunshineliststats.com/EmployerByName?page=1&name=university&provinceid=9&year=2022"
parser = "html.parser"
soup = BeautifulSoup(safe_transfer(requests.get(name_scrap).text), parser)

university_list = [cleanse(((td.text).strip().split()), {"\n":1, "\r":1}) for td in soup.find("tbody")]

def list_seperate(seperation_index, )