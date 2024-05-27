# Tourist Attractions AI Agent

This project is an AI agent designed to collect information about tourist attractions from a specified country/city. It utilizes both OpenAI's GPT model and Google's GenerativeAI (Gemini) model to generate descriptions for tourist attractions. The information collected is presented in an Excel sheet with details such as the country, city, attraction name, descriptions from GPT, descriptions from Gemini, and a combined description.

## Features

- Collects information about tourist attractions using GPT and Gemini models.
- Presents the collected information in an Excel sheet.
- Combines unique points from both GPT and Gemini descriptions.

## Prerequisites

- Python 3.x
- OpenAI API key
- Google GenerativeAI (Gemini) API key

## Usage

1. Extract the zip 
2. Create python venv: python -m venv venv
3. Activate the venv: .\venv\Scripts\Activate
4. Install required packages: pip -r install requirements.txt
3. paste your OWN API Keys for openAI and Gemini. (or pass as ENVs)
4. Run the main.py script: python main.py
5. The collected information will be saved in an Excel file named tourist_attractions.xlsx in the same directory.