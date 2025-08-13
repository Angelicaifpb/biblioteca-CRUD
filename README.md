# Biblioteca

Este projeto é uma aplicação web simples para gerenciar uma biblioteca, permitindo o cadastro e gerenciamento de autores e livros.

## Entidades

- **Autor**
  - `id`: Identificador único do autor.
  - `nome`: Nome do autor.
  - `nacionalidade`: Nacionalidade do autor.
  - `data_nascimento`: Data de nascimento do autor.

- **Livro**
  - `id`: Identificador único do livro.
  - `titulo`: Título do livro.
  - `ano_publicacao`: Ano de publicação do livro.
  - `autor_id`: Identificador do autor associado ao livro.

## Relacionamento

Um livro pertence a um autor, e um autor pode ter vários livros.

### Como executar o projeto
1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    venv/Scripts/activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Executar o script `run.py`
```
python run.py
```
