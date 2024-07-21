
Feature: Login 
    COMO colaborador
    EU QUERO fazer login no backoffice 
    PARA QUE eu possa gerenciar o estoque do e-commerce

    Background:
        Given que o usuário está na página de login
        
    Scenario: C1
        When o usuário inserir "email" e "password" válidos 
        And se autenticar
        Then ele será redirecionado para a página inicial do sistema
      

    Scenario Outline: C2
        When o usuário inserir "<email>" ou "<password>" inválidos
        And  o usuário clicar no botão de login
        Then o usuário permanece na página de login

        Examples:
            | email | password |
            | teste1807@gmail.com | 123456 |
            | narutohokage@gmail.com | 1807 |