from flask import Flask, request, jsonify
from flask_cors import CORS
from run_scraper import extract_EOD_data

# Create instance of Flask class
app = Flask(__name__)
CORS(app)

@app.route("/test-hello")
def test_hello():
    return '<h1>Test</h1>'

@app.route("/api/submit-form", methods=["POST"])
def submit_form():
    data = request.json

    pdfUrl = data.get("pdfUrl")
    reportType = data.get("reportType")

    try:
        extract_EOD_data(pdfUrl, report_type=reportType)
        response = {
            "message": "Form submitted successfully",
            "pdfUrl": pdfUrl,
            "reportType": reportType
        }
        return jsonify(response, 200)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


