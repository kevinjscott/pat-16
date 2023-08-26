```python
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential

class OpenAIQueryHandler:
    def __init__(self):
        self.openai = openai
        self.token_usage = {
            "gpt-4": {"input": 0, "output": 0},
            "gpt-3.5-turbo": {"input": 0, "output": 0},
            "gpt-3.5-turbo-16k": {"input": 0, "output": 0}
        }
        self.token_cost = {
            "gpt-4": {"input": 0.03/1000, "output": 0.06/1000},
            "gpt-3.5-turbo": {"input": 0.0015/1000, "output": 0.002/1000},
            "gpt-3.5-turbo-16k": {"input": 0.003/1000, "output": 0.004/1000}
        }

    def update_token_usage(self, model, response):
        usage = response['usage']
        self.token_usage[model]["input"] += usage["prompt_tokens"]
        self.token_usage[model]["output"] += usage["completion_tokens"]

    def get_usage(self):
        total_tokens = {"input": 0, "output": 0}
        total_cost = 0
        for model, usage in self.token_usage.items():
            total_tokens["input"] += usage["input"]
            total_tokens["output"] += usage["output"]
            total_cost += (usage["input"] * self.token_cost[model]["input"]) + (usage["output"] * self.token_cost[model]["output"])
        return total_tokens, total_cost

    @retry(wait=wait_random_exponential(min=1, max=65), stop=stop_after_attempt(6))
    def chat(self, system_prompt, user_prompt, model="gpt-3.5-turbo-16k"):
        response = self.openai.ChatCompletion.create(
            model = model,
            temperature = 0.0,
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        self.update_token_usage(model, response)
        return(response['choices'][0]['message']['content'])
```