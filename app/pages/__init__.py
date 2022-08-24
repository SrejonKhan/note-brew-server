from flask import Blueprint, render_template

page_blueprint = Blueprint('page_v1', __name__, url_prefix='/', template_folder="templates")

@page_blueprint.route('/')
def index():
    return render_template("index.html")
