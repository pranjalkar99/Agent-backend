import os

def initialize_env():
    #Langchain
    os.environ['LANGCHAIN_TRACING_V2'] = ''
    os.environ['LANGCHAIN_ENDPOINT'] = ""
    os.environ['LANGCHAIN_API_KEY'] = ""
    os.environ['LANGCHAIN_PROJECT' ]= ""

    #Vectara
    os.environ["VECTARA_CUSTOMER_ID"] = ''
    os.environ["VECTARA_CORPUS_ID"] = ''
    os.environ["VECTARA_API_KEY"] = ''

    #Zuki
    os.environ['OPENAI_API_KEY'] = ''
    os.environ['OPENAI_API_BASE'] = ''