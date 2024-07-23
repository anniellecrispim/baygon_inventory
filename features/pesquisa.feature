Feature: Pesquisar Produto por Nome ou Descrição

    COMO colaborador 
    EU QUERO encontrar um ou mais produtos 
    PARA encontrar mais rapidamente os produtos

    #Happy Scenarios
    
    Background:
        Given que um colaborador está logado no sistema
        
   
    Scenario: C14
        When pesquisar um produto cadastrado
        Then um ou mais produtos serão exibidos
        
    Scenario Outline: C15
        When clicar na opção de filtro com o nome "<categorias>"
        And pesquisar um produto existente
        Then os produtos serão exibidos
        Examples:
            |categorias|
            |Todos|
            |Roupas|
            |Calçados|
            |Acessórios|