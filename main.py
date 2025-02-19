from flask import Flask, request, render_template, send_file
import base64

def encode_base64(content):
    return base64.b64encode(content.encode("utf-8")).decode("ascii")

def decode_base64(content):
    return base64.b64decode(content).decode("utf-8")

def encode_utf16(content):
    return content.encode("utf-16").hex()

def decode_utf16(content):
    return bytes.fromhex(content).decode("utf-16")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        encoding_type = request.form["encoding"]
        action = request.form["action"]
        
        if file:
            content = file.read().decode("utf-8")
            
            if encoding_type == "base64":
                processed_content = encode_base64(content) if action == "encode" else decode_base64(content)
            elif encoding_type == "utf-16":
                processed_content = encode_utf16(content) if action == "encode" else decode_utf16(content)
            else:
                return "Invalid encoding type", 400
            
            output_file = "output.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(processed_content)
            
            return send_file(output_file, as_attachment=True)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
