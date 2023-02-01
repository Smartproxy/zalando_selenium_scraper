from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extension import proxies
from bs4 import BeautifulSoup
import json

username = 'SPusername'
password = 'SPpassword'
endpoint = 'gate.smartproxy.com'
port = '7000'
website = 'https://www.zalando.co.uk/shoes/'

chrome_options = webdriver.ChromeOptions()

proxies_extension = proxies(username, password, endpoint, port)

chrome_options.add_extension(proxies_extension)
chrome_options.add_argument("--headless=new")


chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
chrome.get(website)

html = chrome.page_source

def main():
    
    soup = BeautifulSoup(html, "html.parser")

    # Select div containing data points

    div_tags = soup.find_all('div', class_='DT5BTM w8MdNG cYylcv _1FGXgy _75qWlu iOzucJ JT3_zV vut4p9')

    # Extract data points

    data = []
    for div_tag in div_tags:
        
        brand_tags = div_tag.find_all('h3', class_="SZKKsK u-6V88 FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2")
        brand_text = [brand_tag.text for brand_tag in brand_tags]

        model_tags = div_tag.find_all('h3', class_="_0Qm8W1 u-6V88 FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2")
        model_text = [model_tag.text for model_tag in model_tags]
    
        pricing_tags = div_tag.find_all('p', class_="_0Qm8W1 u-6V88 FxZV-M pVrzNP")
        pricing_text = [pricing_tag.text for pricing_tag in pricing_tags]

        pricing2_tags = div_tag.find_all('p', class_="_0Qm8W1 u-6V88 FxZV-M weHhRC ZiDB59")
        pricing2_text = [pricing2_tag.text for pricing2_tag in pricing2_tags]

        pricing3_tags = div_tag.find_all('p', class_="_0Qm8W1 u-6V88 dgII7d TQ5FLB mx_ksa")
        pricing3_text = [pricing3_tag.text for pricing3_tag in pricing3_tags]
    
        category_tags = div_tag.find_all('span', class_="_0Qm8W1 VnVJx_ dgII7d DJxzzA FCIprz")
        category_text = [category_tag.text for category_tag in category_tags]

        url_tags = div_tag.find_all('a', class_="_LM JT3_zV CKDt_l CKDt_l LyRfpJ")
        url_text = [url_tag['href'] for url_tag in url_tags]

        image_tags = div_tag.find_all('img', class_="_0Qm8W1 u-6V88 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy")
        image_text = [image_tag['src'] for image_tag in image_tags]
    
        element = {
            "Brand": brand_text,
            "Model": model_text,
            "CurrentPrice": pricing_text,
            "RegularPrice": pricing2_text,
            "DiscountPrice": pricing3_text,
            "Category": category_text,
            "ProductURL": url_text,
            "ImageURL": image_text
        }
        data.append(element)

    # Save data to JSON

    with open('data.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
