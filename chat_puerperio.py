from dotenv import load_dotenv
import os
from openai import OpenAI

# Carrega o .env
load_dotenv()

# Pega a chave
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def chat(pergunta):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em saúde materna e puerpério, com linguagem empática e explicativa."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content

# Teste rápido
if __name__ == "__main__":
    pergunta = input("Digite sua pergunta sobre puerpério: ")
    print(chat(pergunta))

