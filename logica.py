﻿from config import *
from funcoes import *
from webexteams import getwebexMsg, webexmsgRoomviaID
import json

def logica(comando,usermail):

    # faz a logica de entender o comando pedido e a devida resposta para o usuario
    # o parametro usermail e' utilizado para identificar o usuario que solicitou o comando
    # O usuario pode ser uzado como filtro para se executar ou negar o comando
    #
    # Retorna mensagem para ser enviada para console ou Webex teams
    
    #Separa o comando por espacos
    #Primeiro item e'o comando em si, os demais sao parametros deste comando
    #
    comando=comando.lower()
    sp=comando.split(" ")
    
    # comando na variavel box, lower deixa em minusculo para normalizar
    box=sp[0]
    
    # Para o caso de nenhum pedido coberto aqui
    mais="\nEscreva 'mais' para saber suas opções"
    
    # 21.11.19
    # variavel arquivo para o caso do bot devolver arquivos anexados
    
    arquivo=""
    
    msg=""
	
    # chamadas de acordo com os parametros

    # Funcoes para todos
    
    # Uso da funcao "mais"

    if box == "Oi" and len(sp)<2:
        msg="Aldo é um cara dahora:\n"
     


    if len(sp)>2:
        tema=sp[2]
        msg=maissobre(tema)
        
    # Funcoes que usam outras APIs
    if len(sp)>1 and box=="api":
        # URL
        site="apitesteexample.com"
        # Parametro de autorizacao
        token="123456"
        msg=APICall(site,token)
        

    return msg,arquivo


def trataPOST(content):

    # resposta as perguntas via webexteams
    # trata mensagem quando nao e' gerada pelo bot. Se nao e' bot, entao usuario
    try:     
        if content['name']==webhook_name and content['data']['personEmail']!=botmail:
            # identifica id da mensagem
            msg_id=(content['data']['id'])
            # identifica dados da mensagem
            webextalk=getwebexMsg(msg_id)
            usermail=webextalk[2]
            mensagem=webextalk[0]
            sala=webextalk[1]

            # executa a logica
            msg,arquivo=logica(mensagem,usermail)
        
            # Envia resposta na sala apropriada
            webexmsgRoomviaID(sala,msg,arquivo)

    except:
            print("POST nao reconhecido")
            pass