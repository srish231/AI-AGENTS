from transformers import pipeline
import re
import math

# Load a text generation model for interpreting the user's intent
agent = pipeline("text2text-generation", model="google/flan-t5-base")

def detect_operation(question):
    """Returns the type of operation based on keywords."""
    question = question.lower()

    if any(op in question for op in ["add", "plus", "sum", "total"]):
        return "add"
    elif any(op in question for op in ["subtract", "minus", "difference", "less"]):
        return "subtract"
    elif any(op in question for op in ["multiply", "times", "product"]):
        return "multiply"
    elif any(op in question for op in ["divide", "divided", "quotient"]):
        return "divide"
    elif any(op in question for op in ["square root", "sqrt", "root"]):
        return "sqrt"
    elif any(op in question for op in ["power", "raised to", "exponent"]):
        return "power"
    else:
        return None


while True:
    user_input = input("🧠 Ask me a math question (or type 'exit'): ")

    if user_input.lower() == 'exit':
        break

    # Let the agent clarify the question
    reformulated = agent(user_input, max_length=50)[0]['generated_text']
    print("🤖 Reformulated question:", reformulated)

    operation = detect_operation(user_input)

    # Extract all numbers
    numbers = re.findall(r"-?\d+\.?\d*", user_input)
    numbers = [float(num) for num in numbers]

    try:
        if operation == "add" and len(numbers) >= 2:
            result = numbers[0] + numbers[1]
            print(f"🧮 Result: {result}")

        elif operation == "subtract" and len(numbers) >= 2:
            result = numbers[0] - numbers[1]
            print(f"🧮 Result: {result}")

        elif operation == "multiply" and len(numbers) >= 2:
            result = numbers[0] * numbers[1]
            print(f"🧮 Result: {result}")

        elif operation == "divide" and len(numbers) >= 2:
            result = numbers[0] / numbers[1]
            print(f"🧮 Result: {result:.2f}")

        elif operation == "sqrt" and len(numbers) >= 1:
            result = math.sqrt(numbers[0])
            print(f"🧮 Square root of {numbers[0]} is {result:.2f}")

        elif operation == "power" and len(numbers) >= 2:
            result = math.pow(numbers[0], numbers[1])
            print(f"🧮 {numbers[0]} raised to {numbers[1]} is {result:.2f}")

        else:
            print("❓ Sorry, I couldn't understand the operation or found insufficient numbers.")
    except Exception as e:
        print("⚠️ Error occurred:", e)
