# 🔗 Markov Text Generator

A simple **text generation application using Markov Chains**, built as **Prodigy Infotech Task-03**.

The project demonstrates how a statistical language model can learn relationships between words and generate new text based on the probability of the next word.

## 📌 Project Overview

A Markov Chain is a mathematical model where the next state depends on the current state or a limited number of previous states.

In this project, words are treated as states.

For example, with a **2nd-order Markov Chain**:

```text
Artificial intelligence is changing the world.
```

The model learns transitions such as:

```text
Artificial intelligence → is
intelligence is → changing
is changing → the
changing the → world
```

During generation, the model uses these learned transitions to predict the next word.

## ✨ Features

- Word-based Markov Chain text generation
- Supports Markov orders from 1 to 4
- Adjustable generated text length
- Adjustable randomness using temperature
- Custom training text
- Displays training token count
- Displays learned Markov states
- Clean Streamlit web interface
- No external AI API required
- Lightweight and easy to understand

## 🛠️ Technologies Used

- Python
- Markov Chains
- Probability & Statistics
- Regular Expressions
- Streamlit
- Collections (`defaultdict`, `Counter`)

## 📂 Project Structure

```text
markov-text-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/markov-text-generator.git
cd markov-text-generator
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How the Markov Model Works

The implementation uses an **N-order Markov Chain**.

### Order 1

```text
previous word → next word
```

Example:

```text
machine → learning
```

### Order 2

```text
previous 2 words → next word
```

Example:

```text
machine learning → is
```

### Order 3

```text
previous 3 words → next word
```

Example:

```text
machine learning is → useful
```

Higher orders usually preserve more local context but require more training data.

## 🎛️ Model Parameters

### Markov Order

Controls how many previous tokens are used to predict the next token.

- `1` → more random
- `2` → balanced
- `3` → more contextual
- `4` → more dependent on training text

### Generated Words

Controls the length of the generated output.

### Randomness / Temperature

Controls how deterministic the generated text is.

- Lower temperature → more predictable
- Higher temperature → more diverse/random

## 📐 Algorithm

```text
Input Training Text
        ↓
Tokenization
        ↓
Create N-word States
        ↓
Count Next-Word Frequencies
        ↓
Build Markov Model
        ↓
Choose Starting State
        ↓
Sample Next Word
        ↓
Update State
        ↓
Repeat
        ↓
Generated Text
```

## 🔍 Example

Training text:

```text
Machine learning is useful.
Machine learning is powerful.
Machine learning helps computers learn.
```

A 2nd-order model can learn:

```text
(machine, learning) → is
(learning, is) → useful / powerful
```

The generator can then create text such as:

```text
Machine learning is powerful.
```

The exact output changes because the model uses probabilistic sampling.

## ⚠️ Limitations

This is a statistical text generator, not a modern Large Language Model.

It:

- does not understand semantic meaning
- has limited long-range context
- depends heavily on training text
- can generate repetitive or grammatically incorrect sentences
- does not have factual knowledge
- does not use neural networks

## 🎯 Learning Outcomes

This project helps understand:

1. Markov Chains
2. Probability distributions
3. Natural Language Processing basics
4. Tokenization
5. N-gram language models
6. Random sampling
7. Text generation
8. Streamlit application development

## 📌 Future Improvements

- Add sentence-level training
- Add file upload for `.txt` documents
- Add bigram/trigram comparison
- Add probability visualization
- Add word-frequency charts
- Add model save/load functionality
- Add a larger corpus
- Compare Markov generation with GPT-based generation

## 👩‍💻 Internship Task

**Task:** Task-03 — Text Generation with Markov Chains  
**Organization:** Prodigy Infotech

## 📄 License

This project is intended for educational and internship purposes.
