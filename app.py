from flask import Flask, render_template, request

app = Flask(__name__)

# app.py
@app.route("/submit_certificate_application", methods=["POST"])

def handle_application():
    # Access form data
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    certificate_type = request.form.get("certificate_type")
    reason = request.form.get("reason")

    # Process the data (e.g., validate, store in database)
    # ... (code for processing data) ...

    # Generate a response (e.g., confirmation message)
    return "Certificate application submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
