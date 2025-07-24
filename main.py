from transformers import pipeline

# Load the question-answering model
qa = pipeline("question-answering")

# Provide context and question

question = "What is artificial intelligence?"

# Get the answer
result = qa(question=question)

print("Answer:", result['answer'])
