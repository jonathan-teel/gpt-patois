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
    prompt = """ 
    Score the following answer based on relevance, accuracy, completeness, clarity, cepth, creativity, etc. Question: '$$QUESTION$$' Response: '$$ANSWER$$'. Provide only a score from 1 to 10 for each criterion, with 1 indicating poor performance and 10 indicating excellent performance.
    """
    prompt = prompt.replace('$$QUESTION$$', question).replace('$$ANSWER$$', answer)
    print(prompt)
    grade = get_response(prompt)
    return grade

def main():
    with open('inputs.json') as json_file:
        data = json.load(json_file)

    regular_prompts = data['regular_examples']
    gpt_control_prompts = data['gpt_control_examples']

    regular_responses = []
    gpt_control_responses = []

    cnt = 0

    for question in regular_prompts:
        answer = get_response(question)
        grade = grade_response(question, answer)
        regular_responses.append({"question": question, "answer": answer, "grade": grade})
        #if cnt > 1: break
        cnt = cnt + 1

    cnt = 0

    for question in gpt_control_prompts:
        answer = get_response(question)
        grade = grade_response(question, answer)
        gpt_control_responses.append({"question": question, "answer": answer, "grade": grade})
        #if cnt > 1: break
        cnt = cnt + 1

    output = {
        "Regular Responses": regular_responses,
        "GPT-Control Responses": gpt_control_responses
    }

    with open('outputs_gpt4.json', 'w') as json_file:
        json.dump(output, json_file, indent=4)

if __name__ == "__main__":
    main()