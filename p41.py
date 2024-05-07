from flask import Flask, request, send_file
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/upload', methods = ["POST"])
def upload_file():
    try:
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return 'File Uploaded Successfully'
    except Exception as e:
        return str(e), 500
    
@app.route('/download/<filename>', methods = ['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File Not Found', 404
    
if __name__=="__main__":
    app.run(debug=True)
