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
chat = model.start_chat(history=[])
chat



while True:
    res = input('User: ')
    response = chat.send_message(res)
    to_markdown(response.text)

    print('Gemini: ' + response.text)
    
    

