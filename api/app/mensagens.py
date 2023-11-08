from colorama import Fore, Style
from flask import Response
import json
import os

def escrever_mensagem(mensagem):
    rota = os.path.join('api', 'app', 'static', 'logs', 'arquivo_de_logs')
    arquivo = open(f'{rota}.txt', 'a')

    from datetime import datetime
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mensagem_formatada = f'[{data_hora_atual}] {mensagem}\n'
    arquivo.write(mensagem_formatada)

    arquivo.close()

# Função para formatar mensagens de erro
def erro_msg(msg, error):
    escrever_mensagem(f"[ERRO] {msg} -> {error}")
    print(f"{Fore.RED}[ERRO] {msg} -> {error} {Style.RESET_ALL}")

# Função para formatar mensagens de erro
def normal_msg(msg, error='OK'):
    escrever_mensagem(f"[INFO] {msg} -> {error}")
    print(f"{Fore.GREEN}[INFO] {msg} -> {error} {Style.RESET_ALL}")