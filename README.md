# Synthetic Data Generator

This Python script uses OpenAI's `gpt-3.5-turbo` language model to generate synthetic data for NLP training. The script prompts the language model to generate random comments, and then labels those comments as either a suggestion or not. The resulting data is saved to a CSV file.

## Environment

- Python 3.11

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```

## Setup

2. Sign up for an OpenAI API key, if you don't have one. Visit <https://beta.openai.com/signup/> to sign up.

3. Copy the `.env.example` and rename it to `.env`, put your OpenAI API key in there

## Usage

1. Open a terminal and navigate to the directory containing the `main.py` script.

2. Modify the global variables as necessary.

   a. `PROMPT` should be changed based on what you want to generate

   b. `NUM_OF_CALLS` determines how many times the OpenAI API gets called

3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The script will generate synthetic text data along with their labels and save them to a CSV file named output.csv in the same directory.

## Example

Here's an example of what your output might look like:

> The characters were poorly developed and the dialogue was cheesy.,0
>
> The cinematography was stunning and the soundtrack was perfect.,1
>
> I found the plot confusing and the acting was mediocre.,0
>
> This movie was a real tearjerker, I couldn't stop crying.,1
>
> The humor was crude and offensive, I didn't find it funny at all.,0
>
> The chemistry between the two leads was electric, I was rooting for them the whole time.,1
