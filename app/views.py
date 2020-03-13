import datetime
import os

from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import ProfileForm
from app.models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/profile',methods=['GET','POST'])
def profile():
    form = ProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        gender = form.gender.data
        location = form.location.data
        biography = form.biography.data
        profile_pic = form.profile_pic.data
        filename = secure_filename(profile_pic.filename)
        profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        user = User(firstname,lastname,gender,email,location,biography,filename)
        db.session.add(user)
        db.session.commit()
        flash('Profile successfully added','success')
        return redirect(url_for('profiles'))
    flash_errors(form)
    return render_template('profile.html',form=form)

@app.route('/profile/<userid>')
def uprofile(userid):
    userid = User.query.get(userid)
    curdate = format_date_joined('2018-03-12')
    profile_pic = get_image(userid.profile_pic_id)
    return render_template('userprofile.html' ,user=userid, curdate=curdate, profile_pic=profile_pic)

@app.route('/profiles')
def profiles():
    users = User.query.all()
    return render_template('profiles.html',users=users)
    

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form,field).label.text,
                error
            ),'danger')


def format_date_joined(date):
    year,month,day = map(int,date.split('-'))
    date_joined = datetime.date(year,month,day)
    return ("Joined on " + date_joined.strftime("%B %d, %Y"))

def get_image(filename):
    rootdir = os.getcwd()
    for subdir, dirs,files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            try:
                if file == filename:
                    return file
            except:
                raise(OSError)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page. """
    return render_template('404.html'),404
