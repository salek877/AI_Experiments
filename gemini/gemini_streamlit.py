import streamlit as st
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image



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

    message_count = 0

    continue_chat = True

    while continue_chat:
        if message_count == 0:
            input_msg = inpt_frm_vsn + ' Tell me the fruit name and nutrition. Complete answer in 55 words. Never show the word count.'
        else:
            input_key = f"chat_input_{message_count}"
            user_input = st.chat_input('Please write your message here...', key=input_key)
            if user_input:
                input_msg = user_input + ' Complete answer in 55 words. Never show the word count.'
            else:
                continue_chat = False
                break

        response = chat.send_message(input_msg, generation_config=genai.types.GenerationConfig(
            max_output_tokens=100
        ))
        to_markdown(response.text)
        st.text('Gemini: ' + response.text)
        message_count += 1

        

def main():
    st.title("Gemini")


    GOOGLE_API_KEY = 'AIzaSyDMDS5TghIYsEV4nD6FsC8PDCtqGvkuUls'

    genai.configure(api_key=GOOGLE_API_KEY)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = PIL.Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image.', use_column_width=True)

        vision_result = vision(img)
        st.text(vision_result)

        check_point = st.text_input("If you want to continue chat write 'nutrition': ")

        if check_point.lower() == 'nutrition':
            chat(vision_result)


if __name__ == "__main__":
    main()
