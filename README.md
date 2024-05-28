# FakePinterest

## Descrição

FakePinterest é um site inspirado no Pinterest, mas de forma bem mais básica. O projeto permite a criação e exclusão de usuários e posts, oferecendo uma plataforma simples para compartilhar e gerenciar conteúdo visual.

## Índice

- [Instalação](#instalação)
- [Funcionalidades](#funcionalidades)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Funcionalidades

- Criar, visualizar e excluir posts.
- Gerenciar perfil de usuário, incluindo foto de perfil.
- Navegação intuitiva com barra de navegação responsiva.

## Requisitos

Os requisitos estão listados no arquivo `requirements.txt`.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/RatingTax78753/FakePinterest-Django.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd FakePinterest
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Uso

- Acesse o servidor de desenvolvimento no navegador através de `http://127.0.0.1:8000/`.
- Registre-se ou faça login para começar a usar a plataforma.
- Envie e gerencie seus posts de forma simples e intuitiva.

## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch:

    ```bash
    git checkout -b minha-nova-funcionalidade
    ```

3. Faça suas alterações e adicione commits:

    ```bash
    git commit -m "Adiciona nova funcionalidade"
    ```

4. Envie para o branch original:

    ```bash
    git push origin minha-nova-funcionalidade
    ```

5. Crie uma pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

## Contato

Email: ruanvr2006@gmail.com