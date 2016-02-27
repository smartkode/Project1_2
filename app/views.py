"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, time, json
from app import app
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate():
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                return os.getcwd()
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) **create bucket on AWS
                # firstname = request.form['firstname']
                # lastname = request.form['lastname']
                # age = request.form['age']
                # sex = request.form['sex']
                # userid = 62007000 
                # check = db.session.execute('SELECT COUNT(id) FROM profile')
                # for r in check:
                #     result = r[0]
                # if result > 0:
                #     last_user = db.session.query(Profile).get(result)
                #     if last_user.userid >= userid:
                #         userid = last_user.userid + 1
                # image = filename
                # profile = Profile(userid,firstname,lastname,age,sex,image)
                # db.session.add(profile)
                # db.session.commit()
                # flash("Profile created successfully!")
                # # return "{} {} {}".format(image, app.config['UPLOAD_FOLDER'], os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # return render_template('profile.html', form=form)
        else:
            flash("You had an error!")
    return render_template('profile.html', form=form)
def timeinfo():
    return (time.strftime("%a, %d %b %Y"))


# from werkzeug.routing import Map, Rule, RuleTemplate, RuleFactory

# url_map = Map([
#     Rule('/profile', endpoint='#select_language'),
#     Subdomain('<string(length=2):lang_code>', [
#         Rule('/', endpoint='index'),
#         Rule('/about', endpoint='about'),
#         Rule('/help', endpoint='help')
#     ])
# ])
# @app.route('/profile/<string:userid>')
@app.route('/profile/<int:userid>', methods=['GET', 'POST'])
def viewprofile(userid):
    profile = db.session.query(Profile).get(userid)
    username = ((profile.firstname + profile.lastname).lower()).replace(" ", "")
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        prof = dict([("userid", profile.userid), ("username", username), ("image", profile.image), ("age", profile.age), ("sex", profile.sex)])
        return json.dumps(prof, sort_keys=False, indent=4)
    
    return render_template('profile_view.html', date=timeinfo(), profile=profile, username=username)
    # if type(userid) == str:
        
    #     userid = int(userid)
    #     profile = db.session.query(Profile).get(userid)
    #     username = ((profile.firstname + profile.lastname).lower()).replace(" ", "")
    #     return render_template('profile_view.html', date=timeinfo(), profile=profile, username=username)
    # if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
    #     return "works"
    # return render_template('profile_view.html', date=timeinfo(), profile=profile, username=username)
    

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    profiles = db.session.query(Profile).all()
    prof_list = []
    for p in profiles:
        username = ((p.firstname + p.lastname).lower()).replace(" ", "")
        prof_list.append(dict([("username", username), ("userid", p.userid)]))
    prof_dict = dict([("users",prof_list)])
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        return json.dumps(prof_dict, sort_keys=False, indent=4)
    return render_template('list_profiles.html', profiles=profiles)

@app.route('/test', methods=['GET'])    
def test():
    return render_template('test.html')
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/
# get vars
# request.args.get("username")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
