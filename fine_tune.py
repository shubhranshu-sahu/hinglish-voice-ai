import openai
import os
import sys

# Set your API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def upload_training_file():
    """Upload the dataset.jsonl file to OpenAI"""
    try:
        print("Uploading training file...")
        with open("dataset.jsonl", "rb") as file:
            response = openai.File.create(
                file=file,
                purpose="fine-tune"
            )
        file_id = response.id
        print(f"File uploaded successfully with ID: {file_id}")
        return file_id
    except Exception as e:
        print(f"Error uploading file: {e}")
        sys.exit(1)

def start_fine_tuning(file_id):
    """Start the fine-tuning job using the uploaded file"""
    try:
        print("Starting fine-tuning job...")
        response = openai.FineTuningJob.create(
            training_file=file_id,
            model="gpt-3.5-turbo",
            hyperparameters={
                "n_epochs": 3,
                "learning_rate_multiplier": 0.1
            },
            suffix="hinglish-assistant"
        )
        job_id = response.id
        print(f"Fine-tuning job started with ID: {job_id}")
        print(f"Check status with: openai api fine_tuning.jobs.get -i {job_id}")
        return job_id
    except Exception as e:
        print(f"Error starting fine-tuning: {e}")
        sys.exit(1)

def main():
    if not openai.api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your API key with: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)

    print("Hinglish Voice-AI Fine-Tuning Process")
    print("====================================")

    file_id = upload_training_file()
    job_id = start_fine_tuning(file_id)

    print("\nFine-tuning job submitted successfully!")
    print("Next steps:")
    print("1. Wait for the fine-tuning job to complete.")
    print("2. Once completed, run inference.py to test your model.")

if __name__ == "__main__":
    main()
