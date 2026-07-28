# 🚀 Espaço Viagem

Bem-vindo ao **Espaço Viagem**! Um portal educacional interativo desenvolvido para estudantes e entusiastas de astronomia. Nosso objetivo é descomplicar a ciência espacial unindo imagens em alta definição e dados curiosos sobre o nosso sistema solar de forma rápida e acessível.

## 🎯 O Projeto
Este projeto foi construído focando na simplicidade e na performance, com entrega em **GitHub Pages**. Através dele, conectamos os usuários ao cosmos utilizando dados abertos e uma interface limpa.

**Público-alvo:** Estudantes de Astronomia de todas as idades.

## ✨ Funcionalidades Principais
* **Vitrine do Cosmos:** Exibição da Imagem Astronômica do Dia (APOD) fornecida pela API oficial da NASA.
* **Enciclopédia Planetária:** Textos explicativos e curiosidades sobre os planetas, alimentados por raspagem de dados (*web scraping*) da Wikipedia.
* **Radar de Asteroides:** Um painel simples listando os asteroides mais próximos da Terra no dia atual.

## 🛠️ Tecnologias Utilizadas
* **Backend / Lógica:** Python e [FastHTML](https://fastht.ml/)
* **Frontend:** HTML5 e CSS3 (puro)
* **Integração de Dados:** NASA API (REST) e Web Scraping (Wikipedia)
* **Persistência:** SQLite local
* **Hospedagem:** GitHub Pages

## 🔐 Fluxo de Login e Administração
O projeto agora possui um fluxo simples de autenticação com SQLite.

### Usuário administrador
* Usuário: `admin`
* Senha: `admin123`

Ao fazer login com o usuário administrador, o sistema abre o painel administrativo, onde é possível:
* criar novos usuários
* remover usuários cadastrados
* visualizar a lista de usuários existentes

### Cadastro de usuários
* A tela inicial possui um link para criar conta
* O cadastro cria um novo usuário no banco SQLite
* Se o nome já existir, a criação é rejeitada com mensagem de erro

### Banco de dados
* O banco utilizado é o SQLite, armazenado localmente no arquivo `espaco_viagem.db`
* A tabela `users` guarda os registros de usuário com `id`, `username` e `password_hash`

## 📂 Estrutura do Projeto (Arquitetura MVC)
Para manter o código organizado e facilitar o trabalho em equipe, adotamos o padrão **MVC (Model-View-Controller)**. 

```text
espaco-viagem/
│
├── models/         # (MODEL) Lógica de Dados 
│   ├── nasa_api.py # Conexão e consumo da API da NASA
│   └── wiki_bot.py # Script de web scraping da Wikipedia
│
├── views/          # (VIEW) Interface do Usuário
│   ├── static/     # Arquivos estáticos (CSS, imagens locais)
│   ├── home.py     # Componentes visuais da página inicial
│   └── radar.py    # Componentes visuais da tela de asteroides
│
├── controllers/    # (CONTROLLER) Regras de Negócio e Rotas
│   └── main.py     # Arquivo principal do FastHTML (gerencia as URLs)
│
└── README.md       # Documentação do projeto
