
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

'''Function to extract different informations of the product'''
def do_task(iteration):











'''Use the function above to crawl for all links'''
for iteration in range(len(Links)):
    print('on the {} link (total: {})'.format(iteration + 1, len(Links)))   
    output = do_task(iteration)
    result.loc[len(result)] = output
    

'''Exporting result to target folder'''
end_time = datetime.now()
timestr = time.strftime("%d.%m.%Y-%H%M%S")
print('Duration: {}'.format(end_time - start_time))
name = "Webshop_"+timestr+"_"+candidates
result.to_excel(r'{}.xlsx'.format(name), index=False)  

