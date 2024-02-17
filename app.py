from flask import Flask, render_template, jsonify, request
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
import config
import openai
import aiapi

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/community')
def community():
    return 'Hello, World!'

@app.route('/chatbot')
def chatbot():
    return 'Hello, World!'