from flask import render_template, Blueprint, request, make_response
import logging, json
from models import contact_email
from home import app
home_blueprint = Blueprint('home',__name__,url_prefix='/')

@app.route('/', methods=['GET','POST'])
def home():
    logging.info("Loading home page...")
    return render_template('index.html')

@app.route('/message/', methods=['POST'])
def message():
    logging.info("Received POST request to send email")
    logging.info(request.data)
    logging.info(json.loads(request.data))
    sentmail = contact_email(json.loads(request.data))
    if sentmail:
        return make_response("Message Sent!")
    else:
        return make_response("Message Send Failuire!"), 500
