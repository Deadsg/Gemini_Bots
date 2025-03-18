from google import genai

def chat_with_gemini():
    client = genai.Client(api_key="AIzaSyC64vBJ2a_SKN2Egi7YTmZX17R6zgAH8w0")
    model = "gemini-2.0-flash"
    
    print("Gemini AI Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat.")
            break
        
        response = client.models.generate_content(
    model="gemini-2.0-flash", contents= user_input
)
        print("Gemini:", response.text if response else "(No response)")

if __name__ == "__main__":
    chat_with_gemini()