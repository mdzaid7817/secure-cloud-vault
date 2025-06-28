from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from secure_file_s3 import generate_key, encrypt_file, decrypt_file, upload_to_s3

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'
BUCKET_NAME = 'pblcyber'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    encrypt = 'encrypt' in request.form

    if file:
        filename = secure_filename(file.filename)
        local_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(local_path)

        if encrypt:
            key = generate_key()
            encrypted_path = encrypt_file(local_path, key)
            os.remove(local_path)
            final_path = encrypted_path
            encryption_key = key.decode()
        else:
            final_path = local_path
            encryption_key = None

        upload_to_s3(BUCKET_NAME, final_path, os.path.basename(final_path))

        return render_template('index.html',
                               message='✅ File uploaded successfully!',
                               encryption_key=encryption_key,
                               download_link=f'/download/{os.path.basename(final_path)}')
    return render_template('index.html', message='❌ No file uploaded.')

@app.route('/decrypt', methods=['POST'])
def decrypt_from_key():
    filename = request.form['filename']
    key = request.form['key'].encode()

    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)
    decrypted_name = filename.replace('.enc', '_decrypted')
    decrypted_path = os.path.join(DECRYPTED_FOLDER, decrypted_name)

    try:
        decrypt_file(encrypted_path, key, decrypted_path)
        return render_template('index.html',
                               message='✅ File decrypted successfully!',
                               decrypted_link=f'/decrypted/{decrypted_name}')
    except Exception:
        return render_template('index.html',
                               message='❌ Failed to decrypt. Make sure the key and file are correct.')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/decrypted/<filename>')
def download_decrypted_file(filename):
    return send_from_directory(DECRYPTED_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
