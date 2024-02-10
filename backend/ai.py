import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
model = genai.GenerativeModel('gemini-pro')
generation_config = genai.GenerationConfig(
  temperature=.8,
)

genai.configure(api_key = os.environ['GEMINI_API_KEY'])

generate_tasks_prompt = """: this is a goal that I want to accomplish. Can you generate some potential tasks to work towards this goal and format it in
the following JSON format: 
    [{"name" : task_name, "completed" : False, "pointsValue" : 10}]
    Only return the three best tasks please, and make sure the tasks are short in character length. Make the tasks able to be completed in a
    day. Remove trailing quotes.
"""

generate_response_prompt = """I am going to ask you certain mental health questions, respond to them with potential solutions."""

def gen_tasks(goal_name) -> list:
    complete_prompt = goal_name + generate_tasks_prompt
    tasks_str = model.generate_content(complete_prompt, generation_config=generation_config)
    return json.loads(tasks_str.parts[0].text)

def gen_response(text):
    if text.startswith("""I am going to ask you certain mental health questions, respond to them with potential solutions."""):
        response = model.generate_content(text, generation_config=generation_config)
        return response.parts[0].text
    else:
        print(generate_response_prompt + " " + text)
        response = model.generate_content(generate_response_prompt + " " + text, generation_config=generation_config)
        return response.parts[0].text
