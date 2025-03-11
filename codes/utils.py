import re
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import GoogleGenerativeAI
import csv
import pandas as pd
import ollama
def extract_task_list(long_string):
    """Extract the task list from a long string."""
    lines = long_string.split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    lines = [line for line in lines if not re.match(r'^\d+\.', line)]
    return lines

def call_gpt(prompt, temperature=0.7, max_tokens=None, timeout=None):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout
    )
    result = llm.invoke(prompt)
    return result.content

def call_claude(prompt, temperature=0.7, max_tokens=None, timeout=None):
    llm = ChatAnthropic(model="claude-3-5-sonnet-20241022",
                        temperature=temperature,
                        max_tokens=max_tokens,
                        timeout=timeout)
    result = llm.invoke(prompt)
    return result.content

def call_gemini(prompt, temperature=0.7, max_tokens=None, timeout=None):
    llm = GoogleGenerativeAI(model="gemini-1.5-flash",
                             temperature=temperature,
                             max_tokens=max_tokens,
                             timeout=timeout)
    result = llm.invoke(prompt)
    return result

def calculate_workflow_length_loss(annotations, responses):
    loss = 0
    for i in range(len(annotations)):
        filtered_responses = responses[responses["task_id"] == annotations.iloc[i]["id"]]
        for j in range(len(filtered_responses)):
            loss += abs(filtered_responses.iloc[j]["task_length"] - annotations.iloc[i]["task_length"])
    loss = loss / len(annotations)
    return loss

def find_task_length(outline):
    number_list = []
    lines = outline.split("\n")
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit():
                # Check if next char forms a 2-digit number
                if j + 1 < len(line) and line[j + 1].isdigit():
                    if j + 2 < len(line) and line[j + 2] == '.':
                        num = int(line[j:j+2])
                        number_list.append(num)
                else:
                    if j + 1 < len(line) and line[j + 1] == '.':
                        num = int(char)
                        if num <= 10:
                            number_list.append(num)
    if not number_list:
        return 0
    return max(number_list)

def call_api(api_type, prompt_file, output_file, model, ollama_model='deepseek-r1:latest', temperature=0.7):
    '''
    api_type: 'workflow' or 'code'
    prompt_file: the path to the csv file containing the prompts
    output_file: the path to the csv file where responses will be written
    model: 'gpt4', 'claude', 'gemini'

    this function will call the api for each prompt in the prompt_file and write the responses to the output_file
    '''
    prompts = pd.read_csv(prompt_file)
    with open(prompt_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['task_id', 'response_id', 'prompt_type', 'response_type', 'Arcpy', 'llm_model', 'response_content', 'task_length'])

    responses = []
    for i, content in prompts.iterrows():
        if i > 0:  # Clear previous line if not first iteration
            print('\r' + ' ' * 50 + '\r', end='')  # Clear the previous line
        print(str(i+1) + '/' + str(len(prompts)), end='', flush=True)
        responses = []
        prompt = content['prompt_content']
        for i in range(3):
            if model == 'gpt4':
                response = call_gpt(prompt, temperature)
            elif model == 'claude':
                response = call_claude(prompt, temperature)
            elif model == 'gemini':
                response = call_gemini(prompt, temperature)
            elif model == 'ollama':
                response = call_ollama(prompt, ollama_model, temperature)
            responses.append(response)
        with open(output_file, "a", newline='') as f:
            writer = csv.writer(f)
            if content['domain_knowledge'] == True and content['dataset'] == True:
                type = 'domain_and_dataset'
            elif content['domain_knowledge'] == True:
                type = 'domain'
            elif content['dataset'] == True:
                type = 'dataset'
            else:
                type = 'original'
            if api_type == 'workflow':
                for i, response in enumerate(responses):
                    writer.writerow([content['task_id'], str(content['task_id'])+api_type+str(i), type, api_type, content['Arcpy'], model, response, len(extract_task_list(response))])
            elif api_type == 'code':
                for i, response in enumerate(responses):
                    writer.writerow([content['task_id'], str(content['task_id'])+api_type+str(i), type, api_type, content['Arcpy'], model, response, 'none'])


def call_ollama(prompt, model='deepseek-r1:latest', temperature=0.7):
    # call ollama with different open source models
    response = ollama.generate(
        model=model,
        options={"temperature": temperature},
        prompt=prompt,
    )
    result = response.response
    if '</think>' in result:
        return result.split("</think>")[1].strip() # for deepseek-r1:latest
    else:
        return result