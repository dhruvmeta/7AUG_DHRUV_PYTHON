from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(_name_)

# A list to store photo metadata (simplified for this example)
photos = []

@app.route('/')
def index():
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        photo = request.files['photo']
        if photo:
            filename = photo.filename
            photo.save(os.path.join('static/images', filename))
            photos.append(filename)
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
            