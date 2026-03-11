from customtkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def cadastro():
    servico= Service(ChromeDriverManager().install())

    navegador= webdriver.Chrome(service=servico)
    #navegador.get(""){abre o site especificado}
    #navegador.find_element('xpath,''){Busca um elemento no site pelo xpath}
    #navegador.find_element().send_keys(''){Escreve no elemento solicitado}
    #navegador.find_element().click(){Clica no elemento solicitado}

    nome= entrada_nome.get().strip
    email= f'{entrada_email.get()}@gmail.com'
    num= entrada_num.get()
    
    navegador.get('https://testautomationpractice.blogspot.com/')
    navegador.find_element('xpath','//*[@id="name"]').send_keys(nome)
    navegador.find_element('xpath','//*[@id="email"]').send_keys(email)
    navegador.find_element('xpath','//*[@id="phone"]').send_keys(num)

hud= CTk()
hud.geometry('300x200')
entrada_nome= CTkEntry(hud, placeholder_text='Insira seu nome', width=200, height=20)
entrada_nome.pack(pady=20)
entrada_email= CTkEntry(hud, placeholder_text='Insira seu email', width=200, height=20)
entrada_email.pack()
entrada_num= CTkEntry(hud, placeholder_text='Insira seu numero', width=200, height=20)
entrada_num.pack(pady=20)
cadastrar= CTkButton(hud, width=200, height= 30, command=cadastro, text='Cadastrar')
cadastrar.pack()




hud.mainloop()