#!/usr/bin/env python3
# encoding: utf-8

from flask import Blueprint, render_template, redirect

serarch = Blueprint('search',__name__)

@serarch.route('/')
def index():
    return render_template('index.html')

@serarch.route('/search')
def _serarch():
    
    return '1'
