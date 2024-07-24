# baygon_inventory

Este projeto automatiza testes para o sistema de controle de estoque do Instituto Joga Junto, usando Selenium, Behave e um ambiente virtual utilizando a linguagem Python.

## Tecnologias Utilizadas

- **Selenium**: Automação do navegador e interação com a interface web.
- **Behave**: Testes de aceitação com Gherkin.
- **Ambiente Virtual Python**: Isolamento das dependências do projeto.

## Funcionalidades Testadas

- **Login/Logout**: Verifica a funcionalidade de login e logout.
- **Cadastro de Produto**: Testa o processo de adição de novos produtos.
- **Pesquisa de Produto**: Valida a funcionalidade de busca.
- **Filtragem de Produtos**: Verifica a capacidade de filtrar produtos.

## Configuração do Ambiente

1. **Criação do Ambiente Virtual**

    ```sh
    python -m venv venv
    ```

2. **Ativação do Ambiente Virtual**

    - No Windows:

        ```sh
        venv\Scripts\activate
        ```

    - No Linux/Mac:

        ```sh
        source venv/bin/activate
        ```

3. **Instalação das Dependências**

    ```sh
    pip install -r requirements.txt
    ```

## Dependências

Veja o arquivo `requirements.txt` para as bibliotecas necessárias.

### Principais Imports

```python
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time