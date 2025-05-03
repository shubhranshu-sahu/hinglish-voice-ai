# Hinglish Voice-AI Fine-Tuning Mini-Project

This project demonstrates how to fine-tune an OpenAI language model for code-switched Hinglish dialogue in voice AI applications.

## Project Structure

- `dataset.jsonl`: The training dataset in JSONL format
- `fine_tune.py`: Script to upload dataset and start fine-tuning
- `inference.py`: Script to test the fine-tuned model
- `README.md`: Project documentation (this file)

## Setup Instructions

### Prerequisites

1. Python 3.6+
2. OpenAI Python package (`pip install openai`)
3. An OpenAI API key with access to fine-tuning

### Setting up API Key

Set your OpenAI API key as an environment variable:

```bash
# For Linux/macOS
export OPENAI_API_KEY="your-api-key-here"

# For Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# For Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"