
from openai import OpenAI
#pip install openai

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-0LYOO4ylzXzDCRCJVkxZT3BlbkFJHTYrrOj0HcvwQB1B7yMI"
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Nova, skilled in general tasks like Alexa, Google Cloud"},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message.content)


#Cannot use api key without a plan, need chatgpt plus for integrating this