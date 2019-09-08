from flask import Flask, render_template, request, redirect, flash
from config import ACCESS_KEY, SECRET_KEY
import boto3
from werkzeug import secure_filename

app = Flask(__name__)

app.secret_key = 'FEIUFFHEUFN8I8L8O8T8P8A8L8FBEB3489Y328?><>>DUE'
bucket_name = "YOUR S3 BUCKET NAME"

s3 = boto3.client(
   "s3",
   aws_access_key_id=ACCESS_KEY,
   aws_secret_access_key=SECRET_KEY
)
bucket_resource = s3


@app.route("/", methods=['post', 'get'])
def index():
    if request.method == "POST":

        try:
            data = request.files['file']
            filename = ''
            if data:
                filename = secure_filename(data.filename)
                data.save(filename)
                bucket_resource.upload_file(
                    Bucket=bucket_name,
                    Filename=filename,
                    Key=filename
                )
                flash('Upload successfully Done')
                return redirect('/')
        except Exception as e:
            return (str(e))
    return render_template("index.html")

#error page handle
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

