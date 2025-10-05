import joblib
from pathlib import Path

# Load the saved pipeline
model_path = Path("models/phish_detector.joblib")
if not model_path.exists():
    raise FileNotFoundError("Saved model not found! Run main.py first.")

pipeline = joblib.load(model_path)

# Test with new email examples
examples = [
    "Please update your payment details immediately here: http://fake-link.example",
    "Team meeting at 10 AM tomorrow, join link in calendar",
    "Your account has been suspended. Click here to verify: http://phish.example"
]

# Make predictions
preds = pipeline.predict(examples)
probs = pipeline.predict_proba(examples) if hasattr(pipeline, "predict_proba") else None

# Print results
for i, txt in enumerate(examples):
    label = preds[i]
    prob = (probs[i].max() if probs is not None else None)
    print("Email:", txt)
    print("Prediction:", label, f"Confidence: {prob:.2f}" if prob is not None else "")
    print("-" * 60)
    
