from flask import Flask, request, jsonify
from flask_cors import CORS

# Create instance of Flask class
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

@app.route("/api/submit-form", methods=["POST"])
def submit_form():
    data = request.json

    pdfUrl = data.get("pdfUrl")
    reportType = data.get("reportType")

    response = {
        "message": "Form submitted successfully",
        "pdfUrl": pdfUrl,
        "reportType": reportType
    }

    return jsonify(response), 200

