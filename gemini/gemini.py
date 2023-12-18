import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = 'Generate your api key from https://makersuite.google.com/app/apikey and use here'

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Who is Nikola Tesla?")


to_markdown(response.text)

print(response.text)

response.prompt_feedback