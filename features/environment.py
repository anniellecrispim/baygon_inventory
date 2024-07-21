from selenium.webdriver import Firefox

def before_scenario(context, scenario):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')


def after_scenario(context, scenario):
    context.browser.quit()

