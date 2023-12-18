import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown

import PIL.Image

img = PIL.Image.open('assets/apple.jpg')
img


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = 'Generate your api key from https://makersuite.google.com/app/apikey and use here'

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(img)

to_markdown(response.text)


response = model.generate_content(["What do you see in the given image?", img], stream=True)
response.resolve()

to_markdown(response.text)

print(response.text)