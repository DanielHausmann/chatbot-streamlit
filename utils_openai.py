import openai


def retorna_resposta_modelo(mensagens,
                            openai_key,
                            modelo = "gpt-3.5-turbo",
                            temperatura = 0,
                            stream = False
):
    client = openai.Client(api_key=openai_key)

    resposta = client.chat.completions.create(
        messages=mensagens,
        model=modelo,
        temperature=temperatura,
        stream=stream
    )
    return resposta
