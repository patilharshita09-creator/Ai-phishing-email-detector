import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import warnings

warnings.filterwarnings("ignore")

print("Hello, AI Phishing Detector!")

# Load CSV
df = pd.read_csv("data/emails.csv")

print("\nLoaded rows:", len(df))
print(df.head())

# Preprocessing
df = df.dropna(subset=['text','label']).reset_index(drop=True)
df['text_clean'] = df['text'].astype(str).str.lower()

# Split data
X = df['text_clean']
y = df['label']
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
except Exception:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Vectorize text
vec = TfidfVectorizer(ngram_range=(1,2), min_df=1)
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vec, y_train)

# Evaluate
y_pred = clf.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {acc*100:.2f}%")
print("\nClassification report:")
print(classification_report(y_test, y_pred))

# Predict new examples
examples = [
    "Please update your payment details immediately here: http://fake-link.example",
    "Team meeting at 10 AM tomorrow, join link in calendar"
]
ex_vec = vec.transform([e.lower() for e in examples])
preds = clf.predict(ex_vec)
print("\nExample predictions:")
for e, p in zip(examples, preds):
    print(f"  -> {p}  |  {e}")

import joblib
from sklearn.pipeline import Pipeline

# Create a pipeline with your vectorizer and classifier
pipeline = Pipeline([
    ("tfidf", vec),
    ("clf", clf)
])

# Save the pipeline to the models folder
joblib.dump(pipeline, "models/phish_detector.joblib")

print("\nModel and vectorizer saved successfully in 'models/' folder!")

