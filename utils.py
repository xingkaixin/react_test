import openai

from config import openai_config


def ask_ai(messages: list):
    openai.api_key = openai_config.key
    openai.api_base = openai_config.base_url
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3,
        max_tokens=2048,
        stop="Observation",
    )
    print(response)
    if "choices" in response:
        return (
            response["choices"][0].get("message").get("content").encode("utf8").decode()
        )
    else:
        raise ValueError("Invalid response from ChatGPT")


def get_github_user_info(user: str):
    import requests

    response = requests.get(f"https://api.github.com/users/{user}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Invalid response from GitHub API")


def calculator_tool(expression):
    return eval(expression)
