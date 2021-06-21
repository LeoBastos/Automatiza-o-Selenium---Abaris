import os
from selenium import webdriver
from time import sleep
import getpass
from datetime import date

"""
LOGIN
"""
username = input("Usuário: ")
password = getpass.getpass(prompt='Senha: ', stream=None)
sleep(1)

"""
ESCOLHA
"""
print('***************************************************')
print('Escolha o Tipo de Documento: ')
print('1 - Análise Curricular')
print('2 - Aproveitamento de estudos')
print('***************************************************')

escolha = input('Digite o Documento: ')

if escolha == '1':
    resultado = '/html/body/div[34]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/span'
    sleep(2)

elif escolha == '2':
    resultado = '/html/body/div[34]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/span'
    sleep(2)
else:
    print('Atividades Complementares')

"""
SETUP INICIAL
"""
data_atual = date.today()
data_em_texto = 'Volta Redonda, ' + data_atual.strftime('%d/%m/%Y')
url = "https://###########.br/"
driver = webdriver.Chrome('C:\\Users\\LeO\\Desktop\\Abaris\\chromedriver.exe')
driver.get(url)
sleep(1)

#EFETUAR O LOGIN
print('Efetuando Login!')
driver.find_element_by_id('usuario').send_keys(username)
driver.find_element_by_id('senha').send_keys(password)
sleep(1)
driver.find_element_by_id('btn-acessar').click()
sleep(3)
print('login efetuado com sucesso!')
sleep(3)
print('Aguarde....')
sleep(3)
print('Aguarde....')
sleep(6)


#LIMPAR O OVERLAY
driver.find_element_by_class_name('overlay-novo-link').click()
print('Aguarde...')
sleep(1)
driver.find_element_by_class_name('overlay-novo-link').click()
print('Aguarde...')
sleep(1)
driver.find_element_by_class_name('overlay-novo-link').click()
print('Aguarde...')
print('Overlay Limpo')
sleep(2)


#CLICAR NA PESQUISA
print('Selecionar Pesquisa')
driver.find_element_by_xpath('/html/body/section[3]/section/div/div/div/section[1]/div/ol/li[1]/a/i').click()
sleep(5)

#SELECIONANDO GRUPO DE TIPO DE DOCUMENTOS - ALUNOS
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article/div/div[3]/form/div[1]/div/section[1]/div[1]/select/option[4]').click()
print('PASTA: Alunos, selecionado!')
sleep(3)

#SELECIONAR O TIPO DE DOCUMENTO
print('Selecionando: Documento')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article/div/div[3]/form/div[1]/div/section[1]/div[2]/div/div/div[1]/div').click()
sleep(3)

print('Selecionar Documento')
driver.find_element_by_xpath(resultado).click()
sleep(3)
print('Botão Confirmar')
driver.find_element_by_xpath('/html/body/div[34]/div/div[2]/div/div[2]/div[1]/div/div').click()
sleep(1)
print('Aguarde...')
sleep(2)

#FILTRAGEM DA BUSCA
print('Desmarcar checkbox: Assinados')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article/div/div[3]/form/div[1]/div/section[1]/div[3]/input[1]').click()
sleep(1)
print('Aguarde...')
sleep(2)

#CLICANDO PARA ASSINAR
print('Clicando em: Assinatura')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article/div/div[3]/sidebar/div[1]/div/ol/li[5]/a').click()
print('Aguarde...')
sleep(10)

print('Selecionando Institucional')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article[2]/div/div[3]/form/div[1]/div/div[2]/ul/li[2]/input').click()

sleep(2)

print('Selecionando CONSAE')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article[2]/div/div[3]/form/div[1]/div/div[4]/select/option[2]').click()
sleep(2)

print('Colocando a Senha')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article[2]/div/div[3]/form/div[1]/div/div[5]/input').send_keys(password)
sleep(2)

print('Preenchendo a Data')
driver.find_element_by_xpath('/html/body/section[3]/section/div[2]/div[2]/article[2]/div/div[3]/form/div[1]/div/div[6]/input').send_keys(data_em_texto)
sleep(2)

print('FIM')