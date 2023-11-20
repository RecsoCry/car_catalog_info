import requests
import xml.etree.ElementTree as ET
from core.models import Carmake, Model


def update_car_catalog():
    # response = requests.get('https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml')
    tree = ET.parse(r'C:\Users\User\Desktop\Django\car_catalog_info\core\cars.xml')
    root = tree.getroot()

    Carmake.objects.all().delete()
    Model.objects.all().delete()

    for name in root:
        car = name.items()
        one_name = car[0][1]
        car_name = Carmake.objects.create(name=one_name)
        for model in name:
            brand = model.items()
            if len(brand)> 1:
                one_brand = brand[0][1]
                brand_name = Model.objects.create(carmake=car_name, name=one_brand)





