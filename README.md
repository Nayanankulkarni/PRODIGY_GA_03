🔗 Markov Text Generator

A simple and interactive Text Generation application using Markov Chains, built with Python and Streamlit as part of Prodigy Infotech Task-03.

The application learns word patterns from training text and generates new text based on the learned probabilities. Users can also enter their own starting text and generate a continuation.

📌 Project Overview

A Markov Chain is a probabilistic model where the next state depends on the current state or a limited number of previous states.

In this project, words are treated as states.

For example, with a 2nd-order Markov Chain:

machine learning → is
learning is → useful

The model learns these relationships from the training text and uses them to generate new text.

✨ Features
📚 Custom training text
✍️ User-defined starting text/prompt
🔗 Word-based Markov Chain
⚙️ Adjustable Markov order from 1–4
📝 Adjustable number of generated words
🎲 Adjustable randomness
📊 Training token statistics
📈 Learned state statistics
🖥️ Interactive Streamlit interface
🚫 No external AI API required
⚡ Lightweight and easy to run
🎯 How It Works
              Training Text
                    ↓
               Tokenization
                    ↓
             Markov Model
                    ↓
          Learn Word Patterns
                    ↓
             User Prompt
                    ↓
          Find Matching State
                    ↓
           Predict Next Word
                    ↓
             Update State
                    ↓
              Repeat
                    ↓
            Generated Text
🧠 Example
Training Text
Machine learning helps computers discover patterns from data.
Machine learning is useful in many applications.
Artificial intelligence is changing modern technology.
User Input
Machine learning
Generated Output

The model can generate a continuation such as:

Machine learning is useful in many applications.

The exact output can vary because the model uses probabilistic sampling.

🛠️ Technologies Used
Python
Streamlit
Markov Chains
Natural Language Processing
Probability & Statistics
Regular Expressions
Python Collections
📂 Project Structure
markov-text-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/markov-text-generator.git

Move into the project:

cd markov-text-generator
2. Create a Virtual Environment

For Windows:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
🚀 Run the Application

Start Streamlit:

streamlit run app.py

The application will open at:

http://localhost:8501

If it doesn't open automatically, copy the URL into your browser.

🎛️ Model Settings
Markov Order

Controls how many previous words are used to predict the next word.

Order	Description
1	Uses 1 previous word
2	Uses 2 previous words
3	Uses 3 previous words
4	Uses 4 previous words

Higher orders generally preserve more local context but require more training data.

Words to Generate

Controls how many new words the application generates after the user's prompt.

Randomness

Controls the variation in generated text.

Lower value → more predictable
Higher value → more random
🔍 Understanding the Algorithm
Step 1 — Tokenization

The training text is divided into words and punctuation.

Example:

Machine learning is useful.

becomes approximately:

machine
learning
is
useful
.
Step 2 — Create States

For Markov order 2:

machine learning → is
learning is → useful
Step 3 — Learn Probabilities

The model counts how frequently words appear after each state.

For example:

machine learning → is

may occur multiple times in the training data.

Step 4 — User Prompt

The user provides a starting phrase:

Artificial intelligence
Step 5 — Find a Matching State

The model searches its learned states for a matching pattern.

Step 6 — Predict

The model selects the next word based on the learned probabilities.

Step 7 — Repeat

The generated word becomes part of the next state, and the process continues.

📊 Example Workflow
Training Data:
"Machine learning is useful.
Machine learning is powerful."

             ↓

Learned States:

machine learning → is
learning is → useful / powerful

             ↓

User Prompt:

Machine learning

             ↓

Generated:

Machine learning is useful.
⚠️ Limitations

This project is a statistical text generator, not a Large Language Model.

Therefore:

It does not understand semantic meaning.
It has limited context.
It depends heavily on the training data.
It may generate repetitive text.
It may produce grammatically incorrect sentences.
It does not have external knowledge.
It cannot reason like modern AI language models.

The quality of generated text improves when the training corpus is larger and more diverse.

🎓 Learning Outcomes

This project helped demonstrate:

Markov Chains
Probability distributions
N-gram language modeling
Tokenization
Natural Language Processing fundamentals
Random sampling
Text generation
Streamlit application development
🔮 Future Improvements

Possible future enhancements include:

📄 Upload .txt files as training data
📑 PDF/DOCX training-data support
📊 Word-frequency visualization
📈 Probability charts
💾 Save and load trained models
📥 Download generated text
🔤 Bigram vs trigram comparison
🧠 Comparison with neural language models
🌐 Deployment as an online application
🚀 Deployment

This project uses Streamlit, so it can be deployed using a Streamlit-compatible hosting platform.

For deployment, make sure the repository contains:

app.py
requirements.txt
README.md

and that requirements.txt contains:

streamlit
📌 Internship Task

Organization: Prodigy Infotech
Task: Task-03 — Text Generation with Markov Chains

👩‍💻 Author

Nayana N. Kulkarni

Information Science & Engineering
Interested in Artificial Intelligence, Machine Learning, Data Analytics and Software Development.

⭐ If You Like This Project

If this project helped you understand Markov Chains and text generation, consider giving the repository a ⭐ on GitHub.
