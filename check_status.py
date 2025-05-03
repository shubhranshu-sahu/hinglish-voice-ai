import openai
import os
import time

# Configure API key
openai.api_key = os.getenv("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")

# Check fine-tuning job status
def check_status(job_id):
    status = openai.FineTune.retrieve(id=job_id)
    return status

# Replace with your actual job ID from fine_tune.py output
job_id = "ft-your-job-id"
status = check_status(job_id)
print(f"Status: {status.status}")