from flask import Flask
from flask import render_template  # to open html files
import os
from flask import url_for, send_from_directory # to open any files like pictures
from flask import request # to send data to server from web page
from flask import redirect # to open page by clicking 
import csv # to write in excel file
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def launch_html_page(page_name = None):
	return render_template(page_name)

def add_to_database_csv(data):
	with open('database.csv', mode='a', newline='') as file:
		csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([data["email"] , data["subject"], data["message"]])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		add_to_database_csv(data)
    		return redirect('thankyou.html')
    	except:
    		return 'did not write to database'
    else:
    	return 'something went wrong!'