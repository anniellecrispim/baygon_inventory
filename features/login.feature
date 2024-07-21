
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
      

    