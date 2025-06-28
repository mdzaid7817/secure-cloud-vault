import os
from cryptography.fernet import Fernet
import os

os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''
os.environ['AWS_DEFAULT_REGION'] = ''  # e.g., 'ap-south-1'

import boto3
from botocore.config import Config
from dotenv import load_dotenv

# Load credentials from .env file           
load_dotenv()

AWS_ACCESS_KEY = os.getenv('')
AWS_SECRET_KEY = os.getenv('')

UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    encrypted_path = file_path + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted)
    return encrypted_path

def decrypt_file(encrypted_path, key, output_path):
    fernet = Fernet(key)
    with open(encrypted_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(output_path, 'wb') as f:
        f.write(decrypted)
    return output_path

def upload_to_s3(bucket_name, file_path, s3_key):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name='eu-north-1',
        config=Config(signature_version='s3v4')
    )
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded to S3: s3://{bucket_name}/{s3_key}")
