from fastapi import FastAPI, Request
from pydantic import BaseModel
from firewall import intercept_output
from typing import Dict
import numpy as np
def to_serializable(obj):
    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_serializable(v) for v in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    return obj
app = FastAPI()

class OutputRequest(BaseModel):
    output: str

@app.post("/intercept/")
async def intercept(req: OutputRequest):
    filtered_output, report = intercept_output(req.output)
    # Ensure all values in report are JSON serializable
    return {
        "filtered_output": filtered_output,
        "report": to_serializable(report)
    }
