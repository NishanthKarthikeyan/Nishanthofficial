from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Certificates Page
@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

# Achievements Page
@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

# Route for images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.path.join('static', 'images'), filename)

if __name__ == '__main__':
    app.run(debug=True)
