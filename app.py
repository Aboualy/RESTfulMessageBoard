# coding: utf8
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from flask import Flask, render_template, url_for, flash, redirect, jsonify
from msgform import MessageForm
from database import Database
from dictionary import Dictionary
from flask_cors import cross_origin
from flask_accept import accept_fallback
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


# route to the main page
@app.route("/")
@app.route("/home")
def home():
    messages = Database.give_dict()
    return render_template('home.html', messages=messages)

# route to the about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/message", methods=['GET', 'POST'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        data = Dictionary(form.title.data, form.content.data, form.sender.data, form.url.data).store()
        Database(data).add_to_dict()
        flash(f'Message sent form {form.sender.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('message.html', title='Create Message', form=form)



#The service supports two response versions within the same endpoint.
#The caller is able to define which response version he can handle.
# json format
@app.route('/message-service', methods=['GET', 'POST'])
@accept_fallback
@cross_origin()
def show_messages():
    x = Database().dict_to_json()
    return jsonify(items=x)

# xml format
@show_messages.support('application/xml')
def show_messages_xml():
    xml_format = Database().dict_to_xml()
    return xml_format


if __name__ == '__main__':
    app.run(debug=True)