from detoxify import Detoxify
import spacy
import json
import os
import numpy as np
from datetime import datetime

# Load the English language model for NER
nlp = spacy.load("en_core_web_sm")

# Function to check toxicity using Detoxify
def check_toxicity(text):
    result = Detoxify('original').predict(text)
    return result

# Function to redact named entities (PII)
def redact_pii(text):
    doc = nlp(text)
    redacted = []
    for token in doc:
        if token.ent_type_ in ["PERSON", "ORG", "GPE", "DATE", "CARDINAL"]:
            redacted.append("[REDACTED]")
        else:
            redacted.append(token.text)
    return " ".join(redacted)

# Helper function to convert non-serializable NumPy types
def convert_types(obj):
    if isinstance(obj, np.generic):
        return obj.item()
    elif isinstance(obj, dict):
        return {k: convert_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_types(v) for v in obj]
    return obj

# Function to log the intercepted outputs
def log_output(original, corrected, report):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().isoformat()

    # Convert numpy types to JSON-serializable types
    clean_report = convert_types(report)

    log = {
        "timestamp": timestamp,
        "original_output": original,
        "filtered_output": corrected,
        "report": clean_report
    }

    with open("logs/intercepts_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")

# Function to process and filter the AI output
def intercept_output(text):
    toxicity = check_toxicity(text)
    needs_redact = any(score > 0.5 for score in toxicity.values())

    report = {
        "toxicity_scores": toxicity,
        "action_taken": ""
    }

    if needs_redact:
        filtered = redact_pii(text)
        report["action_taken"] = "Redacted due to toxicity"
    else:
        filtered = text
        report["action_taken"] = "Safe"

    log_output(text, filtered, report)
    return filtered, report
