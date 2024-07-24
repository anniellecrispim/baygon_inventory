Feature: Cadastro de produto

  Scenario: Envio de dados para cadastro de produto
    Given que estou na página do Instituto Joga Junto
    When faço login
    And cadastro um produto
    Then o produto é cadastrado com sucesso
