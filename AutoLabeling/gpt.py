import os
import openai

# openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

class API():
    gpt3="openai"

class GPT():
    def __init__(self):
        self.api = eval(API.gpt3)

    def engines(self):
        return self.api.Engine.list()

    def completion(self, prompt, parameters = {}):
        prompt = prompt[:2000] # 2049 max token length
        
        gpt_parameters = dict(
          engine="davinci",
          prompt=prompt,
          temperature=0.3,
          max_tokens=10,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["\n"]
        )
        
        gpt_parameters.update(parameters)
        
        response = self.api.Completion.create(
          **gpt_parameters
        )

        text_completion = response.choices[0].text
        return text_completion.strip().lower()