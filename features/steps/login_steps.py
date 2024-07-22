from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

@given(u'que o usuário está na página de login')
def stepLoginPage(context):
    wait = WebDriverWait(context.browser, 10)
    
    indexLogin = wait.until(EC.url_to_be('https://projetofinal.jogajuntoinstituto.org/'))
    assert indexLogin == True, "Página não encontrada" 

#para pegar os valores que estão no .feature
@when(u'o usuário inserir "{email}" e "{password}" válidos')
@when(u'o usuário inserir "{email}" ou "{password}" inválido')
def stepFillInputs(context, email, password):
    context.browser.find_element(By.NAME, "email").send_keys(email) 
    context.browser.find_element(By.NAME, "password").send_keys(password)
    
@when(u'se autenticar')
@when(u'o usuário clicar no botão de login')
def stepLogin(context):
    context.browser.find_element(By.TAG_NAME,'form').submit()

@then(u'ele será redirecionado para a página inicial do sistema')
def stepIndexBackoffice(context):
    wait = WebDriverWait(context.browser, 10)
    #url_contains -> retorna true se a url atual tem a string que eu estou passando
    backoffice = wait.until(EC.url_contains('products'))
    assert True == backoffice, "Acesso Negado" #se der problema aqui não fecha a janela
    time.sleep(3)   
    
@then(u'o usuário permanece na página de login')
def stepLoginPage(context):
    
    wait = WebDriverWait(context.browser, 10)
    #url_to_be -> retorna true se a url atual é igual a url que eu estou passando
    indexLogin = wait.until(EC.url_to_be('https://projetofinal.jogajuntoinstituto.org/'))
    assert True == indexLogin, "Não retornou para a página de login" 
    time.sleep(3)   
    
 


