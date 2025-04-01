import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class MarkdownLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the markdown content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract and print the title
        self.title = soup.title.string if soup.title else "No title found"
        #print(f"Title: {self.title}")
        
        # Extract and print the text
        self.text = soup.get_text()
        #print(f"Text: {text}")
                


system_prompt = "You are an assistant that analyzes the contents of a text \
and provides a acronyms and aabbreviations dictionary. "
system_prompt += "for example in the sentence: \
    IDN: número de identificação do equipamento (Identification Number). É um número que identifica de forma única o equipamento dentro do sistema (nenhum equipamento pode ter um IDN já usado por outro equipamento).\
        IDN is the acronym and número de identificação do equipamento is the meaning. "

def messages_for(markdown_loader):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": markdown_loader.text}
    ]

def getAcronymDictionary(file_path):
    md = MarkdownLoader(file_path)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(md)
    )
    return response.choices[0].message.content

def display_acronymDictionary(file_path):
    acronymDictionary = getAcronymDictionary(file_path)
    display(Markdown(acronymDictionary))

#display_acronymDictionary("docs/OPEN_IAM-R2.25.md")    
print(getAcronymDictionary("docs/OPEN_IAM-R2.25.md"))