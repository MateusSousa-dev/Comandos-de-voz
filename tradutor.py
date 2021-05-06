#importando o reconhecedor de frases
import speech_recognition as sr
#importando o tradutor de textos
from translate import Translator
#importando o conversor de texto para fala
from gtts import gTTS
#importando o leitor de áudio
from playsound import playsound
#importando comando para fechar o programa
from sys import exit
#importando o comando para apagar a fala anterior
from os import remove



#definição de linguagem inicial
linguagem = 'pt-br'
linguagem_entrada = 'pt-br'

#definição para transformar a fala em texto
def entrada():
    #reconhece o microfone
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        #abre o microfone para reconhecer a frase
        reconhece = mic.listen(source)
    #utiliza o google para transformar a fala em texto
    reconhece_google = mic.recognize_google(reconhece, language=linguagem_entrada)
    print(reconhece_google)
    #retorna a frase em texto
    return reconhece_google


#definição para converter texto em fala
def saida(frase):
    fala = gTTS(frase, lang=linguagem)
    fala.save('audio.mp3')
    print(frase)
    playsound('audio.mp3')
    remove('audio.mp3')


#definição para escolha de linguagens
def escolha():
    #opções de línguas
    while True:
        opcoes = entrada()
        if opcoes == 'português':
            port = 'pt'
            return port
            break
        elif opcoes == 'inglês':
            en = 'en'
            return en
            break
        elif opcoes == 'espanhol':
            es = 'es'
            return es
            break
        elif opcoes == 'chinês':
            zh = 'zh'
            return zh
            break
        else:
            saida('Desculpe, não entendi!')


#fala inicial
saida('Olá, seja bem vindo ao tradutor')
#fala com as opções de línguas
saida('As opções de línguas são: Português, Inglês, Espanhol e Chinês.')

while True:
    #tratamento de erro caso não entenda a linguagem
    try:
        #escolha da língua falada
        saida('Qual será a língua de origem?')
        de = escolha()
        break
        #resposta ao erro por não entender a linguagem
    except:
        saida('Desculpe, não entendi')

while True:
    #tratamento de erro caso não entenda a linguagem
    try:
        #escolha da língua traduzida
        saida('Qual será a língua para a tradução?')
        para = escolha()
        break
    #resposta ao erro por não entender a linguagem
    except:
        saida('Desculpe, não entendi')


#definição para traduzir a frase em texto para outra língua
def traduz(texto):
    #escolha de linguagens para a tradução
    traduzir = Translator(from_lang=de, to_lang=para)
    #tradução do texto
    traducao = traduzir.translate(texto)
    print(traducao)
    #retorna a tradução
    return traducao


while True:
    #define lingua para português
    linguagem = 'pt-br'
    saida('Qual a frase a ser traduzida?')
    #tratativa de erro caso não entenda a frase
    try:
        #define a linguagem para a língua de origem
        linguagem_entrada = de
        #utiliza a definição entrada para receber a frase
        frase_original = entrada()
        #parte da tratativa de erro, indica que entendeu a frase
        leitura = 'compreendido'
    #resposta ao erro de não entender a frase
    except:
        #define lingua para português
        linguagem = 'pt-br'
        saida('Desculpe, não entendi!')
        #parte da tratativa de erro, indica que não entendeu a frase e retorna ao início do loop
        leitura = 'não compreendido'
    
    #continuação após as tratativas de erro
    if leitura == 'compreendido':
        #define a linguagem para a língua da tradução
        linguagem = para
        #utiliza a função traduz para traduzir a frase falada pelo usuário
        traduzido = traduz(frase_original)
        #retorna em áudio a resposta do que foi traduzido
        saida(traduzido)

        #comando de finalização do programa por comando de voz
        if frase_original == 'sair':
            exit()
        elif frase_original == 'exit':
            exit()
        elif frase_original == '离开':
            exit()
        elif frase_original == 'salir':
            exit()

