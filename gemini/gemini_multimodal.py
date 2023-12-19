import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image


def load_img(file_pth):
    return PIL.Image.open(file_pth)


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def vision(img):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(img)
    to_markdown(response.text)
    response = model.generate_content(["Tell me the fruit name and ripeness level.", img], stream=True)
    response.resolve()
    to_markdown(response.text)
    vision_output = response.text
    return vision_output


def chat(inpt_frm_vsn):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    chat

    res = inpt_frm_vsn + 'Tell me the fruit name and nutrition'

    while True:
        response = chat.send_message(res, generation_config=genai.types.GenerationConfig(
            max_output_tokens=200
        ))
    
        to_markdown(response.text)

        print('Gemini: ' + response.text)
        res = input('User: ')

def main():
    img_path = 'assets/apple.jpg'
    img = load_img(img_path)
    display(img)

    GOOGLE_API_KEY = 'AIzaSyA1bYLSWmPCXiN7C6LdyrLtXmtw7ylbuS0'

    genai.configure(api_key=GOOGLE_API_KEY)

    vision_result = vision(img)
    print(vision_result)

    check_point = input("If you want to continue chat write 'nutrition': ")


    if check_point == 'nutrition':
        chat(vision_result)



if __name__ == "__main__":
    main()
