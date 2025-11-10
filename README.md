
# Login e Cadastro

O presente projeto tem como finalidade demonstrar conhecimento básico em Algoritmo e Lógica de programação.

O aplicativo conta com uma API feita em RapidAPI, em python. E um frontend feito em HTML e css.

## Como Rodar

Dentro da raiz do projeto crie um ambient virtual para as dependências do projeto:

```bash
  python -m venv ./venv
```

### Ative o script do ambiente virtual.

#### Linux:

```bash
  source  raiz_do_projeto\Scripts\activate
```

#### Windows (cmd):

```cmd
    raiz_do_projeto\Scripts\activate.ps1
```

#### Windows (Git Bash):

```cmd
   source raiz_do_projeto\Scripts\activate.ps1
```

### Baixe as dependências

```cmd
   pip install -r requirements.txt
```
### Execute o servidor


```cmd
   uvicorn app:app --reload
```


## Backend:

- Dotenv

- Pytest

- RapidAPI

- blake2b (hashlib)


## Frontend:

- HTML

- css

- Google Fonts

- Figma


## Tests Unitários:

```cmd
   pytest -q
```
