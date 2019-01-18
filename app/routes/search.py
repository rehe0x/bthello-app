#!/usr/bin/env python3
# encoding: utf-8

from flask import Blueprint, render_template, redirect,request
from common.database import ElasticsClient

ElasticsClients = ElasticsClient('bt_metadata','doc') 

serarch = Blueprint('search',__name__)

@serarch.route('/')
def index():
    return render_template('index.html')

@serarch.route('/search')
def _serarch():
    value = request.args.get('value')
    return str(ElasticsClients.Get_Data_By_Body(value))