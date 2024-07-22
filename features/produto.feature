#language: pt

Funcionalidade: Adionar Produto
  Cenário: O sistema deve permitir cadastro de produtos

  COMO colaborador
  EU QUERO cadastrar produtos
  PARA QUE eu possa gerenciar o estoque
  
  Dado que um colaborador está na página de cadastro de produto
  Quando ele preencher os detalhes do produto
  E clicar no botão "Enviar Novo Produto"
  Então o produto deve ser salvo no sistema




