# QA Chatbot with Google Gemini

This QA chatbot built using Google Gemini, a large language model. This chatbot is designed to answer your questions in a conversational way.

## Features:

Leverages the power of Google Gemini to access and process information.
Provides answers to your questions in a natural and engaging way.
Continuously learns and improves based on user interactions.

## Requirements:

 - Python 3.10
 - Google API Key for Gemini (https://aistudio.google.com/app/apikey) 

## Setup:

## 1. Create a virtual environment

```
conda create -p venv python=3.10 -y
```

## 2. Install dependencies:

```
pip install -r requirements.txt
```

## 3. Activate the environment

```
source activate ./venv/
```


## 4. Create a .env file:

  - Create a file named .env in the project root directory. This file will store your Google API key. Add the following line to the .env file, replacing YOUR_API_KEY with your actual key:

  - GEMINI_API_KEY=YOUR_API_KEY


## 5. Running the Chatbot:

Start the chatbot using the following command:

```
streamlit run app.py
```

This will launch the chatbot in your web browser.


## Usage:

Once the chatbot is running, you can interact with it by typing your questions in the chat window. The chatbot will use Google Gemini to understand your questions and provide informative answers.
