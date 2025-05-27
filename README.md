Sistema de Gerenciamento de Tarefas com Flask e MySQL


Projeto web full-stack para gerenciar tarefas pessoais, desenvolvido com Flask no backend e MySQL como banco de dados.
Permite aos usuários registrar-se, fazer login, criar, editar, concluir e excluir tarefas, com segurança e controle de acesso. A interface é simples, responsiva e interativa, usando JavaScript para comunicação assíncrona com o backend.

Funcionalidades

    Cadastro e autenticação de usuários (com Flask-Login)
    CRUD (Create, Read, Update, Delete) completo para tarefas
    Marcar tarefas como concluídas ou pendentes
    Interface amigável e responsiva
    Validação e tratamento de erros no frontend e backend
    Requisições assíncronas com fetch API para melhor UX

Tecnologias Utilizadas

    Python 3.x
    Flask
    Flask-Login
    SQLAlchemy
    MySQL (via PyMySQL)
    HTML, CSS, JavaScript (fetch API)

Instalação

Clone o repositório:

    git clone https://github.com/MaiconMaciel/task-manager
    cd task-manager

Crie e ative um ambiente virtual (recomendado):

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

Instale as dependências:

    pip install -r requirements.txt

Configure o banco de dados MySQL:

    Crie um banco de dados no MySQL (exemplo: tasks_db)
    Configure o arquivo de configuração do Flask (app/__init__.py) com a URI do banco, por exemplo:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost/tasks_db'

Inicialize o banco de dados:

    cd task-manager
    python create_db.py

Como usar

    Execute a aplicação:
    flask run
    acesse o ip.

Cadastre um usuário, faça login e comece a criar, editar, concluir ou remover suas tarefas.

Contribuição

Contribuições são bem-vindas!
Esse é meu primeiro projeto de larga escala, a junção de diversas bibliotecas, funções e arquivos foram um desafio e tanto, mas persistência é tudo.
Faça um fork do projeto, crie sua branch, faça as alterações e envie um pull request.
