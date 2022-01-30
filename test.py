from flask import Flask, render_template, request, redirect, send_from_directory
import csv
app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/download')
def download():
    return send_from_directory("static", filename="cv.pdf")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
    with open("db.txt", mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email}, {subject}\n{message}')

def write_csv(data):
    with open("/home/alexzatykoo/python_portfo/db.csv", newline='\n', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect("/contact_re.html")
        except:
            'Oops, something went wrong.'
    else:
        return 'sthwentwrong'
    return "done"

