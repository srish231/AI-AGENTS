#CALCULATOR AGENT

python -m venv venv
.\venv\Scripts\activate

pip install transformers
pip install torch
pip install accelerate

pip install datasets
pip install huggingface_hub

from transformers import pipeline

# Load the question-answering model
qa = pipeline("question-answering")

# Provide context and question

question = "What is artificial intelligence?"

# Get the answer
result = qa(question=question)

print("Answer:", result['answer'])
