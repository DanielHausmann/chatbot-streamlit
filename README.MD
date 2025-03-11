# Chatbot com OpenAI e Streamlit

Este projeto é um chatbot interativo utilizando a API da OpenAI e a biblioteca Streamlit para criar uma interface amigável. O chatbot permite que os usuários façam perguntas e recebam respostas diretamente da IA.

## 🚀 Funcionalidades

- Interface web simples e intuitiva com Streamlit.
- Suporte aos modelos `gpt-3.5-turbo` e `gpt-4`.
- Histórico de conversas salvo localmente.
- Personalização do modelo e chave da API OpenAI.

## 🛠️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-streamlit.git
   cd chatbot-streamlit
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Como Usar

1. Execute o aplicativo:
   ```bash
   streamlit run main.py
   ```
2. Vá até a aba **Configurações** e adicione sua chave da OpenAI.
3. Após configurar a chave, volte para a aba principal e comece a interagir com o chatbot.

## 📂 Estrutura do Projeto
```
📁 chatbot-streamlit
├── main.py                # Interface principal com Streamlit
├── utils_files.py         # Funções para salvar e carregar mensagens/API key
├── utils_openai.py        # Função para chamar a API da OpenAI
├── data/                  # Pasta para armazenamento de dados
│   ├── configuracoes/     # Pasta onde a chave da API é armazenada
│   ├── mensagens/         # Pasta onde as conversas são salvas
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Este arquivo
└── __pycache__/           # Pasta gerada automaticamente pelo Python
```

## 🔧 Melhorias Futuras

- Adicionar suporte a mais modelos da OpenAI.
- Melhorar a segurança do armazenamento da API Key.
- Criar um sistema de login para múltiplos usuários.

## 📜 Licença

Este projeto é de código aberto e está disponível sob a licença MIT. Sinta-se à vontade para contribuir!

---
💡 **Dica:** Não esqueça de criar um arquivo `requirements.txt` com as bibliotecas usadas:
```bash
pip freeze > requirements.txt
```

