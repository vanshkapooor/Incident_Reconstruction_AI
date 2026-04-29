import ollama

def call_llm(prompt, model="phi3"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert forensic investigator AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']