# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import Blueprint
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required

from app_server import db, bcrypt
from app_server.views.user_login import UserLogin
from app_server.views.user_register import RegisterForm
from app_server.models.model_user import User

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
	form = UserLogin(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(
				user.password, request.form["password"]):
			login_user(user)
			flash("You are logged in. Welcome!", "success")
			return redirect(url_for("user.members"))
		else:
			flash("Invalid email and/or password.", "danger")
			return render_template('user/login.html', form=form)
	return render_template("user/login.html", title="Please Login", form=form)

@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		user = User(
			fullname=form.fullname.data, username=form.username.data,
			email=form.email.data, password=form.password.data
		)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		flash("Thank you for registering.", "success")
		return redirect(url_for("user.members"))
	return render_template("user/register.html", form=form)

@user_blueprint.route("/logout")
@login_required
def logout():
	logout_user()
	flash("You were logged out. Bye!", "success")
	return redirect(url_for("base.home"))

@user_blueprint.route("/members")
@login_required
def members():
	return render_template("user/members.html")

@user_blueprint.route("/administration")
@login_required
def administration():
	return render_template("user/administration.html")
