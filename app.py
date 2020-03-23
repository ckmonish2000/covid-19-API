from flask import Flask,render_template,request
from scraper import scrape


x=scrape()
print(x)