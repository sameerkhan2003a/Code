from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import openai
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import json
import os

app = Flask(__name__)








@app.route('/', methods=['GET', 'POST'])
def index():


    result = None 
    if request.method == 'POST':
        codingLanguage = request.form['codingLanguage']
        userLevel = request.form['userLevel']
        Chat = request.form['Chat']
        client = openai.OpenAI(api_key=os.environ.get('secret_key'))
     
     
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0,
            max_tokens=1000,
            messages=[
                {"role": "system", "content": f"You are a coding sensei or teacher, you have to help the user of {userLevel} to learn {codingLanguage}, be kind and always try to help the user and do everything possible to help him learn the language."},
               { "role": "user", "content": Chat},
            ]
        )
        result = response.choices[0].message.content
        

    return render_template('index.html', result=result)
