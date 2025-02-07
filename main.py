import os
import grants
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = grants.LANGCHAIN_API_KEY
os.environ['OPENAI_API_KEY'] = grants.OPENAI_API_KEY
os.environ["DEEPSEEK_API_KEY"] = grants.DEEPSEEK_API_KEY



