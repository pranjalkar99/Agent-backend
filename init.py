import os

def initialize_env():
    #Langchain
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
    os.environ['LANGCHAIN_API_KEY'] = "ls__5c9cc36a095e4130b0c063a09e9dc393"
    os.environ['LANGCHAIN_PROJECT' ]= "Vectara-test"

    #Vectara
    os.environ["VECTARA_CUSTOMER_ID"] = '4141864993'
    os.environ["VECTARA_CORPUS_ID"] = '2'
    os.environ["VECTARA_API_KEY"] = 'zut_9t_YIYysiVtssUqP51HLgLOd57gyOfubDYnxLw'

    #Zuki
    os.environ['OPENAI_API_KEY'] = 'zu-0418787c5f8c49648ed1c4edf1ddb501'
    os.environ['OPENAI_API_BASE'] = 'https://zukijourney.xyzbot.net/v1'
    
    os.environ["TAVILY_API_KEY"] = "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"
    os.environ["TOGETHER_API_KEY"] = '6e5e02a2d3758839cc7e1bae11c6d4ec1f683744d1fbfcc01192336b7f0e8db4'
    os.environ["GROQ_API_KEY"]="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"