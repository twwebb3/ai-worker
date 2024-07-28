import ollama


def chat_with_llama():
    print("Welcome to the Llama 3.1:8B chat interface!")
    print("Type 'exit' to end the conversation.")

    messages = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        messages.append({
            'role': 'user',
            'content': user_input,
        })

        try:
            response = ollama.chat(model='llama3.1:8b', messages=messages)
            ai_response = response['message']['content']
            print(f"\nAI: {ai_response}")

            messages.append({
                'role': 'assistant',
                'content': ai_response,
            })
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    chat_with_llama()