from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

WORDSEARCH = 'Kawaki' 

@given(u'que um colaborador está logado no sistema')
def stepLoginBackoffice(context):
    wait = WebDriverWait(context.browser, 10)
    
    indexLogin = wait.until(EC.url_to_be('https://projetofinal.jogajuntoinstituto.org/'))
    assert indexLogin, "Página não encontrada" 

    context.browser.find_element(By.NAME, "email").send_keys("teste1807@gmail.com") 
    context.browser.find_element(By.NAME, "password").send_keys("1807")
    context.browser.find_element(By.TAG_NAME,'form').submit()

   
@when(u'clicar na opção de filtro com o nome "{categorias}"')
def stepFilter(context, categorias):
   
    wait = WebDriverWait(context.browser, 10)
    backoffice = wait.until(EC.url_contains('products'))
    assert backoffice, "Acesso Negado" 

    listTotal = context.browser.find_elements(By.CLASS_NAME, "contentList")
    indexList = 0
    for index,list in enumerate(listTotal): 
        if list.text == categorias:
            indexList = index
            break

    listTotal[indexList].click()
    
   
   
@when(u'pesquisar um produto cadastrado') 
@when(u'pesquisar um produto existente')
def stepSearch(context):
    wait = WebDriverWait(context.browser, 10)
    backoffice = wait.until(EC.url_contains('products'))
    assert backoffice, "Acesso Negado" 

    inputSearch = context.browser.find_element(By.XPATH,"//*[@id='root']/header/section[2]/nav/ul/div[1]/input")
    inputSearch.send_keys(WORDSEARCH)
    
@then(u'um ou mais produtos serão exibidos')
@then(u'os produtos serão exibidos')
def stepPrintResultSearch(context):
    time.sleep(5)
    
    h1Total = context.browser.find_elements(By.TAG_NAME,"h1")
  
    find = False
    for h1 in h1Total:
        
        if WORDSEARCH in h1.text:
          find = True
          break
  
    if not find:
        spanTotal = context.browser.find_elements(By.TAG_NAME,"span")
        
        for span in spanTotal:
            if WORDSEARCH in span.text:
                find = True
                break

    assert find, "produto não encontrado"
    time.sleep(5)