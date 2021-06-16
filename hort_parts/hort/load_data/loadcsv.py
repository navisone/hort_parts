import base64
import psycopg2
from zeep import Client, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport


class LoadDataProducts:
    def __init__(self):
        session = Session()
        session.auth = HTTPBasicAuth('Robot', 'Robot')
        transport = Transport(session=session, timeout=600)
        settings = Settings(xml_huge_tree=True)
        self.client = Client('http://192.168.75.115:8005/live/ws/hort?wsdl', transport=transport, settings=settings)

    def load_products(self):
        products = self.client.service.GetData('products')
        data = base64.b64decode(products)
        file = open('cache/products.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_cross(self):
        cross = self.client.service.GetData('cross')
        data = base64.b64decode(cross)
        file = open('cache/cross.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_description(self):
        description = self.client.service.GetData('description')
        data = base64.b64decode(description)
        file = open('cache/description.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_applicability(self):
        applicability = self.client.service.GetData('applicability')
        data = base64.b64decode(applicability)
        file = open('cache/applicability.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_product_manufacturer_model(self):
        deficit = self.client.service.GetData('product_manufacturer_model')
        data = base64.b64decode(deficit)
        file = open('cache/product_manufacturer_model.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()


class LoadDataTecdoc:
    def __init__(self):
        session = Session()
        session.auth = HTTPBasicAuth('Robot', 'Robot')
        transport = Transport(session=session, timeout=600)
        settings = Settings(xml_huge_tree=True)
        self.client = Client('http://192.168.75.115:8005/live/ws/decort?wsdl', transport=transport, settings=settings)

    def load_tecdoc_manufacturer(self):
        tecdoc_manufacturer = self.client.service.GetData('tecdoc_manufacturer')
        data = base64.b64decode(tecdoc_manufacturer)
        file = open('cache/tecdoc_manufacturer.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_tecdoc_manufacturer_model(self):
        tecdoc_manufacturer_model = self.client.service.GetData('tecdoc_manufacturer_model')
        data = base64.b64decode(tecdoc_manufacturer_model)
        file = open('cache/tecdoc_manufacturer_model.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()


LoadDataProducts = LoadDataProducts()
LoadDataProducts.load_products()
LoadDataProducts.load_cross()
LoadDataProducts.load_description()
LoadDataProducts.load_applicability()
LoadDataProducts.load_product_manufacturer_model()
print('Load Data Products')

# LoadDataTecdoc = LoadDataTecdoc()
# LoadDataTecdoc.load_tecdoc_manufacturer()
# LoadDataTecdoc.load_tecdoc_manufacturer_model()
# print('Load Data Tecdoc')

