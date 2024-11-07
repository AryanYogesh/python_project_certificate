from flask import Flask, request, render_template

from certificate.certificates import cerf

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('certificate_form.html')

@app.route("/generate",methods=['POST'])
def generate():
    name = request.form.get('name')
    course = request.form.get('course')
    all_classes = request.form.get('all_classes')
    all_assignments = request.form.get('all_assignments')

    certificate=cerf(name,course,all_classes,all_assignments)
    dicts=certificate.generate_certificate()
    name=dicts['name']
    course=dicts['course']
    if all_classes=='Yes' and all_assignments=='Yes':
        print("all_classes:", all_classes)
        print("all_assignments:", all_assignments)

        return render_template('generate.html',name=name,course=course)
    
    
    else:
        return render_template('not_completed.html')
    

if __name__=='__main__':
    app.run(debug=True)