学习笔记

## Scrapy VS Requests

Scrapy 体系过于庞杂，对新手不友好，没有 Requests 来得方便直观。

## Selenium

Selenium 每次都要拉起浏览器，速度不理想，而其本身也定位与调试工具。但Selenium胜在能应对各种奇怪的验证码机制，暂时没有其他替代方案。

## 验证码图片识别

课堂介绍的识别方案须依赖系统内置的各种库，改用百度云提供的 OCR 能力来处理更方便和强大，返回文字本身之外还能获得文字坐标和偏转角度。结合 Selenium 可以破解点击文字的验证码。

## MySQL

执行 MySQL 命令时注意以 ；结束语句