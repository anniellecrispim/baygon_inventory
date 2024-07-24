from selenium import webdriver

def before_all(context):
    """
    Inicializa o navegador antes de todos os testes.

    Args:
        context (behave.runner.Context): O contexto da execução do teste, onde o navegador é armazenado.
    """
    context.browser = webdriver.Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    context.browser.implicitly_wait(10)


def after_all(context):
    """
    Encerra o navegador após todos os testes.

    Args:
        context (behave.runner.Context): O contexto da execução do teste, onde o navegador é armazenado.
    """
    context.browser.quit()
