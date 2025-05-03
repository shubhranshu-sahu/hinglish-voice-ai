import openai
import os

# Configure API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Upload dataset file
with open("dataset.jsonl", "rb") as file:
    response = openai.File.create(
        file=file,
        purpose="fine-tune"
    )
    file_id = response.id
    print(f"File uploaded with ID: {file_id}")