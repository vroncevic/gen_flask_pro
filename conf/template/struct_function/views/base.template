# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import render_template
from flask import Blueprint

base_blueprint = Blueprint("base", __name__)

@base_blueprint.route("/")
def home():
	return render_template("base/home.html")

@base_blueprint.route("/contact/")
def contact():
	return render_template("base/contact.html")

@base_blueprint.route("/about/")
def about():
	return render_template("base/about.html")
