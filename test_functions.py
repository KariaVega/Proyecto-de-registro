from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ruta del controlador, por ejemplo ChromeDriver
driver = webdriver.Chrome(executable_path='ruta/al/chromedriver')

try:
    # Abre el formulario
    driver.get('ruta/a/formulario.html')  # Cambia a la ruta local del archivo HTML

    # Encuentra los elementos del formulario y rellena cada campo
    driver.find_element(By.ID, "nombre").send_keys("Juan Pérez")
    driver.find_element(By.ID, "email").send_keys("juan.perez@example.com")
    driver.find_element(By.ID, "telefono").send_keys("1234567890")
    driver.find_element(By.ID, "fechaNacimiento").send_keys("2000-01-01")
    
    # Selecciona una opción del menú desplegable de grado
    grado = driver.find_element(By.ID, "grado")
    for option in grado.find_elements(By.TAG_NAME, "option"):
        if option.text == "Primero":
            option.click()
            break

    # Verifica que todos los campos están correctamente llenados
    assert driver.find_element(By.ID, "nombre").get_attribute("value") == "Juan Pérez"
    assert driver.find_element(By.ID, "email").get_attribute("value") == "juan.perez@example.com"
    assert driver.find_element(By.ID, "telefono").get_attribute("value") == "1234567890"
    assert driver.find_element(By.ID, "fechaNacimiento").get_attribute("value") == "2000-01-01"
    assert grado.get_attribute("value") == "primero"

    # Envía el formulario
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Pausa para ver el resultado (opcional)
    time.sleep(2)

finally:
    # Cierra el navegador
    driver.quit()
