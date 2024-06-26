import os
from openai import OpenAI

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

prompt = input("Prompt: ")

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="hd",
  n=1,
)

image_url = response.data[0].url
print(image_url)