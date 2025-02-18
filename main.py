from flask import Flask, request, render_template, send_file
import base64

def encode_text(content, encoding_type):
    if encoding_type == "base64":
        return base64.b64encode(content.encode()).decode()
    elif encoding_type == "utf-16":
        return content.encode("utf-16").decode("latin1")
    return None

def decode_text(content, encoding_type):
    if encoding_type == "base64":
        return base64.b64decode(content.encode()).decode()
    elif encoding_type == "utf-16":
        return content.encode("latin1").decode("utf-16")
    return None

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        encoding_type = request.form["encoding"]
        action = request.form["action"]
        
        if file:
            content = file.read().decode("utf-8")
            
            if action == "encode":
                processed_content = encode_text(content, encoding_type)
            else:
                processed_content = decode_text(content, encoding_type)
            
            output_file = "output.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(processed_content)
            
            return send_file(output_file, as_attachment=True)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
