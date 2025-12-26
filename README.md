# 📝 Task Manager App

> Uma aplicação Fullstack robusta para gerenciamento de tarefas, desenvolvida com foco em arquitetura MVC, segurança e experiência do usuário (UX).

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Concluído-green)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)
![Flask Version](https://img.shields.io/badge/Flask-3.1.1-lightgrey)

## Sobre o Projeto

Este projeto consiste em um sistema completo de gerenciamento de tarefas (To-Do List). O objetivo principal não foi apenas criar um CRUD, mas sim estruturar uma aplicação escalável que integrasse um **Backend sólido em Python (Flask)** com um **Frontend dinâmico e responsivo**.

Diferente de abordagens tradicionais que recarregam a página a cada ação, este projeto utiliza **JavaScript Puro (Vanilla JS) e Fetch API** para comunicação assíncrona, garantindo que a interface seja fluida e moderna.

### Destaques Técnicos
* **Arquitetura Modular:** Utilização de **Flask Blueprints** para separar rotas de autenticação (`auth_routes`) e lógica de negócios (`tasks_routes`), facilitando a manutenção.
* **ORM & Database:** Integração com **MySQL** via **SQLAlchemy**, garantindo modelagem de dados eficiente e prevenção contra SQL Injection.
* **Segurança:** Gerenciamento de sessões com **Flask-Login** e proteção de credenciais sensíveis via variáveis de ambiente (`python-dotenv`).
* **Frontend Async:** Manipulação do DOM e requisições HTTP via `fetch`, proporcionando uma experiência de usuário (UX) sem "flicker" (recarregamento de página).

---

## Tecnologias Utilizadas

**Backend**
* **Python 3**
* **Flask 3.1.1** (Framework Web)
* **Flask-Login** (Gestão de Sessões/Auth)
* **SQLAlchemy & PyMySQL** (ORM e Driver MySQL)
* **Werkzeug** (Segurança e Hash de senhas)
* **Python-Dotenv** (Gerenciamento de variáveis de ambiente)

**Frontend**
* **HTML5 & CSS3** (Design Responsivo)
* **JavaScript (ES6+)** (Fetch API, Manipulação de DOM)
* **Jinja2** (Template Engine)

---

## Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente.

### 1. Clone o repositório
```bash
git clone [https://github.com/MaiconMaciel/task-manager](https://github.com/MaiconMaciel/task-manager)
cd task-manager
```

### 2. Configure o Ambiente Virtual

Recomendado para isolar as dependências do projeto.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```
### 4. Configuração do Banco de Dados (.env)

Este projeto utiliza variáveis de ambiente para segurança.

```bash
Crie um banco de dados no seu MySQL (ex: tasks_db).

Crie um arquivo chamado .env na raiz do projeto.

Adicione a string de conexão seguindo o modelo:

# Exemplo de arquivo .env
DATABASE_URI=mysql+pymysql://seu_usuario:sua_senha@localhost/tasks_db
SECRET_KEY=uma_chave_secreta_muito_segura
```
### 5. Inicialize o Banco de Dados
Execute o script para criar as tabelas definidas nos Models.

```bash

python create_db.py

```
### 6. Execute a Aplicação
```bash
flask run
Acesse no seu navegador: http://127.0.0.1:5000
```

### Funcionalidades
    [x] Autenticação: Cadastro e Login de usuários (senhas hashadas).

    [x] Dashboard Pessoal: Cada usuário vê apenas suas próprias tarefas.

    [x] CRUD Completo: Criar, Ler, Atualizar e Deletar tarefas.

    [x] Status Dinâmico: Marcar tarefas como concluídas/pendentes sem recarregar a página.

    [x] Design Responsivo: Adaptável para mobile e desktop.

### Aprendizados e Desafios
Este projeto marca uma etapa importante no meu desenvolvimento como desenvolvedor Fullstack. O maior desafio foi orquestrar a comunicação entre o Fetch API no cliente e as rotas do Flask no servidor, garantindo que o estado da aplicação se mantivesse consistente no banco de dados MySQL.

A estrutura de pastas foi pensada para simular um ambiente de produção real, separando models, routes, templates e static files.

### Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar Pull Requests.