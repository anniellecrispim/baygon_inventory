from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given('que estou na página do Instituto Joga Junto') 
def acessar_pagina(context):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    titulo_pagina = context.browser.title
    assert 'Joga Junto' in titulo_pagina, "Título da página não encontrado (esperava 'Joga Junto')"

@when('faço login')
def login(context):
    context.browser.find_element(By.XPATH, '//*[@id="mui-1"]').send_keys("teste12@gmail.com")
    context.browser.find_element(By.XPATH, '//*[@id="outlined-adornment-password"]').send_keys("1234")
    context.browser.find_element(By.XPATH, '//*[@id="root"]/main/form/button').click()

@when('cadastro um produto') 
def cadastro_produto(context):
    wait = WebDriverWait(context.browser, 10)
    
    # Clicar no botão para adicionar produto
    adicionar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/header/section[2]/div/header/button')))
    adicionar_btn.click()
    
    
    # Preencher os campos do formulário
    context.browser.find_element(By.XPATH, '//*[@id="mui-2"]').send_keys("Tenis Rock And Roll")
    context.browser.find_element(By.XPATH, '//*[@id="mui-3"]').send_keys("Viva ao Rock")
    context.browser.find_element(By.XPATH, '//*[@id="radix-6"]/form/div[3]/div/label[1]').click()
    context.browser.find_element(By.XPATH, '//*[@id="mui-4"]').send_keys("139.90")
    context.browser.find_element(By.NAME, 'image').send_keys(r'C:\Users\caiob\OneDrive\Área de Trabalho\Imagens backoffice ijj\tenis_rock.jpeg')
    context.browser.find_element(By.XPATH, '//*[@id="mui-6"]').send_keys("41194-105")
    

    
@then('o produto é cadastrado com sucesso') 
def produto_cadastrado(context):
    context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/button').submit()
   
    
    
   
    


   



