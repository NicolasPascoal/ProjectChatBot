# FURIA FanBot 🔥

Este repositório contém a solução desenvolvida para o desafio técnico da vaga de Assistente de Engenharia de Software da FURIA Tech.

O projeto inclui:

- Um **chatbot funcional** desenvolvido em Python com integração ao Telegram, projetado para proporcionar uma experiência interativa aos fãs da equipe de CS da FURIA.
- Uma **landing page moderna**, com visual inspirado no site oficial da FURIA, explicando as funcionalidades do bot e com link direto de acesso.

---

## 📌 Funcionalidades do Bot

O FanBot é acessado pelo Telegram e oferece os seguintes comandos:

| Comando        | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| `/start`       | Mensagem de boas-vindas e apresentação do bot                             |
| `/quemSomos`   | Informações institucionais sobre a FURIA                                  |
| `/jogadores`   | Line-up atual da equipe de CS2                                             |
| `/status`      | Simulação de uma partida ao vivo                                          |
| `/proxjogo`    | Próxima partida agendada da equipe                                        |
| `/redes`       | Links das redes sociais oficiais da FURIA                                 |
| `/loja`        | Link direto para a loja oficial da FURIA                                  |

---

## 🌐 Landing Page

A landing page foi construída em HTML, CSS e Bootstrap, e inclui:

- Hero section com chamada visual e botão de acesso ao bot
- Seção explicativa com texto voltado para fãs
- Cards apresentando as funcionalidades
- Estilo visual adaptado ao tema da FURIA

Acesse o bot diretamente por aqui:  
👉 [@furia_fanbot](http://t.me/FanDafuria_bot)

---

## 💻 Tecnologias Utilizadas

- **Python 3.10+**
- **python-telegram-bot**
- **HTML5 + CSS3**
- **Bootstrap 5.3**
- **Font Awesome**
- **Google Fonts (Oxanium)**

---

## ⚙️ Como rodar o projeto localmente

### 🔸 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/furia-fanbot.git
cd furia-fanbot
```

### 🔸 2. Crie e ative o ambiente virtual

No **Windows**:

```bash
python -m venv venv
.env\Scriptsctivate
```

No **Linux/Mac**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 🔸 3. Instale as dependências

```bash
pip install python-telegram-bot
```

> Outras bibliotecas (como `Flask`, `streamlit`, etc.) **não são necessárias** neste projeto.

---

### 🔸 4. Configure o token do bot

No arquivo `main.py` (ou `bot.py`), substitua o valor da variável `TOKEN` pela sua chave do BotFather:

```python
TOKEN = "SEU_TOKEN_AQUI"
```

---

### 🔸 5. Execute o bot

```bash
python main.py
```

---

## 🖼️ Estrutura de Pastas

```
furia-fanbot/
│
├── main.py                # Código do bot Telegram
├── index.html             # Landing page
├── style.css              # Estilo da landing
├── img/                   # Imagens usadas na página
│   ├── furia-logo.jpeg
│   └── Furia-logo-animation.png
├── background.jpg         # Imagem de fundo da hero
└── README.md              # Este arquivo
```

---

## 📹 Demonstração em Vídeo

Vídeo apresentando o funcionamento do bot, simulações e interação com o fã:  
📺 *[Link do YouTube aqui em breve]*

---

## 📬 Contato

Desenvolvido por [Seu Nome]  
[LinkedIn ou GitHub aqui]  
Candidato à vaga de Assistente de Engenharia de Software – FURIA Tech

---

## ⚠️ Observações

- Este projeto é voltado para fins demonstrativos no processo seletivo da FURIA Tech.
- Nenhuma das informações simuladas (como partidas) representa dados oficiais em tempo real.

#GOFURIA 💥
