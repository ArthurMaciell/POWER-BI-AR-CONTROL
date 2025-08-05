# 🧠 Projeto: FastAPI + RD Station + Power BI

Este projeto tem como objetivo integrar dados da plataforma **RD Station** com o **Power BI** por meio de uma API desenvolvida com **FastAPI**. Ele permite que dados atualizados sejam acessados automaticamente, seja por agendamento de chamadas ou por integração com webhooks.

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python 3.10+](https://www.python.org/)
- [RD Station API](https://developers.rdstation.com/)
- [Power BI](https://powerbi.microsoft.com/)
- (Opcional) [ngrok](https://ngrok.com/) para testes com webhooks

## 📂 Estrutura do Projeto

```
.
├── app/
│   ├── main.py               # Entrada da API FastAPI
│   ├── rd_integration.py     # Lógica de extração de dados do RD Station
│   └── utils.py              # Funções auxiliares (ex: autenticação, parse etc.)
├── requirements.txt
└── README.md
```

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
```

## ▶️ Rodando o servidor

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:  
📍 `http://localhost:8000`

## 🔁 Agendando atualizações para o Power BI

Para manter os dados sempre atualizados, você pode agendar uma chamada para o endpoint:

```bash
GET /atualizar-dados
```

Exemplo com `curl` (para usar no Agendador de Tarefas ou crontab):

```bash
curl http://localhost:8000/atualizar-dados
```

## 📈 Integração com o Power BI

1. No Power BI, use **Obter Dados → API da Web**.
2. Insira a URL: `http://localhost:8000/atualizar-dados`
3. O Power BI irá importar os dados atualizados da sua API.

## 🔐 Autenticação com RD Station

A autenticação é feita via OAuth2. Para configurar:

1. Registre seu app no RD Station.
2. Adicione suas credenciais no `.env` ou diretamente no código:

```env
RD_CLIENT_ID=xxx
RD_CLIENT_SECRET=xxx
RD_REFRESH_TOKEN=xxx
```

## 📌 Possíveis melhorias

- [ ] Adicionar suporte a webhooks do RD Station
- [ ] Salvar dados em banco de dados SQL ou planilha
- [ ] Criar interface de dashboard
- [ ] Deploy na nuvem (Railway, Render, etc.)

## 🤝 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 🧑‍💻 Autor

Desenvolvido por [Seu Nome](https://github.com/seu-usuario) 🚀