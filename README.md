# baygon_inventory


![GitHub repo size](https://img.shields.io/github/repo-size/anniellecrispim/baygon_inventory?style=for-the-badge)
![PYTHON](https://img.shields.io/badge/Python-%203.12.4%20-blue?style=for-the-badge&logo=python)
![GitHub forks](https://img.shields.io/github/forks/anniellecrispim/baygon_inventory?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/anniellecrispim/baygon_inventory?style=for-the-badge)
![LICENCE](https://img.shields.io/github/license/anniellecrispim/baygon_inventory?style=for-the-badge)



<img src="logo.png" alt="Logo Squad Baygon">


> Este é a última avaliação do Instituto Joga Junto do módulo Avançado, onde este repositório é apenas um dos artefados usados para a entrega final.

##  Sobre o Projeto

Esse  projeto automatiza testes para o sistema de controle de estoque do Instituto Joga Junto, usando Selenium, Behave e um ambiente virtual utilizando a linguagem Python.


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
```

## 🤝 Squad Baygon

Agradecemos imensamente as pessoas que fizeram esse projeto acontecer: o nosso querido **Squad Baygon Quality** e ao Instituto Joga Junto pela oportunidade.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/anniellecrispim" title="GitHub da Annielle">
        <img src="https://avatars.githubusercontent.com/anniellecrispim" width="100px;" alt="Foto da Annielle Crispim no GitHub"/><br>
        <sub>
          <b>Annielle Crispim</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/caiobarreto0" title="GitHub do Caio">
        <img src="https://avatars.githubusercontent.com/caiobarreto0" width="100px;" alt="Foto do Caio Barreto no GitHub"/><br>
        <sub>
          <b>Caio Barreto</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/juliarobaina" title="GitHub da Julia">
        <img src="https://avatars.githubusercontent.com/juliarobaina" width="100px;" alt="Foto da Julia Robaina no GitHub"/><br>
        <sub>
          <b>Julia Robaina</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Vitor-Back" title="GitHub do Vitor">
        <img src="https://avatars.githubusercontent.com/Vitor-Back" width="100px;" alt="Foto do Vitor Back no GitHub"/><br>
        <sub>
          <b>Vitor Back</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/tamiresana" title="GitHub da Tamires">
        <img src="https://avatars.githubusercontent.com/tamiresana" width="100px;" alt="Foto da Tamires Ana no GitHub"/><br>
        <sub>
          <b>Tamires Ana</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 😄 Sobre o Instituto 

O Instituto Joga Junto é uma organização que promove oportunidades de desenvolvimento por meio da educação e formação profissional. Eles oferecem tutoria gratuita no modo 'estudo aberto', com turmas selecionadas e pequenas,  focando no treinamento em áreas de tecnologia, com o objetivo de capacitar pessoas e abrir novas perspectivas de carreira. O Instituto também se dedica a projetos sociais que buscam transformar vidas através do conhecimento e da inclusão social. E o mais importante: **Jogar Junto!**

### Trilha Tripp 

Além de estamos na trilha de capacitação de QA (Quality Assurance), estamos no módulo avançado com direito a treinameto com Python e testes automatizados. Além de testes de API.

### Avaliadores Projeto final

Nossos avaliadores do Projeto Final

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/MatheusGeambastiane" title="Foto do Matheus">
        <img src="https://avatars.githubusercontent.com/MatheusGeambastiane" width="100px;" alt="Foto da Matheus Geambastiane no GitHub"/><br>
        <sub>
          <b>Matheus Geambastiane</b>
        </sub>
      </a>
    </td>
 <td align="center">
      <a href="https://www.linkedin.com/in/rfdsouza/" title="Perfil do Trem Desgovernado no LinkedIn">
      <img src="https://media.licdn.com/dms/image/D5603AQFcxhQs4grslw/profile-displayphoto-shrink_800_800/0/1684419656473?e=1726099200&v=beta&t=OWwNILbsFDSpV3u-AIIlQpKp_8fTzt_xNH89i8XLzCE" width="100px;" alt="Foto do Trem Desgovernado no LinkedIn"/><br>
     <sub>
       <b>Renato Souza</b>
     </sub>
   </a>
 </td>
  <td align="center">
      <a href="" title="">
        <img src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" width="100px;" alt=""/><br>
        <sub>
          <b>Edson</b>
        </sub>
      </a>
    </td>
<table>
