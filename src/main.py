import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
import json
from typing import List

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: List[str]

def extract_event_info(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Using GPT-3.5-turbo for wider compatibility
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts event information. Please provide the extracted information in JSON format with the following fields: name, date, and participants."},
            {"role": "user", "content": text},
        ]
    )

    # Extract JSON from API response
    response_text = completion.choices[0].message.content
    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON. Raw response: {response_text}")
        return None

    # Parse JSON into CalendarEvent model
    try:
        event = CalendarEvent(**response_json)
        return event
    except ValueError as e:
        print(f"Failed to create CalendarEvent. Error: {e}")
        return None

if __name__ == "__main__":
    input_text = "Alice and Bob are going to a science fair on Friday."
    event = extract_event_info(input_text)
    if event:
        print(f"Extracted event: {event}")
    else:
        print("Failed to extract event information.")
        