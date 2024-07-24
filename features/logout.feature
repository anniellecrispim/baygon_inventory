# language: pt

Funcionalidade: Logout C10
  Cenário: O sistema deve ter um botão para deslogar o usuário do sistema

  COMO colaborador 
  EU QUERO sair do sistema 
  PARA QUE eu encerre minha sessão
  
  Dado que um colaborador está logado no Backoffice
  Quando clicar no botão de perfil ou passar o ponteiro do mouse sobre o botão
  E clicar na opção de logout
  Então o colaborador é direcionado para a página de login