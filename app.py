from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

path = "C:\dev\Projects\Youtube Video Downloader\downloads"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html", url = url)
    return render_template("home.html")

@app.route("/download", methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        file = video.download(path)
        return send_file(file, as_attachment=True)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)