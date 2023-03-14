from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return f"Video '{yt.title}' downloaded successfully!"
    except Exception as e:
        return f"Error downloading video: {e}"

if __name__ == '__main__':
    app.run(debug=True)
