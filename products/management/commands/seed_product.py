import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from products.models import Product

numbers = ["03000000", "01000000", "02000000", "10000000", "08000000", "07000000"]


def get_item(number):
    number = 10000000
    items = []
    item = {}

    result = requests.get(
        f"http://minishop.gmarket.co.kr/riotstore/List?Category={number}&Page=0&PageSize=120"
    )
    soup = BeautifulSoup(result.text, "html.parser")
    item_box = soup.find("div", {"id": "ItemList"})
    item_list = item_box.find_all("li", {"class": "normal"})
    for item in item_list:
        item_image = item.find("p", {"class": "prd_img"}).find("img")["data-original"]
        item_name = item.find("p", {"class": "prd_name"}).text.strip(" \n")
        item_price = (
            item.find("p", {"class": "prd_price"}).text.strip(" \n 원").replace(",", "")
        )
        item = {
            "name": item_name,
            "price": (item_price),
            "image": item_image,
        }
        items.append(item)
    return items


class Command(BaseCommand):

    help = "Create Product"

    def handle(self, *args, **kwargs):

        for number in numbers:
            items = get_item(number)
            for i in items:
                Product.objects.create(
                    name=i.get("name"),
                    image=i.get("image"),
                    price=i.get("price"),
                )

        return self.stdout.write(self.style.SUCCESS("Product Created!"))