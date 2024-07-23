
Feature: Login 
    COMO colaborador
    EU QUERO fazer login no backoffice 
    PARA QUE eu possa gerenciar o estoque do e-commerce

    #Utilizado para colocar os passos que são iguais a vários cenários
    Background: 
        Given que o usuário está na página de login
    
    # "" - para adicionar parâmetros e incluir valores
    Scenario: C1
        When o usuário inserir "teste1807@gmail.com" e "1807" válidos 
        And se autenticar
        Then o usuário será redirecionado para a página inicial do sistema
    
    #Scenario Outline - utilizado para realizar vários testes no mesmo cenário com valores diferentes
    #Scenario Outline - utilizado também para transformar cenários semelhantes em um
    Scenario Outline: C2
        When o usuário inserir "<email>" ou "<password>" inválido
        And  o usuário clicar no botão de login
        Then o usuário permanece na página de login

        Examples:
            | email | password |
            | teste1807@gmail.com | 123456 |
            | narutohokage@gmail.com | 1807 |