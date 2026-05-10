from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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
    espera.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-page")))
    elemento.click()
    espera.until(EC.presence_of_element_located((By.CLASS_NAME, "courses-section__courses")))
    i3 = 0
    while True:
            pai = navegador.find_element(By.CLASS_NAME, "courses-section__courses")
            elementos = pai.find_elements(By.CLASS_NAME, "card-course")
            if i3 >= len(elementos):
                break
            item = elementos[i3]
            navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", item)
            time.sleep(1)
            navegador.execute_script("arguments[0].click();", item)
            espera.until(EC.presence_of_element_located((By.CLASS_NAME, "welcome-container")))
            try:
                botao=WebDriverWait(navegador,10).until(EC.element_to_be_clickable((By.XPATH,"//button[.//h3[normalize-space()='MATERIAIS DE ESTUDOS']]")))
            except:
                print("MATERIAIS DE ESTUDOS não encontrado")
                navegador.back()
                espera.until(EC.presence_of_element_located((By.CLASS_NAME,"courses-section__courses")))
                i3+=1
                continue
            navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
            time.sleep(1.4)
            botao.click()
            pai = navegador.find_element(By.CLASS_NAME, "draggable")
            filho = pai.find_elements(By.TAG_NAME, "a")
            for i in range(len(filho)):
                pai = navegador.find_element(By.CLASS_NAME, "draggable")
                filho = pai.find_elements(By.TAG_NAME, "a")
                try:
                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", filho[i])
                    espera.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-page")))
                    pai = navegador.find_element(By.CLASS_NAME, "draggable")
                    filho = pai.find_elements(By.TAG_NAME, "a")
                    time.sleep(1.5)
                    navegador.execute_script("arguments[0].click();", filho[i])
                except IndexError:
                    print("DEU ERRO")
                    break
                time.sleep(1)
                clicados = set()
                tentativas_sem_novos = 0
                while True:
                    botao_marcar = navegador.find_elements(By.CLASS_NAME, "mark-progress__button")
                    novos = 0
                    for i2 in range(len(botao_marcar)):
                        botao_marcar = navegador.find_elements(By.CLASS_NAME, "mark-progress__button")
                        if i2 >= len(botao_marcar):
                            break
                        button = botao_marcar[i2]
                        try:
                            identificador = button.id
                            if identificador in clicados:
                                continue
                            classes = button.get_attribute("class").split()
                            if "mark-progress__button--marked" not in classes:
                                navegador.execute_script("arguments[0].click();", button)
                            clicados.add(identificador)
                            novos += 1
                        except:
                            pass
                    referencia=navegador.find_elements(By.CLASS_NAME,"topic-references")
                    if referencia:
                        try:
                            navegador.execute_script("arguments[0].scrollIntoView({block:'end'});",referencia[0])
                            time.sleep(1)
                            posicao_referencia=referencia[0].location['y']
                            scroll_atual=navegador.execute_script("return window.pageYOffset+window.innerHeight")
                            if scroll_atual>=posicao_referencia:
                                botoes_finais=navegador.find_elements(By.CLASS_NAME,"mark-progress__button")
                                for botao_final in botoes_finais:
                                    try:
                                        classes=botao_final.get_attribute("class").split()
                                        if"mark-progress__button--marked"not in classes:
                                            navegador.execute_script("arguments[0].click();",botao_final)
                                    except:
                                        pass
                                break
                        except:
                            pass
                    navegador.execute_script("window.scrollBy(0,1200)")
                    time.sleep(1)
                voltar = navegador.find_element(By.CLASS_NAME, "mr-2")
                voltar.click()
                espera.until(EC.presence_of_element_located((By.CLASS_NAME, "draggable")))
                time.sleep(1)
            navegador.execute_script("window.scrollTo(0, 0)")
            time.sleep(1)
            voltar = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, "mr-2")))
            navegador.execute_script("arguments[0].click();", voltar)
            espera.until(EC.presence_of_element_located((By.CLASS_NAME, "courses-section__courses")))
            time.sleep(1.5)
            i3 += 1

rodar("111202022", "Matheusrr01@")
#abas = navegador.window_handles
#navegador.switch_to.window(abas[0])