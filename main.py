# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, send_from_directory
from download_scripts import DownloadYTVideo, get_all_video_resolutions, return_yt_by_itag, VideoToMp3
from flask_cors import CORS
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

	
@app.route('/robots.txt', methods=['GET'])
@app.route('/sitemap.xml', methods=['GET'])
def render_sitemap():
	return send_from_directory(app.static_folder, request.path[1:])
	
	

@app.route('/', methods=['POST', 'GET'])
def home():
	if(request.method == "GET"):
		try:
			return render_template('index.html')
		except Exception as e:
			print("Error in rendering template", e)
	elif(request.method == "POST"):
		video_url=request.form['video_url']
		print("VIDEO URL", video_url)
		return DownloadYTVideo(video_url)

 
@app.route('/get_resolutions', methods=['POST'])
def find_video_resolutions():
	if(request.method == 'POST'):
		video_url=request.json['video_url']
		return get_all_video_resolutions(video_url)


@app.route('/downloadyoutubevideo', methods=['POST', 'GET'])
# ‘/’ URL is bound with hello_world() function.
def download_yt_video():
	try:
		print(request.json['url'])
		yturl=request.json["url"]
		# return { "download_url": DownloadYTVideo(yturl)}
		return DownloadYTVideo(yturl)
	except Exception as er:
		print("Error", er)

@app.route('/downloadbyitag', methods=['POST'])
def download_yt_vide_by_itag():
	if(request.method == "POST"):
		url = request.form['url']
		itag = request.form['itag']
		try:
			return return_yt_by_itag(url, itag)
		except Exception as e:
			print(e)


@app.route('/policy.html', methods=['GET'])
def return_policy():
	return render_template('policy.html')





# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(host="0.0.0.0", port=5000, debug=True)
