#python3
#seach imgur for images and download first 20 associated images

import requests, bs4, os

def main():
    try:
        response = requests.get('https://www.flickr.com/search/?text=the%20expanse')
        response.raise_for_status()
    except requests.HTTPError:
        print("Error has occurred opening the website.")

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    imgElem = soup.select('yui_3_16_0_1_1671036276604_1162 img')
    print(imgElem)

main()