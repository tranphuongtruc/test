from hugchat import hugchat
from hugchat.login import Login


def generate_response(prompt_input, email, passwd):
    '''
    Function for generating LLM response
    '''
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    
    # Create Chatbot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

