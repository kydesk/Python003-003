学习笔记

# Python 基础语法

在练习过程中回顾之前学习的基础语法

# 爬虫库

## Requests 库

头部信息只带 header 和 cookie 均被反爬，须从浏览器复制全部头部信息

## BeautifulSoup

### find_all() 和 find()

- find_all() 返回一个列表，列表元素包含所有找到的标签
- find() 返回一个标签

### .contents

使用 .contents 定位元素时注意 \n 也被视为一个元素

## Scrapy

- 使用 scrapy crawl spidername 命令启动蜘蛛，而不是运营 .py 文件
- 执行 scrapy crawl spidername 命令时，终端应该在蜘蛛的项目目录下
- Xpath 直接复制自源代码的路径容易出错，需自己按实际情况重新编写