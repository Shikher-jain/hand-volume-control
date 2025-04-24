from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_gesture_control():
    source_type = request.form.get('source')
    if source_type == '2':  # For video file, you will need to add file handling
        video_file = request.form.get('video_path')
        if not video_file:
            return redirect(url_for('home', error="Please select a video file."))
        subprocess.Popen([sys.executable, "Advance-Python-SJ/Open CV/Advance/Projects/Gesture/HandVolumeGesture.py", video_file])
    else:
        subprocess.Popen([sys.executable, "Advance-Python-SJ/Open CV/Advance/Projects/Gesture/HandVolumeGesture.py", source_type])
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)


