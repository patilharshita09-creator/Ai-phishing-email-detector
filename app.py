from flask import Flask, render_template, request
import joblib
from pathlib import Path

# Load the saved model pipeline
model_path = Path("models/phish_detector.joblib")
if not model_path.exists():
    raise FileNotFoundError("Saved model not found! Run main.py first.")

pipeline = joblib.load(model_path)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    prob = None
    if request.method == "POST":
        email_text = request.form.get("email_text", "")
        if email_text.strip():
            pred = pipeline.predict([email_text])[0]
            prob = pipeline.predict_proba([email_text])[0].max() if hasattr(pipeline, "predict_proba") else None
            result = "Phishing ⚠️" if pred == "phishing" else "Safe ✅"
    return render_template("index.html", result=result, prob=prob)

if __name__ == "__main__":
    app.run(debug=True)
