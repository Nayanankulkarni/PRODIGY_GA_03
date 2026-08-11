# 🔗 Markov Text Generator

<p align="center">
  <b>A simple and interactive text generation application using Markov Chains</b>
</p>

<p align="center">
  Built with Python and Streamlit as part of the Prodigy Infotech Internship.
</p>

---

## 📌 Project Overview

The **Markov Text Generator** is a simple Natural Language Processing project that demonstrates how text can be generated using a **Markov Chain**.

The application learns word-to-word relationships from a given training text. After learning these patterns, the user can provide their own starting text or prompt, and the application generates a continuation based on the probabilities learned from the training data.

Unlike modern Large Language Models, this project does not use an external AI API or a pre-trained neural network. Instead, it demonstrates the basic concept of **probabilistic text generation** using a lightweight statistical approach.

---

## 🎯 Objective

The main objective of this project is to understand the fundamentals of:

- Markov Chains
- Text generation
- Natural Language Processing
- Probability-based prediction
- N-gram language modeling
- Tokenization
- Random sampling

The project provides a practical and interactive way to understand how a simple statistical model can generate text.

---

## ✨ Features

### 📚 Custom Training Text

Users can provide their own training text.

The model analyzes the training data and learns which words commonly appear after other words.

### ✍️ User Starting Text

The application allows users to enter their own starting phrase or sentence.

Example:

```text
Machine learning
