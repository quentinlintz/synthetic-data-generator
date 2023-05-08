import openai
import csv
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROMPT = (
    "Generate 10 random movie reviews in CSV format, each followed by a comma and a label indicating if it's a positive (1) or negative (0) review. "
    "Please do not include any numbering or double quotes at the beginning of the lines. "
    "Format each line exactly like this (without double quotes): "
    "review text,1 or review text,0\n"
    "Example:\n"
    "The acting was great, but the plot was a bit slow.,0\n"
    "This movie was amazing! I loved everything about it.,1\n"
    "The special effects were impressive, but the story was weak.,0\n"
    "I thought the pacing was perfect and the ending was satisfying.,1\n"
)
NUM_OF_CALLS = 1

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_text():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def save_to_csv(data, file_name):
    with open(file_name, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = []

    try:
        for i in range(NUM_OF_CALLS):
            response = generate_text()
            lines = response.split("\n")
            for line in lines:
                if line:
                    try:
                        comment, label = line.rsplit(",", 1)
                        label_int = int(label.strip())
                        data.append((comment.strip(), label_int))
                    except ValueError:
                        print(f"Skipping line due to invalid format: '{line}'")
            print(f"Completed API call {i + 1} of {NUM_OF_CALLS}")


    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Saving partial data to the CSV file...")

    finally:
        save_to_csv(data, "output.csv")
        print("Data saved to 'output.csv'.")
