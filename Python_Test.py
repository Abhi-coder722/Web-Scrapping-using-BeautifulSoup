
'''Importing modules needed in the code, If some of them missing you can install it in on your environment if you want to modify the code'''
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
'''Feel Free to use other method or modules as you see fit'''

start_time = datetime.now()
'''Declaration of the columns that will be exported in excel file'''
columns_list = ["url","product_title","size","price","variation_id"]
result = pd.DataFrame(columns = columns_list)

'''Define the path to your input file because I will be importing links from an excel file you can also direct enter a link instead of importing files'''
Links = pd.read_excel(r'input_file.xlsx')


candidates = input("Please input your name here : ")

