import openai
import os
import sys
import json

# Set your API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
# Test prompts in Hinglish to evaluate model performance
test_prompts = [
    "Mujhe ek chai pilao.",
    "Aaj weather kaisa hai Mumbai mein?",
    "Can you help me with my homework?",
    "Kya aap mujhe Python coding sikhane mein help kar sakte ho?",
    "Weekend pe movie dekhne jaana hai, koi recommendations?"
]

def get_model_name():
    """Get the fine-tuned model name from user input"""
    model_name = input("Enter your fine-tuned model name (e.g., ft:gpt-3.5-turbo:personal:hinglish-assistant:xxxx): ")
    if not model_name.startswith("ft:"):
        print("Warning: Model name should typically start with 'ft:'. Are you sure this is correct?")
        confirm = input("Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            sys.exit(0)
    return model_name

def generate_response(model_name, prompt, temperature=0.7):
    """Generate a response using the fine-tuned model"""
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant who communicates fluently in Hinglish (a mix of Hindi and English)."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=150
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error generating response: {e}"

def save_results(results):
    """Save results to a file"""
    with open("inference_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to inference_results.json")

def main():
    if not openai.api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your API key with: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
        
    print("Hinglish Voice-AI Inference Testing")
    print("==================================")
    
    # Get the fine-tuned model name
    model_name = get_model_name()
    
    # Test the model with different prompts
    results = {}
    
    print("\nGenerating responses for test prompts...")
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n[Test {i}]")
        print(f"Prompt: {prompt}")
        
        # Generate response with different temperature settings
        for temp in [0.3, 0.7, 1.0]:
            print(f"\nTemperature: {temp}")
            response = generate_response(model_name, prompt, temperature=temp)
            print(f"Response: {response}")
            
            # Store results
            if prompt not in results:
                results[prompt] = {}
            results[prompt][f"temp_{temp}"] = response
    
    # Save results to file
    save_results(results)
    
    print("\nInference testing completed!")

if __name__ == "__main__":
    main()