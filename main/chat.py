import openai
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import common.config as config

openai.api_key = config.OPENAI_API

engine_id = "text-davinci-002"

def generate_solution(input_data):
    prompt = "Solution to the following problem:\n" + input_data + "\n\nSolution:"
    model = engine_id
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    solution = response.choices[0].text.strip()
    return solution

def main(input_data):
    solution = generate_solution(input_data)
    print(solution)
