# How to use Scrapy (Windows Tutorial)

## Before the initial start:
Go to project folder and execute the following commands in the console:

```
python -m venv venv
```
```
venv\Scripts\activate
```
```
venv\Scripts\python.exe -m pip install --upgrade pip
```
```
pip install scrapy
```
```
scrapy startproject project1
```
```
scrapy genspider spider alibaba.com
```

## Before each start:
Go to project folder and execute the following command to activate venv:
```
venv\Scripts\activate
```
```
cd your_project_name
```
To create a new spider execute:
```
scrapy genspider spider alibaba.com
```
To test and execute your spider:
```
scrapy crawl myspider
```