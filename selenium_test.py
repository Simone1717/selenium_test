from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Imposta il driver di Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Apri Google
    driver.get('https://www.google.com')

    # Attesa esplicita per il caricamento del pulsante di accettazione dei cookie su Google
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))
    ).click()

    # Naviga sul sito specificato
    driver.get('https://iisbadoni.edu.it/')

    # Attesa esplicita per il caricamento del pulsante di accettazione dei cookie sul sito specificato
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'cookiescript_accept'))
    ).click()

    # Naviga alla pagina specificata
    driver.get('https://iisbadoni.edu.it/istituto-2/istituto/')

    # Attesa esplicita per il caricamento della pagina
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Istituto")]'))
    )

    # Mantiene aperta la finestra del browser per ispezione manuale
    input("Premi invio per chiudere il browser...")

finally:
    # Chiudi il browser
    driver.quit()
