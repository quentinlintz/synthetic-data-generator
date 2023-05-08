# Synthetic Labeled Data Generator

This Python script generates synthetic labeled data using the OpenAI API. You can customize the script to generate different types of text data and their associated labels. The generated dataset is saved in a CSV file, which can be used to train NLP models.

## Environment

- Python 3.11

## Getting Started

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip
    pip install -r requirements.txt

## Setup

1. Clone the repository or download the `synthetic_data_generator.py` script.

2. Sign up for an OpenAI API key, if you don't have one. Visit <https://beta.openai.com/signup/> to sign up.

3. Replace the placeholder `your_openai_api_key_here` in the `synthetic_data_generator.py` script with your actual OpenAI API key.

## Usage

1. Open a terminal and navigate to the directory containing the `synthetic_data_generator.py` script.

2. Run the script using the following command:

   ```bash
   python main.py
   ```

3. The script will generate synthetic text data along with their labels and save them to a CSV file named synthetic_data.csv in the same directory.
