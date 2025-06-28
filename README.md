
# 🔐 Interactive Cloud Security Simulation: A Visual Approach to Data Protection

## 📌 Overview

**CyberSentinels** presents an interactive cybersecurity solution focused on **client-side encrypted cloud storage**. This Flask-based web application allows users to securely upload and download files via **Amazon S3**, with optional **AES-128 encryption** using Python's `cryptography.fernet` module.

The project emphasizes user data **confidentiality** and **integrity** by encrypting files locally before transmission. Files can only be decrypted using a secure key generated during upload, empowering users with full control over their sensitive data.

---

## 🚀 Features

- 🔐 **Encrypt/Decrypt Files** using Fernet (AES-128 + HMAC)
- ☁️ **Upload/Download to Amazon S3**
- 🛡️ **Client-Side Key Management** (Keys are never stored)
- 🖥️ **Simple Flask Web Interface**
- ✅ **Tested on multiple file types** (.txt, .docx, etc.)
- 📦 Robust **error handling and input validation**

---

## 🧰 Technologies & Libraries

- **Python 3.10+**
- **Flask** – For web interface
- **cryptography** – For AES-based encryption (Fernet)
- **boto3** – For AWS S3 interaction
- **botocore.config** – For enforcing Signature Version 4
- **AWS S3** – For cloud storage
- **HTML/CSS** – For basic frontend

---

## 🛠️ Project Structure

```
.
├── app.py                  # Flask web server
├── secure_file_s3.py       # Encryption & AWS S3 logic
├── templates/
│   └── index.html          # Main UI
├── uploads/                # Stores uploaded files temporarily
├── decrypted/              # Stores decrypted files temporarily
└── README.md               # You're here!
```

---

## 🔄 How It Works

### 🔼 Uploading a File

1. User selects a file and chooses to encrypt it (optional).
2. If encryption is selected:
   - A secure key is generated.
   - File is encrypted locally using Fernet (AES-128).
3. File (encrypted/plain) is uploaded to AWS S3.
4. User receives:
   - ✅ Upload confirmation
   - 🔑 Encryption key (if encrypted)
   - 📥 Download link

### 🔽 Decrypting a File

1. User provides:
   - Encrypted file name
   - Previously saved key
2. System decrypts the file locally.
3. User gets a link to download the decrypted version.

---

## 🌐 Setup Instructions

### Prerequisites

- Python 3.10+
- AWS S3 bucket configured (`eu-north-1` region recommended)
- Python packages: `boto3`, `flask`, `cryptography`, `python-dotenv`

### Installation

```bash
git https://github.com/mdzaid7817/secure-cloud-vault.git
cd s3-secure-vault
pip install -r requirements.txt
```

### AWS Credentials

Set your AWS credentials in the environment or `.env` file:

```
AWS_ACCESS_KEY_ID=your_key_id
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=eu-north-1
```

---

## 🧪 Testing & Validation

| Feature                    | Status | Description                                             |
|---------------------------|--------|---------------------------------------------------------|
| File Encryption           | ✅     | Works across multiple formats                           |
| File Decryption           | ✅     | Handles valid and invalid key input                     |
| AWS S3 Upload/Download    | ✅     | Region and signature version validated                  |
| Error Handling            | ✅     | User-friendly messages for all common exceptions        |
| Key Security              | ✅     | Keys generated and displayed once (never stored)        |

---

## 📈 Future Enhancements

- 💻 GUI Integration (web-based drag & drop)
- 🔑 Secure Key Vault integration
- 📦 File compression before upload
- 🧪 Unit test coverage


---


