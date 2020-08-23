# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        Movie_Name = item['Movie_Name']
        Movie_Categories = item['Movie_Categories']
        Release_Date = item['Release_Date']
        output = f'{Movie_Name},{Movie_Categories},{Release_Date}\n'
        with open('./Movie_Top10.csv','a+',encoding='utf-8') as article:
            article.write(output)
        return item
