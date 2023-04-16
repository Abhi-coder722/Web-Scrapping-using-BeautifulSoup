
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

    url = Links.iloc[iteration,0]
        
    #the next line sends a http get request to the specified url which retrieves the HTML content of the webpage in response. 
    res = requests.get(url)

    # res.text retrieves the content of the res object as a string, which is then passed as an argument to BeautifulSoup
    #next line uses BeautifulSoup to parse the html content of the page, creating a soup object
    soup = BeautifulSoup(res.text, 'html.parser')

        
    # check if product_title element exists before accessing it
    #if the product_title is present then extract the value and store in a variable 

    product_title_elem = soup.find('h1', {'class': 'product-title'})
    if product_title_elem:
        product_title = product_title_elem.text.strip()
    else:
        product_title = ''

    # similarly check for size, price, and variation_id elements if the data is extractable then store it otherwise store a blank space in the variable

    # next line looks for first span element that has the class attribute set to product-size within the HTML content of the soup object, and if the size_elem is not None then store it in size variable

    # size checking part-1 where the size has a selection
    select_elem = soup.find('select', {'id': 'data-product-option-0'})
    if select_elem:
        selected_option = select_elem.find('option', {'selected': 'selected'})
        size = selected_option.get('value') if selected_option else " "
    else:
        # size = soup.find('div', {'class': 'product-description'}).find('li', text=lambda t: 'Size' in t).text.strip().split()[-1]
        size=product_title.split(" ")[-1]
        

    findprice=soup.find('div', {'class': 'price--main'})
    price = findprice.find('span', {'class': 'money'}).text.strip() if findprice else " "


    # the next line finds the HTML input element with the attribute name set to variation_id using the BeautifulSoup. This element is then stored in the variable variation_id_elem, and if it isn't None then the get() method is called on the variation_id_elem object with the argument 'value' to extract the value of the value attribute of the input element, and it is stored in the variable variation_id

    variant_elem = soup.find('select', {'name': 'id'})
    if variant_elem :
        variant_option = variant_elem.find('option', selected=True)

        # Extract the value of the 'data-variant-id' attribute
        original_variant_id = variant_option['data-variant-id']
    else: 
        id_elem = soup.find('input', {'name': 'id'})
        original_variant_id = id_elem['value'] if id_elem else " "


    #then store the data of all the variables as list in a single output variable
    output = [url, product_title, size, price, original_variant_id]
    # at last return the extracted values from the web page
    return output









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

