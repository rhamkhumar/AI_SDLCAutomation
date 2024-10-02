import openai

# OpenAI API setup
openai.api_key = 'your-openai-api-key'

def generate_code(requirements):
    prompt = f"Generate a Flask API that {requirements}"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500,
    )
    return response['choices'][0]['text']

# Example usage:
requirements = "handles user authentication and connects to a MySQL database"
generated_code = generate_code(requirements)
print(generated_code)