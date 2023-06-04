import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")

openai.api_key = OPENAI_API_KEY

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model=OPENAI_API_MODEL,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def grade_response(question, answer):
    prompt = """ Using these guidelines:
    Relevance: The response should directly address the question and stay on-topic throughout.
    Accuracy: The information provided should be factually correct.
    Completeness: The response should fully answer the question, without leaving out any significant details that pertain to the question.
    Clarity: The response should be easy to understand, well-structured, and coherently organized. It should avoid unnecessary jargon or complex language, unless appropriate for the context (such as a technical question).
    Depth: The response should provide insight beyond the basic answer, when possible. It could include nuances, different perspectives, or deeper analysis.
    Creativity: If appropriate, the response could be evaluated on its creativity, such as providing a unique perspective, interesting examples, or an engaging style of communication.
    
    Grade the following answer to the provided question\n
    """
    grading_prompt = f"question: '{question}' \n answer: '{answer}'."
    grade = get_response(prompt + grading_prompt)
    return grade

def main():
    with open('inputs.json') as json_file:
        data = json.load(json_file)

    regular_prompts = data['regular_examples']
    gpt_control_prompts = data['gpt_control_examples']

    regular_responses = []
    gpt_control_responses = []

    for question in regular_prompts:
        answer = get_response(question)
        grade = grade_response(question, answer)
        regular_responses.append({"question": question, "answer": answer, "grade": grade})

    for question in gpt_control_prompts:
        answer = get_response(question)
        grade = grade_response(question, answer)
        gpt_control_responses.append({"question": question, "answer": answer, "grade": grade})

    print("Regular Responses:", regular_responses)
    print("GPT-Control Responses:", gpt_control_responses)

if __name__ == "__main__":
    main()