'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 1. Configura e inicializa o navegador (neste caso, o Chrome)
# O ChromeDriverManager baixa e gerencia a versão correta do driver para você.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 2. Navega até a URL desejada
url = 'https://quotes.toscrape.com/js/' # Este site carrega as citações com JavaScript
driver.get(url)

# 3. Opcional: Maximiza a janela do navegador
driver.maximize_window()

# Imprime o título da página para confirmar que funcionou
print(f"O título da página é: {driver.title}")

# 4. É ESSENCIAL fechar o navegador no final para não deixar processos abertos
driver.quit()

'''
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Importações necessárias para as esperas e localização de elementos
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Inicialização do Navegador
print("Iniciando o navegador...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'http://quotes.toscrape.com/js/'
driver.get(url)

dados = []

try:
    print("Aguardando o conteúdo dinâmico carregar...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'quote'))
    )
    print("Conteúdo carregado!")

    #  Coleta dos Dados
    quotes_divs = driver.find_elements(By.CLASS_NAME, 'quote')
    
    print(f"Encontradas {len(quotes_divs)} citações na página.")

    for quote_div in quotes_divs:
        texto = quote_div.find_element(By.CLASS_NAME, 'text').text
        autor = quote_div.find_element(By.CLASS_NAME, 'author').text
        
        dados.append({'Citação': texto, 'Autor': autor})

except Exception as e:
    print(f"Ocorreu um erro durante o scraping: {e}")

finally:
    # Fechamento do Navegado
    print("Fechando o navegador.")
    driver.quit()


# Salvando os Dados 
if dados:
    df = pd.DataFrame(dados)
    df.to_csv('citacoes_dinamicas.csv', index=False, encoding='utf-8')
    print("\n--- Primeiras 5 citações salvas: ---")
    print(df.head())
    print("\nDados salvos com sucesso em 'citacoes_dinamicas.csv'!")



"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Importações essenciais para o modo headless do Firefox
from selenium.webdriver.firefox.options import Options

ff_options = Options()
ff_options.add_argument("--headless") # A linha mais importante!

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ff_options)
print("Driver do Firefox iniciado em modo headless.")

url = 'http://quotes.toscrape.com/js/'
driver.get(url)
print(f"Título da página: {driver.title}")

driver.quit()
"""
