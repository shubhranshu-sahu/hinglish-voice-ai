# Hinglish Voice-AI Fine-Tuning Mini-Project

This project demonstrates how to fine-tune an OpenAI language model for code-switched Hinglish dialogue in voice AI applications.

## Project Structure

* `dataset.jsonl`: The training dataset in JSONL format
* `fine_tune.py`: Script to upload dataset and start fine-tuning
* `inference.py`: Script to test the fine-tuned model
* `README.md`: Project documentation (this file)

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
```

## How to Run the Project

### Step 1: Clone and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hardik1712/hinglish-voice-ai.git
   cd hinglish-voice-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install openai
   ```

3. **Verify your API key is set:**
   ```bash
   # On Linux/macOS
   echo $OPENAI_API_KEY
   
   # On Windows (Command Prompt)
   echo %OPENAI_API_KEY%
   
   # On Windows (PowerShell)
   echo $env:OPENAI_API_KEY
   ```

### Step 2: Prepare Your Dataset

1. **Check your dataset format:**
   - Ensure `dataset.jsonl` exists in the project root
   - Each line should contain a valid JSON object with training examples
   - Example format:
   ```json
   {"messages": [{"role": "system", "content": "You are a helpful assistant that speaks Hinglish."}, {"role": "user", "content": "Kya haal hai?"}, {"role": "assistant", "content": "Main theek hun, thanks for asking!"}]}
   ```

2. **Validate your dataset (optional):**
   ```bash
   python -c "import json; [json.loads(line) for line in open('dataset.jsonl')]"
   ```

### Step 3: Fine-tune the Model

1. **Run the fine-tuning script:**
   ```bash
   python fine_tune.py
   ```

2. **What this script does:**
   - Uploads your `dataset.jsonl` to OpenAI
   - Creates a fine-tuning job
   - Displays the job ID and status
   - Monitors the training progress

3. **Expected output:**
   ```
   Uploading dataset...
   Dataset uploaded successfully. File ID: file-abc123
   Creating fine-tuning job...
   Fine-tuning job created. Job ID: ftjob-xyz789
   Job Status: validating_files
   Job Status: running
   ...
   Job Status: succeeded
   Fine-tuned model: ft:gpt-3.5-turbo:your-org:model-name:abc123
   ```

4. **Important notes:**
   - Fine-tuning can take several minutes to hours depending on dataset size
   - Save the fine-tuned model ID that appears after completion
   - You'll be charged for the fine-tuning process based on OpenAI's pricing

### Step 4: Test Your Fine-tuned Model

1. **Update the model ID:**
   - Open `inference.py`
   - Replace the model ID with your fine-tuned model ID from Step 3

2. **Run the inference script:**
   ```bash
   python inference.py
   ```

3. **Test with Hinglish inputs:**
   - The script will prompt you to enter text
   - Try examples like:
     - "Yaar, I'm so confused about this problem"
     - "Kya kar rahe ho? What are you doing?"
     - "Mujhe help chahiye with my homework"

4. **Example interaction:**
   ```
   Enter your message (or 'quit' to exit): Yaar, I'm feeling stressed
   Response: Arre yaar, tension mat lo! Stress is normal, but you should try some relaxation techniques. Kya specific problem hai?
   ```

## Running the Complete Workflow

Here's the complete sequence to run the entire project:

```bash
# 1. Setup
git clone https://github.com/hardik1712/hinglish-voice-ai.git
cd hinglish-voice-ai
pip install openai
export OPENAI_API_KEY="your-api-key-here"  # or use set/$ env for Windows

# 2. Fine-tune the model
python fine_tune.py

# 3. Note down the fine-tuned model ID from the output

# 4. Test the model
python inference.py
```

## Troubleshooting

### Common Issues and Solutions:

1. **"Authentication Error"**
   - Check if your API key is correctly set
   - Verify the API key has fine-tuning permissions
   - Try: `python -c "import openai; print(openai.api_key)"`

2. **"File not found: dataset.jsonl"**
   - Ensure `dataset.jsonl` exists in the project directory
   - Check file permissions and format

3. **"Invalid JSON in dataset"**
   - Validate your JSONL format
   - Each line must be a complete, valid JSON object
   - No trailing commas or syntax errors

4. **"Quota exceeded" or "Rate limit"**
   - Check your OpenAI account usage and billing
   - Wait before retrying
   - Consider upgrading your OpenAI plan

5. **Fine-tuning job fails**
   - Check the dataset size (minimum 10 examples recommended)
   - Ensure proper message format in dataset
   - Review OpenAI's fine-tuning guidelines

### Getting Help:

- Check OpenAI's fine-tuning documentation
- Review error messages carefully
- Test with a smaller dataset first
- Monitor your OpenAI usage dashboard

## Expected Costs

Fine-tuning costs depend on:
- Base model used (gpt-3.5-turbo recommended for cost-effectiveness)
- Dataset size (number of tokens)
- Current OpenAI pricing

Check [OpenAI's pricing page](https://openai.com/pricing) for current rates.

## Next Steps

After successfully running the project:
1. Experiment with different dataset sizes
2. Try various Hinglish conversation patterns
3. Integrate the fine-tuned model into voice AI applications
4. Monitor model performance and iterate
