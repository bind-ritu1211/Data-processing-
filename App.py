from flask import Flask,request, render_template,redirect,url_for
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = os.getcwd()+ "/"
CANCEL_FOLDER = os.getcwd()+ "/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/index')
def upload_file():
   return render_template('submit_file.html')


@app.route('/submit', methods=['GET','POST'])
def submit_file():
    if request.method == 'POST':
        files = request.files['file'] if request.files.get('file') else None
        if files:
            filename = files.filename
            files.save(os.path.join(app.config['UPLOAD_FOLDER'], files.filename))
            return redirect(url_for('.submit_file'))
    return "file successfully submitted"    

@app.route('/cancel', methods=['GET','POST'])
def cancel_file():
    if request.method == 'POST':
        files = request.files['file'] if request.files.get('file') else None
        if files:
            filename = files.filename
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], files.filename))
            return redirect(url_for('.submit_file'))
    return "file successfully cancel"    



if __name__ == "__main__":
    app.run(debug=True)
