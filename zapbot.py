from selenium import webdriver

import time


class WhatsappBot:
    def __init__(self):
        self.messagens = ['Bom dia meu anjo', 'Tuto pein com você ?', 'dormiu bem ? ','que sonooo !!!'] # seta mensagem default
        self.contatos = ['Minha Linda'] # devem ser exatamente iguais aos criados no whats
        
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br') # add linguagem msg
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') # seta caminho do executavel do chrome driver 


    def EnviarMensagens(self):


        """ seta site para bot verificar """
        self.driver.get('https://web.whatsapp.com') 
        time.sleep(30) # delay de 30 segundos, para esperar escanear o qr code

        """ loop de contatos """
        for contato in self.contatos:
            
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{contato}']") # pega refer^ncia do elemento (contato)
            time.sleep(3) # delay de 3 segundos, para não travar durante os cliques
            grupo.click()

            for mensagem in self.messagens:
                chat_box = self.driver.find_element_by_class_name('_1Plpp') # pega referência do elemento (chat box)
                time.sleep(1)
                chat_box.click()
                time.sleep(1)
                chat_box.send_keys(mensagem) # escreve mensagem default

                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']") # pega referência do elemento (span button)
                time.sleep(1)
                botao_enviar.click()
                time.sleep(1)



""" executa classe """
bot = WhatsappBot()
bot.EnviarMensagens()
