import pickle
import re
from unidecode import unidecode
from pathlib import Path

PASTA_CONFIGURACOES = Path(__file__).parent / "data" / "configuracoes"
PASTA_CONFIGURACOES.mkdir(exist_ok=True)
PASTA_MENSAGENS = Path(__file__).parent / "data" / "mensagens"
PASTA_MENSAGENS.mkdir(exist_ok=True)
CACHE_DESCONVERTE = {}

#SALVAMENTO E LEITURA DE CONVERSAS

def converte_nome_arquivo(nome_mensagem):
    nome_mensagem = unidecode(nome_mensagem)
    nome_mensagem = re.sub("\W+","", nome_mensagem).lower()
    return nome_mensagem

def desconverte_nome_arquivo(nome_arquivo):
    if nome_arquivo not in CACHE_DESCONVERTE:
        nome_mensagem = ler_mensagem_por_nome_de_arquivo(nome_arquivo, key="nome mensagem")
        CACHE_DESCONVERTE[nome_arquivo] = nome_mensagem
    return CACHE_DESCONVERTE[nome_arquivo]

def retorna_nome_da_mensagem(mensagens):
    nome_mensagem = ""
    for mensagem in mensagens:
        if mensagem["role"] == "user":
            nome_mensagem = mensagem["content"][:30]
            break
    return nome_mensagem

def salvar_mensagem(mensagens):
    if len(mensagens) == 0:
        return False
    nome_mensagem = retorna_nome_da_mensagem(mensagens)
    nome_arquivo = converte_nome_arquivo(nome_mensagem)
    arquivo_salvar = {"nome mensagem":nome_mensagem,
                      "nome arquivo": nome_arquivo,
                      "mensagem": mensagens}
    with open(PASTA_MENSAGENS / nome_arquivo, "wb") as f:
        pickle.dump(arquivo_salvar,f)

def ler_mensagem_por_nome_de_arquivo(nome_arquivo,key="mensagem"):
    with open(PASTA_MENSAGENS / nome_arquivo, "rb") as f:
        mensagens = pickle.load(f)
    return mensagens[key]

def ler_mensagens(mensagens, key = "mensagem"):
    if len(mensagens) == 0:
        return []
    nome_mensagem = retorna_nome_da_mensagem(mensagens)
    nome_arquivo = converte_nome_arquivo(nome_mensagem)
    with open(PASTA_MENSAGENS / nome_arquivo, "rb") as f:
        mensagens = pickle.load(f)
    return mensagens[key]

def listar_conversas():
    conversas = list(PASTA_MENSAGENS.glob("*"))
    conversas = sorted(conversas,key=lambda item: item.stat().st_mtime_ns,reverse=True)
    return [c.stem for c in conversas]

#SALVAMENTO E LEITURA DA API KEY

def salvar_key(key):
    with open(PASTA_CONFIGURACOES / "key", "wb") as f:
        pickle.dump(key,f)

def le_key():
    if (PASTA_CONFIGURACOES / "key").exists():
        with open(PASTA_CONFIGURACOES / "key", "rb") as f:
            return pickle.load(f)
    else:
        return ""