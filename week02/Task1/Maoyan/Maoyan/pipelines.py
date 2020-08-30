# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_categories = item['movie_categories']
        release_date = item['release_date']
        incert_values = (movie_name, movie_categories,release_date)
        sql = 'insert into test.maoyan values (%s,%s,%s)'
        try:
            self.cursor.execute(sql,incert_values)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        # output = f'{Movie_Name},{Movie_Categories},{Release_Date}\n'
        # with open('./Movie_Top10.csv','a+',encoding='utf-8') as article:
        #     article.write(output)
        return item
    

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '12345678',
            charset = 'utf8',
        )
        self.cursor = self.conn.cursor()
        return
    
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        return
