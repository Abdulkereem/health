from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import random



hom = Blueprint('homepage', __name__)

@hom.route('/')
def home():
    return render_template('./home/index.html')


