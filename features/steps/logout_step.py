from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


@given('que um colaborador está logado no Backoffice')
def step_given_colaborador_logado(context):
    context.browser.find_element(By.NAME, 'email').send_keys('teste12@gmail.com')
    context.browser.find_element(By.NAME, 'password').send_keys('1234')
    context.browser.find_element(By.XPATH, '/html/body/div/main/form/button').click()
    

@when('clicar no botão de perfil ou passar o ponteiro do mouse sobre o botão')
def step_when_passar_mouse_botao_perfil(context):
    time.sleep(5)
    context.browser.find_element(By.XPATH, '//*[@id="radix-7-trigger-radix-0"]').click()
    

@when('clicar na opção de logout')
def step_when_clicar_opcao_logout(context):
    logout_option = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//p[text()="Sair"]'))
    )
    logout_option.click()    
    
@then('o colaborador é direcionado para a página de login')
def step_then_redirecionado_pagina_login(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    assert context.browser.current_url == 'https://projetofinal.jogajuntoinstituto.org/'
    
    time.sleep(3)