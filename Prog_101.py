from openai import OpenAI

client = OpenAI(api_key = "Tutaj wrzuć klucz API-Chat")

with open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", encoding = 'utf8') as plik:
    wytyczne = '''Użyj odpowiednich tagów HTML do struktry treści,
                oznacz miejsca gdzie powinny pojawić sie grafiki za pomocą tagu <img src="image_placeholder.jpg">,
                dodając tag alt do obrazków z rozbudownym promptem do wygerowania grafiki,
                utwórz bardzo krótki podpis pod obrazkami za pomocą odpowiednich znaczników html,
                nastpenie usuń wszystkie znaczniki <body>, </body>,<html>,</html>, <head>, </head>\n '''
    wytyczne += ''. join(plik.readlines())

odp_gpt= client.chat.completions.create(
    model = "gpt-4",
    messages = [{
            "role":"user",
            "content": wytyczne,
    }],
    temperature = 1,
    max_tokens = 1500,
    top_p=1.0,
    )
print(odp_gpt.choices[0].message.content)
with open ("artykul.html", 'w') as plik:
    plik.write(odp_gpt.choices[0].message.content)
