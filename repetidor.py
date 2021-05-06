#importando o pacote de reconhecimento de fala
import speech_recognition as speech
#importando o pacote de que transformará o texto em fala
from gtts import gTTS as gt
#importando o pacote que tocará o áudio da fala
from playsound import playsound
#importando o pacote para excluir o áudio fala
import os


#definição para reconhecimento da frase falada
def mic():
    #reconhece o microfone
    voz = speech.Recognizer()
    with speech.Microphone() as source:
        print('Fale algo!')
        #abre o microfone para leitura da frase
        entrada = voz.listen(source)
    #traduz a áudio da frase falada para texto
    voz_google = voz.recognize_google(entrada, language='pt-br')
    print('você: '+ voz_google)
    #retorna a frase em texto
    return voz_google


#definição para converter texto em fala
def bot_fala(texto):
    #converte o texto em fala
    fala = gt(texto, lang='pt-br')
    #salva a fala convertia em áudio mp3
    fala.save('fala.mp3')
    print('Bot: '+ texto)
    #executa o áudio mp3
    playsound('fala.mp3')    


#texto falado inicialmente indicando um simples comando de voz
bot_fala('Se quiser sair apenas diga sair! caso contrário eu irei repetir o que você falar!')

#estrutura de repetição para o programa rodar em looping até receber o comando sair
while True:
    #tratamento de erro caso não indentifique nenhuma palavra
    try:
        #apaga o áudio antigo para poder criar um novo no lugar
        os.remove('fala.mp3')
        #utiliza a definição mic para obter a fraze em texto
        frase = mic()
        #utiliza o texto extraido do que foi falado e faz com que seja repetido pelo computador
        bot_fala(frase)    
    #resposta do tratamento de erro
    except:
        bot_fala('Desculpa, mas não entendi')
    #verifica se a resposta foi sair para executar o comando de finalizar o programa
    if frase == 'sair':
        #apaga o áudio já utilizado
        os.remove('fala.mp3')
        #fecha o programa
        from sys import exit
        exit()
