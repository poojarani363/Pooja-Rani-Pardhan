from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LQ7bwcKPgPRYeYz87NTbOpJOy3bRB5YE0H_TTxfix-uA")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print("Gemini:", response.text)g