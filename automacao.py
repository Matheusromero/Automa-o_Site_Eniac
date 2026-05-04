from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
def rodar(login, senha):
    navegador = webdriver.Chrome()
    espera = WebDriverWait(navegador, 999999)
    navegador.get("https://eniac-edu.grupoa.education/plataforma/auth/signin")
    espera.until(EC.presence_of_element_located((By.ID, "55")))
    navegador.maximize_window()
    navegador.find_element("id", "50").send_keys(login)
    navegador.find_element("id", "55").send_keys(senha)
    navegador.find_element("name", "btn-login").click()
    elemento = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="Disciplinas"]')))
    elemento.click()
    time.sleep(5)

#automacao()
#abas = navegador.window_handles
#navegador.switch_to.window(abas[0])