from flask import jsonify, render_template, flash, redirect, url_for, request
from app import app
from app.agq.aqgFunction import AutomaticQuestionGenerator
import json, datetime, os, sys

DATA_FILENAME = "/mnt/c/projects/QGen/app/feedback.json"

@app.route('/')
def check():
    return 'server ready check 1,2,3,...'
@app.route('/index')
def index():
    with open(DATA_FILENAME,mode="r+",encoding="utf-8") as read_file:
        dummy = json.load(read_file)
    return render_template("index.html", users = dummy, name="Admin", title = "QGen")

@app.route('/login')
def login():
    return render_template('login.html',title='Admin login')

@app.route('/about')
def about():
    return render_template('about.html',title='QGen')

@app.route('/demo')
def demo():
    return render_template('demo.html',title='QGen')

@app.route('/agq')
def generateOutput():
    para = request.args.get('para',0,type=str)
    aqg = AutomaticQuestionGenerator()
    questionList = aqg.aqgParse(para)
    res = aqg.display(questionList)
    return jsonify(res)

@app.route('/submit_data')
def savejson():
    data = []
    try:
        with open(DATA_FILENAME, mode="r+",encoding="utf-8") as read_file:
            data = json.load(read_file)
        for user in data:
            global user_id
            user_id = user["feedback_id"]
        f_user_id = int(user_id) + 1
        y = {"feedback_id":f_user_id,
        "name":request.args.get('name',0,type=str),
        "email":request.args.get('email',0,type=str),
        "data_in_para":request.args.get('para',0,type=str),
        "ques_gen":request.args.get('ques',0,type=str),
        "feedback":request.args.get('feeds',0,type=str),
        "session":datetime.datetime.now().strftime('%c')}
        with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
            json.dump([], f)
        with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
            data.append(y)
            json.dump(data,f)
    except:
        y = {"feedback_id":1,
        "name":request.args.get('name',0,type=str),
        "email":request.args.get('email',0,type=str),
        "data_in_para":request.args.get('para',0,type=str),
        "ques_gen":request.args.get('ques',0,type=str),
        "feedback":request.args.get('feeds',0,type=str),
        "session":datetime.datetime.now().strftime('%c')}
        with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
            json.dump([], f)
        with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
            data.append(y)
            json.dump(data,f)
    return 'OK'

@app.route('/del_data')
def del_html():
    open_d = []
    op = request.args.get('ids', 0, type=int)
    with open(DATA_FILENAME, mode="r+",encoding="utf-8") as read_file:
        open_d = json.load(read_file)
    for i in range(len(open_d)):
        if open_d[i]["feedback_id"] == op:
            open_d.pop(i)
            break
    with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
        json.dump([], f)
    with open(DATA_FILENAME,mode="w+",encoding="utf-8") as f:
        json.dump(open_d,f)
    return redirect(url_for('index'))