"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")



@app.route("/property", methods=["GET", "POST"])
def property():
    form = PropertyForm()
    if form.validate_on_submit():
        ti = request.form['title']
        no_bed = request.form['bedrooms']
        no_bath = request.form['bathrooms']
        price = request.files['price']
        lo = request.form['location']
        ty = request.form['type_']
        di = request.form['description']
        filename = secure_filename(im.filename)
        im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new = PropertyProfile(ti, no_bed, no_bath, price, lo, ty, di, filename)
        db.session.add(new)
        db.session.commit()
        flash('File Saved', 'success')
        return redirect(url_for('properties'))
    return render_template("property.html", form=form)


@app.route('/properties')
def properties():

    prop=PropertyProfile.query.all()

    if request.method == "POST":

        return render_template("properties.html", users=prop)


@app.route('/property/<propertyid>', methods=['POST', 'GET'])
def prop_spec(propertyid):
    prop = PropertyProfile.query.filter_by(id=propertyid).first()
    return render_template("propertyinfo.html", user=prop)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


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
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
