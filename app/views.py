"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, time
from app import app
from flask import Flask, render_template, request, redirect, url_for
from app import db
from app.models import Profile
from .forms import ProfileForm
from werkzeug import secure_filename


###
# Routing for your application.
###
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'POST':
        # return "found post"
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        sex = request.form['sex']
        userid = 6000
        # return "so far so good"
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image = filename
        profile = Profile(userid,firstname,lastname,age,sex)
        # return "so far so good"
        db.session.add(profile)
        db.session.commit()
        return "{} {}".format(firstname, lastname)
    return render_template('profile.html', date=timeinfo(), form=form)
def timeinfo():
    return (time.strftime("%a, %d %b %Y"))

@app.route('/profile/int:<userid>', methods=['GET', 'POST'])
def viewprofile():
    return "val"

@app.route('/profiles')
def profiles():
    return "val"




###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8888)
