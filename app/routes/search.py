#!/usr/bin/env python3
# encoding: utf-8

from flask import Blueprint, render_template, redirect,request
from common.database import ElasticsClients

serarch = Blueprint('search',__name__)

@serarch.route('/')
def index():
    return render_template('index.html')

@serarch.route('/search/<val>')
def _serarch(val):
    value = val.split("-")
    #value = request.args.get('value')
    v = value[0]
    p = value[1]
    page = int(p.split(".")[0])
    #分页计算
    pageSize = 15
    pageNo = pageSize * (page -1)
    _searched = ElasticsClients.Get_Data_By_Body(v,pageNo,pageSize)
    data = _searched['hits']
    total = _searched['total']

    count = int((total - 1) / pageSize + 1)
    #最大10页
    count =10 if count > 10 else count
    return render_template('list.html',metadataList=data,count=range(1,count+1))

@serarch.route('/search/details-<infohash>')
def _serarch_id(infohash):
    data = ElasticsClients.Get_Data_Id(infohash[:-5])
    return render_template('details.html',metadata=data)

@serarch.route('/link')
def link():
    return render_template('link.html')
