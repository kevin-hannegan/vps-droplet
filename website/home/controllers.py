from flask import render_template, Blueprint

home_blueprint = Blueprint('home',__name__,url_prefix='/')

@home_blueprint.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')
