from selenium.webdriver import Firefox

#antes de cada cenário
def before_scenario(context, scenario):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')

#depois de cada cenário
def after_scenario(context, scenario):
    context.browser.quit()

