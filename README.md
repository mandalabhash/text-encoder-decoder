# Text Encoder/Decoder Web App

## Overview
The **Text Encoder/Decoder Web App** is a simple Flask-based web application that allows users to encode and decode text files using **Base64** and **UTF-16** encoding formats. The application provides a user-friendly interface to upload a text file and select an encoding or decoding operation.

## Features
- Encode text files to **Base64** or **UTF-16**.
- Decode text files from **Base64** or **UTF-16**.
- Simple and intuitive web interface.
- Supports test file upload and download.

## Technologies Used
- **Python (Flask)** - Backend API
- **HTML, CSS, JavaScript** - Frontend UI
- **Base64, UTF-16 Encoding/Decoding** - Core functionality

## Installation and Setup
### Prerequisites
- Python 3.x installed
- pip (Python package manager)

### Steps to Install and Run
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/mandalabhash/text-encoder-decoder.git
   cd text-encoder-decoder
   ```

2. **Install Dependencies:**
   ```sh
   pip install flask
   ```

3. **Run the Application:**
   ```sh
   python main.py
   ```

4. **Access the Web App:**
   Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. **Upload a text file** containing the content you want to encode or decode.
2. **Select Encoding Type**: Choose between Base64 or UTF-16.
3. **Select Action**: Choose whether to encode or decode the file.
4. **Click Process**: The processed file will be downloaded automatically.

## Folder Structure
```
text-encoder-decoder/
│── templates/
│   └── index.html  # Frontend template
│── main.py         # Flask backend
│── README.md       # Project documentation
```

