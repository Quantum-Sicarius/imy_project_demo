import requests
from bs4 import BeautifulSoup
import re
import json
import uuid

pages = [
    {"name": "motherboard", "url": "https://www.evetech.co.za/components/cheap-intel-amd-based-motherboards-19.aspx"},
    {"name": "harddrive", "url": "https://www.evetech.co.za/components/hard-drives-124.aspx"},
    {"name": "gpu", "url": "https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx"},
    {"name": "cpu", "url": "https://www.evetech.co.za/components/buy-cpu-processors-online-164.aspx"},
    {"name": "powersupply", "url": "https://www.evetech.co.za/PC-Components/corsair-power-supply-78.aspx"}
]

all_products = []

for page in pages:
    page_result = requests.get(page["url"])
    soup = BeautifulSoup(page_result.content, 'html.parser')

    #ctl00_ContentPlaceHolder1_Component_List1_dl_products "ctl00_ContentPlaceHolder1_Component_List_V2_IDs1_dl_products"
    table = soup.find('table', {'id': re.compile('ctl00_ContentPlaceHolder1_Component_List.*_products')}) 
    rows = table.findAll('tr')

    scraped = 0
    products = []

    print("rows: " + str(len(rows)))

    for row in rows:
        #print("======================")
        # Product name
        if not row.find('h2'):
            continue

        name = row.find('h2').find('span').getText().strip()
        #print(name)

        # Price
        if not row.find('div', {"class": "price"}):
            continue

        price = row.find('div', {"class": "price"}).getText().replace("Including VAT", "").replace("R", "").replace(",","").strip()
        #print(price)

        #image
        image = "https://www.evetech.co.za/" + row.find('img')['src'].replace("../ResizeImage_Final.aspx?Image=~/", "").replace("&width=200&height=190", "").strip()

        # Explore description
        #more_info = row.find('a', {"class": "moreInfoBtn"}, href=True)['href'].replace("../", "")
        #print(more_info)
        #info = requests.get("https://www.evetech.co.za/" + more_info)

        #info_soup = BeautifulSoup(info.content, 'html.parser')
        #info_table = info_soup.find(lambda tag: tag.name=='table' and tag.has_attr('style') and tag['style']=="width: 100%" and tag.has_attr('cellspacing') and tag['cellspacing']=="0") 
        #info_rows = info_table.findAll(lambda tag: tag.name=='tr')
        #info_result = ""

        #for info_row in info_rows:
        #    data = info_row.findAll('p')
        #    for d in data:
        #        info_result += d.getText().strip().rstrip('\r\n')

        #details = info_result.rstrip('\r\n')
        #print({"name": name, "price":price, "details":details})
        #print("======================")

        tags = []
        tags.append(page["name"])

        product = {"id": str(uuid.uuid4()), "name": name, "price":price, "image":image , "tags":tags}

        products.append(product)
        all_products.append(product)
        
        print(product)

        print ("Scraped: " + str(scraped) + " prudcts!")
        scraped += 1

    file_name = page["name"] + "s.json"
    file = open(file_name,"w") 
    file.write(json.dumps(products)) 
    file.close() 

file = open("products.json","w") 
file.write(json.dumps(all_products)) 
file.close() 