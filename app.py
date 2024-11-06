from flask import Flask, Request,render_template

from certificate.certificates import cerf

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('certificate_form.html')

@app.route("/certificate_form.html",methods='POST')
def generate():
    name = Request.form.get('name')
    course = Request.form.get('course')
    all_classes = Request.form.get('all_classes')
    all_assignments = Request.form.get('all_assignments')

    certificate=cerf(name,course,all_classes,all_assignments)
    dicts=certificate.generate_certificate()
    name=dicts['name']
    course=dicts['course']
    if all_classes=='yes' and all_assignments=='yes':
        return render_template('generate.html',name=name,course=course)
    
    else:
        return render_template('not_completed.html')