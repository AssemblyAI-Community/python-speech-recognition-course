import openai
from api_secrets import API_KEY_OPENAI

openai.api_key = API_KEY_OPENAI

def ask_computer(prompt):
    return "This is my answer"

    # prompt = "What is your favorite color?"
    res = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
    )
    # print(res)
    return res["choices"][0]["text"]
