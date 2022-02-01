import base64
from zeep import Client, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport


class LoadData:
    def __init__(self):
        session = Session()
        session.auth = HTTPBasicAuth('Robot', 'Robot')
        transport = Transport(session=session, timeout=600)
        settings = Settings(xml_huge_tree=True)
        self.client = Client('http://192.168.75.45/live/ws/navis_hort?wsdl',
                             transport=transport, settings=settings)

    def load_products(self):
        products = self.client.service.GetData('products_hort')
        data = base64.b64decode(products)
        file = open('cache/products.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_cross(self):
        cross = self.client.service.GetData('cross_hort')
        data = base64.b64decode(cross)
        file = open('cache/cross.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_description(self):
        description = self.client.service.GetData('description_hort')
        data = base64.b64decode(description)
        file = open('cache/description.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_applicability(self):
        applicability = self.client.service.GetData('applicability_hort')
        data = base64.b64decode(applicability)
        file = open('cache/applicability.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_product_manufacturer_model(self):
        deficit = self.client.service.GetData('product_manufacturer_model_hort')
        data = base64.b64decode(deficit)
        file = open('cache/product_manufacturer_model.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_product_images(self):
        deficit = self.client.service.GetData('product_images_hort')
        data = base64.b64decode(deficit)
        file = open('cache/product_images.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

    def load_category_product(self):
        deficit = self.client.service.GetData('category_product_hort')
        data = base64.b64decode(deficit)
        file = open('cache/category_product.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()


LoadData = LoadData()
LoadData.load_products()
LoadData.load_cross()
LoadData.load_description()
LoadData.load_applicability()
LoadData.load_product_manufacturer_model()
LoadData.load_product_images()
LoadData.load_category_product()

print('Load Data Products')
