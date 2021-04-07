from flask import Flask, render_template, redirect, url_for, request
import os
from flask_cors import CORS
app = Flask(__name__)
import flask
import os
from flask import jsonify
os.chdir('./darknet')
flag = 1
CORS(app)


def get_predection():
	print("In fn")
	os.system("./darknet detector test data/image_data.data cfg/yolov3_custom2.cfg yolov3_custom2_last.weights data.jpg -thresh 0.15")


def create_dict():
  
    filename = 'data.txt'

    dict1 = {}
    list = []

    count = 0
    # creating dictionary
    with open(filename) as fh:
        for line in fh:
            dict2 = {}
            # reads each line and trims of extra the spaces

            # and gives only the valid words
            # description = line.strip().split(None, 1)
            points = line.split(',')

            dict2['z'] = int(points[0])
            dict2['x'] = int(points[1])
            dict2['rotation'] = int(points[2])
            dict2['scale'] = int(points[3].split('\n')[0])
            list.append(dict2)
        dict1['points'] = list
        return dict1

@app.route('/getpoints')
def getpoints():
  while flag is 0:
     print("Waiting")
  return create_dict()
  


@app.route('/', methods=['GET','POST'])
def upload():
	if request.method =="POST":
		flag = 0
		image = request.files["image"]
# 		image1 = request.files["image"]
		filename = image.filename 
		ext = filename.split('.')[1]
		image.save('data.' + ext)
		get_predection()
		flag = 1
		
	
	return render_template('Home.html')
	

if __name__=='__main__':
	#app.run(host='0.0.0.0', port=8080)
	app.run()
