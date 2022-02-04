import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs

def generate_sound(inp):
    if inp == 1:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    elif inp == 2:
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)


def check_fk_price(url, amount):

    request = requests.get(url)
    soup = bs(request.content,'html.parser')

    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    offers = soup.find("div",{"class":"XUp0WS"}).get_text()
    prince_int = int(''.join(re.findall(r'\d+', price)))
    print(product_name + " is at " + price+"\n OFFERS \n"+offers+"\n")
    if prince_int < amount:
        print("Book Quickly")
        generate_sound(1)
    else:
        print("No Slots found")



def main():
    URL = "https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn63hn-a/p/itmde54f026889ce?pid=COMFXEKMGNHZYFH9&lid=LSTCOMFXEKMGNHZYFH9EOWT4E&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3ACOMFXEKMXWUMGPHW%3Bl%3ALSTCOMFXEKMXWUMGPHW40HAM7%3Bpt%3App%3Buid%3Aac5c25a2-8584-11ec-92a7-99ef6486e033%3B.COMFXEKMGNHZYFH9&ppt=pp&ppn=pp&ssid=npbt1mddr40000001622911909542&otracker=pp_reco_Similar%2BProducts_1_35.productCard.PMU_HORIZONTAL_APPLE%2B2020%2BMacbook%2BAir%2BM1%2B-%2B%25288%2BGB%252F256%2BGB%2BSSD%252FMac%2BOS%2BBig%2BSur%2529%2BMGN63HN%252FA_COMFXEKMGNHZYFH9_productRecommendation%2Fsimilar_0&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_1_NA_view-all&cid=COMFXEKMGNHZYFH9"
    while True:
        check_fk_price(URL, 90000)
        time.sleep(3600)

if __name__ == "__main__":
    main()
