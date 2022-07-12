import requests
import webbrowser

url_begin = "https://www.bestbuy.com/site/searchpage.jsp?st="

programDict = {
    "3070": "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
    "3070ti": "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789",
    "3080": "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-gaming-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6471960.p?skuId=6471960",
    "disableButton": "c-button c-button-disabled c-button-lg c-button-block add-to-cart-button",
}


def getStatus(card):
    source = requests.get(
        programDict[card],
        headers={"User-Agent": "Mozilla/5.0"}
    ).text
    if programDict["disableButton"] not in source:
        print(card+" is available\n\n")
        webbrowser.open(programDict[card])
    else:
        print(card+" is unavailable\n\n")


getStatus("3070")
getStatus("3070ti")
getStatus("3080")
