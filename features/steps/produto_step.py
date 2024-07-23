from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


@given('que um colaborador está na página de cadastro de produto')
def step_given_jogajunto_page(context):
    context.browser.find_element(By.NAME, 'email').send_keys('teste12@gmail.com')
    context.browser.find_element(By.NAME, 'password').send_keys('1234')
    context.browser.find_element(By.XPATH, '/html/body/div/main/form/button').click()
    
    

@when('ele preencher os detalhes do produto')
def step_when_preencher_detalhes_do_produto(context):
    context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/header/button').click()
    context.browser.find_element(By.NAME, 'name').send_keys('Pantufa')
    context.browser.find_element(By.NAME, 'description').send_keys('Pantufa Garfield 34/36')
    context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[2]').click()
    context.browser.find_element(By.NAME, 'price').send_keys('19,89')
    context.browser.find_element(By.NAME, 'image').send_keys(r'C:\Users\10\Desktop\QA - Avançado\Fotos\Pantufa.jpg')
    context.browser.find_element(By.NAME, 'shipment').send_keys('100,00')
    

@when('clicar no botão "Enviar Novo Produto"')
def step_when_clicar_enviar_novo_produto(context):
    context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/button').submit()
    

@then('o produto deve ser salvo no sistema')
def step_then_produto_deve_ser_salvo(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Produto enviado com sucesso!!')]"))
    )
    assert "Produto enviado com sucesso!!" in context.browser.page_source
    
    