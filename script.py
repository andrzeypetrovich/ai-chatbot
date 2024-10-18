import openai

# Open AI API Key
openai.api_key = 'ZmxhZ3tub3RfYW5fYWN0dWFsX2tleV9zb3JyeV9idXRfaGV5X3lvdV9nZXRfdGhlX2ZsYWd9'

# Generate a response from the GPT model
def generate_gpt_response(prompt):
    try:

        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150,
            n=1,                        
            stop=None,
            temperature=0.7
        )
        
        # Get the response text
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    gpt_response = generate_gpt_response(user_prompt)
    
    if gpt_response:
        print("\nGPT-4 Response:")
        print(gpt_response)
