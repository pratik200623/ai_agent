# import ollama

# chat_history = []

# while True:
#     user_input = input("You: ")

#     chat_history = [
#     {
#         'role': 'system',
#         'content': 'You are a ruthless AI mentor. Give short, practical, no-BS answers. Focus on helping user get high paying job fast.'
#     }
# ]     

#     response = ollama.chat(
#         model='llama3',
#         messages=chat_history
#     )

#     reply = response['message']['content']
#     print("AI:", reply)

#     chat_history.append({'role': 'assistant', 'content': reply})


import ollama

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error reading file"

chat_history = [
    {
        'role': 'system',
        'content': 'You are a smart AI that can read files and explain them simply.'
    }
]

while True:
    user_input = input("You: ")

    if user_input.startswith("read "):
        filepath = user_input.replace("read ", "")
        file_content = read_file(filepath)

        prompt = f"Explain this file:\n{file_content}"

        chat_history.append({'role': 'user', 'content': prompt})
    else:
        chat_history.append({'role': 'user', 'content': user_input})

    response = ollama.chat(
        model='gemma4:e4b',
        messages=chat_history
    )

    reply = response['message']['content']
    print("AI:", reply)

    chat_history.append({'role': 'assistant', 'content': reply})