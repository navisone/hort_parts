import base64
import psycopg2
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
        self.client = Client('http://192.168.75.104/live/ws/navis_hort?wsdl', transport=transport,
                             settings=settings)

        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="hort_parts",
            user="torsion_prog",
            password="sdr%7ujK")

    def load_products(self):
        products = self.client.service.GetData('products_hort')
        data = base64.b64decode(products)
        file = open('cache/products.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_product_buffer (
            source_id character varying(300),
            source_category character varying(300),
            name_ru character varying(500),
            name_uk character varying(500),
            name_en character varying(500),
            article character varying(300),
            specification character varying(300),
            advanced_description text   );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/products.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_product_buffer',
                          columns=(
                              'source_id', 'source_category', 'name_ru', 'name_uk', 'name_en',
                              'article', 'specification', 'advanced_description'),
                          sep='|')
        self.conn.commit()

        ins_sql = '''INSERT INTO hort_product (source_id, slug)
        SELECT source_id, article FROM hort_product_buffer
        WHERE source_id NOT IN (SELECT source_id FROM hort_product WHERE source_id IS NOT NULL);'''
        cur.execute(ins_sql)
        self.conn.commit()

        del_sql = '''DELETE FROM hort_product
        WHERE source_id NOT IN (SELECT source_id FROM hort_product_buffer);'''
        cur.execute(del_sql)
        self.conn.commit()

        copy_sql = '''UPDATE hort_product p
            SET  
                source_category = b.source_category,         
                name_ru = b.name_ru,
                name_uk = b.name_uk,
                name_en = b.name_en,
                article = b.article,
                slug = b.article,
                specification = b.specification,
                advanced_description = b.advanced_description                                      
            FROM hort_product_buffer b
            WHERE p.source_id = b.source_id;'''
        cur.execute(copy_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_product p
                    SET category_id = c.id
                    FROM hort_category c
                    WHERE p.source_category = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()

    def load_cross(self):
        cross = self.client.service.GetData('cross_hort')
        data = base64.b64decode(cross)
        file = open('cache/cross.csv', 'w', newline='', encoding='utf-8')
        file.write(str(data.decode('utf-8')))
        file.close()

        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_cross_buffer (
            product character varying(300),
            brand character varying(300),                
            article_nr character varying(300) );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/cross.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_cross_buffer',
                          columns=('product', 'brand', 'article_nr'), sep='|')
        self.conn.commit()

        copy_sql = '''UPDATE hort_cross p
            SET
                brand = b.brand,
                article_nr = b.article_nr                      
            FROM hort_cross_buffer b
            WHERE p.product = b.product;'''
        cur.execute(copy_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_cross s
            SET product_id_id = c.id                               
            FROM hort_product c
            WHERE s.product = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()


LoadData = LoadData()
LoadData.load_products()
LoadData.load_cross()

print('Load Data')
