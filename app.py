import random
import re
from collections import defaultdict, Counter

import streamlit as st


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Markov Text Generator",
    page_icon="🔗",
    layout="wide"
)


# ============================================================
# CUSTOM STYLE
# ============================================================

st.markdown(
    """
    <style>
    .title {
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        font-size: 18px;
        color: gray;
        margin-bottom: 25px;
    }

    .output-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #cccccc;
        min-height: 150px;
        line-height: 1.8;
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="title">🔗 Markov Text Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Generate new text using a word-based Markov Chain.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DEFAULT TRAINING TEXT
# ============================================================

default_training = """Artificial intelligence is changing the way people work and learn.
Machine learning helps computers discover patterns from data.
Machine learning is used in many real world applications.
Artificial intelligence can help people solve complex problems.
Natural language processing allows computers to understand human language.
Text generation is an interesting application of machine learning.
Markov chains can be used to generate text from previously observed patterns.
The model learns which words are likely to appear after other words.
This project demonstrates simple text generation using probability.
Machine learning is becoming an important part of modern technology.
Artificial intelligence is helping businesses improve their products.
Data is an important part of machine learning.
Learning from data allows computers to make useful predictions."""


# ============================================================
# TOKENIZE TEXT
# ============================================================

def tokenize(text):

    return re.findall(
        r"\b[\w']+\b|[.!?,;:()]",
        text.lower()
    )


# ============================================================
# BUILD MARKOV MODEL
# ============================================================

def build_model(words, order):

    model = defaultdict(Counter)

    for i in range(len(words) - order):

        current_state = tuple(
            words[i:i + order]
        )

        next_word = words[i + order]

        model[current_state][next_word] += 1

    return model


# ============================================================
# SELECT NEXT WORD
# ============================================================

def next_word(counter, temperature):

    words = list(counter.keys())

    counts = list(counter.values())

    if temperature <= 0.1:

        return words[counts.index(max(counts))]

    probabilities = [
        count ** (1 / temperature)
        for count in counts
    ]

    return random.choices(
        words,
        weights=probabilities,
        k=1
    )[0]


# ============================================================
# CONVERT TOKENS INTO SENTENCE
# ============================================================

def make_sentence(words):

    result = ""

    punctuation = {
        ".", ",", "!", "?", ";", ":"
    }

    for word in words:

        if result == "":
            result = word

        elif word in punctuation:
            result += word

        else:
            result += " " + word

    return result


# ============================================================
# FIND STATE USING USER PROMPT
# ============================================================

def find_state(model, prompt_words, order):

    if len(prompt_words) >= order:

        state = tuple(
            prompt_words[-order:]
        )

        if state in model:
            return state

    # Search for partial match
    for size in range(
        min(order, len(prompt_words)),
        0,
        -1
    ):

        last_words = tuple(
            prompt_words[-size:]
        )

        possible_states = []

        for state in model:

            if state[-size:] == last_words:

                possible_states.append(state)

        if possible_states:

            return random.choice(
                possible_states
            )

    return None


# ============================================================
# GENERATE TEXT
# ============================================================

def generate_text(
    model,
    prompt,
    order,
    number_of_words,
    temperature
):

    prompt_words = tokenize(prompt)

    if len(prompt_words) == 0:

        return "Please enter some starting text."

    state = find_state(
        model,
        prompt_words,
        order
    )

    # If the prompt is not found,
    # find a state containing one of its words.
    if state is None:

        matching_states = []

        for s in model:

            for word in prompt_words:

                if word in s:

                    matching_states.append(s)

        if matching_states:

            state = random.choice(
                matching_states
            )

        else:

            state = random.choice(
                list(model.keys())
            )

    generated = prompt_words.copy()

    for _ in range(number_of_words):

        if state not in model:

            state = random.choice(
                list(model.keys())
            )

        word = next_word(
            model[state],
            temperature
        )

        generated.append(word)

        state = tuple(
            generated[-order:]
        )

    return make_sentence(generated)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Model Settings")

    order = st.slider(
        "Markov Order",
        1,
        4,
        2
    )

    number_of_words = st.slider(
        "Words to Generate",
        10,
        150,
        50,
        step=10
    )

    temperature = st.slider(
        "Randomness",
        0.1,
        2.0,
        1.0,
        step=0.1
    )

    st.write("")

    st.info(
        "Lower randomness gives more predictable "
        "results. Higher randomness gives more variety."
    )


# ============================================================
# TRAINING DATA
# ============================================================

st.subheader("📚 Training Text")

st.write(
    "Enter the text that the Markov model should learn from."
)

training_text = st.text_area(
    "Training Data",
    value=default_training,
    height=220,
    label_visibility="collapsed"
)


# ============================================================
# CREATE MODEL
# ============================================================

training_words = tokenize(
    training_text
)

model = build_model(
    training_words,
    order
)


st.divider()


# ============================================================
# USER INPUT + OUTPUT
# ============================================================

left, right = st.columns(2)


# ============================================================
# USER PROMPT
# ============================================================

with left:

    st.subheader("✍️ Your Text")

    st.write(
        "Enter a starting sentence or phrase."
    )

    user_text = st.text_area(
        "Starting Text",
        placeholder="Example: Machine learning",
        height=160,
        label_visibility="collapsed"
    )

    st.caption(
        "The model will continue your text using "
        "patterns learned from the training data."
    )


# ============================================================
# OUTPUT
# ============================================================

with right:

    st.subheader("✨ Generated Text")

    if st.button(
        "✨ Generate Text",
        type="primary",
        use_container_width=True
    ):

        if len(training_words) <= order:

            st.error(
                "Training text is too short. "
                "Please add more text."
            )

        elif user_text.strip() == "":

            st.error(
                "Please enter some starting text."
            )

        else:

            result = generate_text(
                model,
                user_text,
                order,
                number_of_words,
                temperature
            )

            st.session_state["result"] = result


    output = st.session_state.get(
        "result",
        "Generated text will appear here."
    )

    st.markdown(
        f'<div class="output-box">{output}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.divider()

st.subheader("📊 Model Information")

a, b, c = st.columns(3)

with a:

    st.metric(
        "Training Words",
        len(training_words)
    )

with b:

    st.metric(
        "Learned States",
        len(model)
    )

with c:

    st.metric(
        "Markov Order",
        order
    )


# ============================================================
# HOW IT WORKS
# ============================================================

st.divider()

st.subheader("🧠 How It Works")

st.write(
    "**1. Training:** The model reads your training text "
    "and learns word relationships."
)

st.write(
    "**2. User Input:** You enter a starting phrase."
)

st.write(
    "**3. Prediction:** The model finds a matching word "
    "pattern and predicts the next word."
)

st.write(
    "**4. Generation:** The predicted word becomes part "
    "of the next pattern."
)

st.write(
    "**5. Repeat:** This process continues until the "
    "requested number of words is generated."
)


# ============================================================
# EXAMPLE
# ============================================================

with st.expander("📌 Example"):

    st.write("Training Text:")

    st.code(
        "Machine learning helps computers discover patterns from data.\n"
        "Machine learning is useful in many applications.\n"
        "Artificial intelligence is changing modern technology."
    )

    st.write("User Text:")

    st.code(
        "Machine learning"
    )

    st.write(
        "The model will try to continue the user's text "
        "using patterns learned from the training text."
    )


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "Built with Python • Markov Chains • Streamlit • "
    "Prodigy Infotech Task-03"
)