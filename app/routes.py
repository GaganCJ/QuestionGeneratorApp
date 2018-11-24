from flask import jsonify, render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.agq.aqgFunction import AutomaticQuestionGenerator
import json, datetime, os, sys

DATA_FILENAME = "/mnt/c/projects/QGen/app/feedback.json"

@app.route('/')
def check():
    return 'server ready check 1,2,3,...'
@app.route('/index')
def index():
    user = {'username':'Gagan'}
    return render_template('index.html',title='Home',user=user)

@app.route('/admin/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',form=form,title='Admin login')

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