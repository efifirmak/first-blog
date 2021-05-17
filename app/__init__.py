from flask import Flask
app = Flask(__name__) #adına app dediğim şey bir flask

from app import views
from app import admin_views

