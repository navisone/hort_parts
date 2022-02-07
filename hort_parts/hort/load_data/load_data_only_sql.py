import base64
import psycopg2
from zeep import Client, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport


class LoadData:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="hort_parts",
            user="torsion_prog",
            password="sdr%7ujK")

    def load_products(self):
        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_product_buffer (
            source_id character varying(300),
            source_commercial character varying(300),
            source_category character varying(300),
            name_ru character varying(500),
            name_uk character varying(500),
            name_en character varying(500),
            name_de character varying(500),
            article character varying(300),
            specification character varying(300),
            advanced_description_ru text,
            advanced_description_uk text,  
            advanced_description_en text,
            advanced_description_de text  );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/products.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_product_buffer',
                          columns=(
                              'source_id', 'source_commercial', 'source_category', 'name_ru', 'name_uk', 'name_en',
                              'name_de', 'article', 'specification', 'advanced_description_ru',
                              'advanced_description_uk', 'advanced_description_en',  'advanced_description_de'),
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
                source_commercial = b.source_commercial, 
                source_category = b.source_category,         
                name_ru = b.name_ru,
                name_uk = b.name_uk,
                name_en = b.name_en,
                name_de = b.name_de,
                article = b.article,
                slug = b.article,
                specification = b.specification,
                advanced_description_ru = b.advanced_description_ru,
                advanced_description_uk = b.advanced_description_uk,
                advanced_description_en = b.advanced_description_en,
                advanced_description_de = b.advanced_description_de                                      
            FROM hort_product_buffer b
            WHERE p.source_id = b.source_id;'''
        cur.execute(copy_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_product p
                    SET category_id = c.id
                    FROM hort_category c
                    WHERE p.source_category = c.source_category;'''
        cur.execute(upd_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_product p
                    SET commercial_id = c.id
                    FROM hort_commercial c
                    WHERE p.source_commercial = c.source_commercial;'''
        cur.execute(upd_sql)
        self.conn.commit()

    def load_cross(self):
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

        trnc_sql = '''TRUNCATE TABLE hort_cross;'''
        cur.execute(trnc_sql)
        self.conn.commit()

        ins_sql = '''INSERT INTO hort_cross (product, brand, article_nr)
                SELECT product, brand, article_nr FROM hort_cross_buffer
                WHERE product NOT IN (SELECT product FROM hort_cross WHERE product IS NOT NULL);'''
        cur.execute(ins_sql)
        self.conn.commit()

        del_sql = '''DELETE FROM hort_cross
                WHERE product NOT IN (SELECT product FROM hort_cross_buffer);'''
        cur.execute(del_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_cross s
            SET product_id_id = c.id                               
            FROM hort_product c
            WHERE s.product = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()

    def load_description(self):
        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_description_buffer (
            product character varying(300),
            property character varying(300), 
            value text );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/description.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_description_buffer',
                          columns=('product', 'property', 'value'), sep='|')
        self.conn.commit()

        trnc_sql = '''TRUNCATE TABLE hort_description;'''
        cur.execute(trnc_sql)
        self.conn.commit()

        ins_sql = '''INSERT INTO hort_description (product, property, value)
                        SELECT product, property, value FROM hort_description_buffer
                        WHERE product NOT IN (SELECT product FROM hort_description WHERE product IS NOT NULL);'''
        cur.execute(ins_sql)
        self.conn.commit()

        del_sql = '''DELETE FROM hort_description
                        WHERE product NOT IN (SELECT product FROM hort_description_buffer);'''
        cur.execute(del_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_description d
            SET product_id_id = c.id                               
            FROM hort_product c
            WHERE d.product = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()

    def load_applicability(self):
        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_applicability_buffer (
            product character varying(300),
            vehicle character varying(300),
            modification character varying(300), 
            engine character varying(300), 
            year character varying(300) );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/applicability.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_applicability_buffer',
                          columns=('product', 'vehicle', 'modification', 'engine', 'year'), sep='|')
        self.conn.commit()

        trnc_sql = '''TRUNCATE TABLE hort_applicability;'''
        cur.execute(trnc_sql)
        self.conn.commit()

        ins_sql = '''INSERT INTO hort_applicability (product, vehicle, modification, engine, year)
                        SELECT product, vehicle, modification, engine, year FROM hort_applicability_buffer
                        WHERE product NOT IN (SELECT product FROM hort_applicability WHERE product IS NOT NULL);'''
        cur.execute(ins_sql)
        self.conn.commit()

        del_sql = '''DELETE FROM hort_applicability
                        WHERE product NOT IN (SELECT product FROM hort_applicability_buffer);'''
        cur.execute(del_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_applicability a
            SET product_id_id = c.id                               
            FROM hort_product c
            WHERE a.product = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()

    def load_product_images(self):
        cur = self.conn.cursor()

        t_sql = '''CREATE TEMP TABLE hort_productimage_buffer (
                    source_product character varying(300),
                    image_url character varying(300) );'''
        cur.execute(t_sql)
        self.conn.commit()

        with open('cache/product_images.csv', 'r', encoding='utf-8') as file:
            cur.copy_from(file, 'hort_productimage_buffer',
                          columns=('source_product', 'image_url'), sep='|')
        self.conn.commit()

        trnc_sql = '''TRUNCATE TABLE hort_productimage;'''
        cur.execute(trnc_sql)
        self.conn.commit()

        ins_sql = '''INSERT INTO hort_productimage (source_product, image_url)
                        SELECT source_product, image_url FROM hort_productimage_buffer
                        WHERE source_product NOT IN (SELECT source_product FROM hort_productimage 
                        WHERE source_product IS NOT NULL);'''
        cur.execute(ins_sql)
        self.conn.commit()

        del_sql = '''DELETE FROM hort_productimage
                        WHERE source_product NOT IN (SELECT source_product FROM hort_productimage_buffer);'''
        cur.execute(del_sql)
        self.conn.commit()

        upd_sql = '''UPDATE hort_productimage a
                    SET product_id = c.id                               
                    FROM hort_product c
                    WHERE a.source_product = c.source_id;'''
        cur.execute(upd_sql)
        self.conn.commit()


LoadData = LoadData()

LoadData.load_products()
print('Load Products')

LoadData.load_cross()
print('Load Cross')

LoadData.load_description()
print('Load Description')

LoadData.load_applicability()
print('Load Applicability')

LoadData.load_product_images()
print('Load Images')
