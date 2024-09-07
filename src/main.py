import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
import json
from typing import List, Optional, Dict
import re

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Contact(BaseModel):
    phone: Optional[str] = None
    # 必要に応じて他の連絡先情報フィールドを追加できます

class DeliveryLocation(BaseModel):
    postal_code: str
    address: str
    contact: Optional[Contact] = None

class OrderInfo(BaseModel):
    delivery_date: str
    item: str
    quantity: int
    delivery_location: DeliveryLocation

def extract_order_info(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts order information. Please provide the extracted information in JSON format with the following fields: delivery_date, item, quantity, and delivery_location (which should include postal_code, address, and optionally contact with a phone field)."},
            {"role": "user", "content": text},
        ]
    )

    # Extract JSON from API response
    response_text = completion.choices[0].message.content
    
    # Remove code block markers if present
    json_str = re.search(r'```(?:json)?(.*?)```', response_text, re.DOTALL)
    if json_str:
        response_text = json_str.group(1).strip()
    
    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON. Raw response: {response_text}")
        return None

    # Parse JSON into OrderInfo model
    try:
        order = OrderInfo(**response_json)
        return order
    except ValueError as e:
        print(f"Failed to create OrderInfo. Error: {e}")
        return None

if __name__ == "__main__":
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to example.txt in the parent directory's inputText folder
    input_file_path = os.path.join(os.path.dirname(current_dir), "inputText", "example.txt")

    # Read input from example.txt file
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {input_file_path}")
        exit(1)
    except IOError:
        print(f"Error: Could not read file at {input_file_path}")
        exit(1)

    order = extract_order_info(input_text)
    if order:
        print(f"Extracted order information:")
        print(f"納品希望日: {order.delivery_date}")
        print(f"アイテム: {order.item}")
        print(f"数量: {order.quantity}")
        print(f"納品場所:")
        print(f"  郵便番号: {order.delivery_location.postal_code}")
        print(f"  住所: {order.delivery_location.address}")
        if order.delivery_location.contact:
            if order.delivery_location.contact.phone:
                print(f"  電話番号: {order.delivery_location.contact.phone}")
    else:
        print("Failed to extract order information.")
        