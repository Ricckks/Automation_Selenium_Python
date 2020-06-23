from selenium import webdriver

driver = webdriver.Chrome ("C:\\Users\\ricardo.assis\\PycharmProjects\\Python\\chromedriver_win32\\chromedriver.exe")


#Cenário 1 - Acesso ao Site

driver.get("https://www.americanas.com.br/")

#Cenário 2 - Login

#Clicar no menu fazer login/Cadastro
driver.find_element_by_xpath("/html/body/div[3]/header/div[2]/div[2]/div[1]/div[3]/span[1]/div").click()

#Clicar no botão "Fazer Login"
driver.find_element_by_xpath("/html/body/div[3]/header/div[2]/div[2]/div[1]/div[3]/span[2]/div/a[1]").click()

#Cenário 3 - Preenchendo apenas o campo "E-mail" e clicando no botão "Contnuar"

#Preencher apenas o campo "E-mail"
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/label[1]/input").send_keys("Teste001")

#Clicar no botão "Continuar"
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/button")

driver.back()

#Cenário 4 - Preenchendo os campos "E-mail", "Senha" e clicando no botão "Continuar"
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/label[1]/input").send_keys("Teste001")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/label[2]/div/input").send_keys("TesteSenha001")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/button")

driver.implicitly_wait(5)
