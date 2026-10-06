import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key was not found.")
    exit()

client = OpenAI(api_key=api_key)

# Hotel information
hotel_information = """
You are a friendly and professional customer service agent for Royal Haven Hotel.

Use only the hotel information below to answer customer questions.

Royal Haven Hotel Information:

Check-in: 3:00 PM
Check-out: 11:00 AM
Breakfast: 6:30 AM to 10:00 AM
Wi-Fi: Free for all hotel guests
Parking: Free for hotel guests
Pets: Pets are not allowed, except service animals
Swimming Pool: 7:00 AM to 9:00 PM
Gym: Open 24 hours
Cancellation: Free cancellation up to 24 hours before check-in
Room Service: 6:00 AM to 11:00 PM

Instructions:
Be polite, friendly, and professional.
Keep answers short and easy to understand.
Do not invent prices, policies, services, or room availability.
If information is not provided above, tell the customer to contact the front desk.
Use the conversation history to understand follow-up questions.
"""

# Simple heading
print("Royal Haven Hotel Customer Service")
print()
print("Hello! How can I help you today?")
print("Type 'exit' to end the chat.")
print()

# Store conversation history
conversation = []

while True:
    user_question = input("You: ")

    if user_question.lower().strip() == "exit":
        print("Agent: Thank you for contacting Royal Haven Hotel. Have a great day!")
        break

    try:
        conversation.append({
            "role": "user",
            "content": user_question
        })

        response = client.responses.create(
            model="gpt-6-luna",
            instructions=hotel_information,
            input=conversation
        )

        agent_answer = response.output_text

        conversation.append({
            "role": "assistant",
            "content": agent_answer
        })

        print("Agent:", agent_answer)
        print()

    except Exception as e:
        print("Agent: Sorry, I am unable to respond right now.")
        print("Error:", e)