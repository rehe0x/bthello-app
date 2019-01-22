#!/usr/bin/env python3
# encoding: utf-8

from flask import Blueprint, render_template, redirect,request
from common.database import ElasticsClients

serarch = Blueprint('search',__name__)

@serarch.route('/')
def index():
    return render_template('index.html')

@serarch.route('/search')
def _serarch():
    value = request.args.get('value')
    data = ElasticsClients.Get_Data_By_Body(value)
    return render_template('list.html',metadataList=data)

@serarch.route('/search/<infohash>')
def _serarch_id(infohash):
    data = ElasticsClients.Get_Data_Id(infohash)
    return render_template('details.html',metadata=data)
