import pandas as pd
import numpy as np
import time
import os
import random
from colorama import Fore, Style

def carregar_arquivo(caminho):
    #Carrega o arquivo baseado na extensão.
    if not os.path.isfile(caminho):
        print(Fore.RED + "Erro: O nome do arquivo não existe ou é inválido!" + Style.RESET_ALL)
        return None

    try:
        if caminho.endswith('.csv'):
            print(Fore.BLUE + "Carregando arquivo CSV..." + Style.RESET_ALL)
            return pd.read_csv(caminho, encoding_errors='ignore')
        elif caminho.endswith('.xlsx'):
            print(Fore.BLUE + "Carregando arquivo Excel..." + Style.RESET_ALL)
            return pd.read_excel(caminho)
        else:
            print(Fore.RED + "Erro: Tipo de arquivo desconhecido!" + Style.RESET_ALL)
            return None
    except Exception as erro:
        print(Fore.RED + f"Erro ao carregar o arquivo: {erro}" + Style.RESET_ALL)
        return None

def ver_duplicatas(df):
    #Verifica e remove duplicatas do DataFrame.
    total_duplicatas = df.duplicated().sum()
    print(Fore.YELLOW + f"Total de duplicatas encontradas: {total_duplicatas}" + Style.RESET_ALL)
    if total_duplicatas > 0:
        df[df.duplicated()].to_csv('duplicatas.csv', index=None)
        df = df.drop_duplicates()
        print(Fore.GREEN + "Duplicatas removidas e salvas em 'duplicatas.csv'." + Style.RESET_ALL)
    return df

def ver_nulos(df):
    #Verifica valores nulos no DataFrame e preenche com a string '#Error#'
    total_nulos = df.isnull().sum().sum()
    print(Fore.YELLOW + f"Total de valores nulos encontrados: {total_nulos}" + Style.RESET_ALL)
    
    df = df.fillna('#Error#')
    
    print(Fore.GREEN + "Todos os valores nulos foram preenchidos com '#Error#'!" + Style.RESET_ALL)
    return df

def salvar_arquivo(df, nome_arquivo='Limp_arquivo.csv'):
    #Salva o DataFrame limpo em um arquivo CSV.
    df.to_csv(nome_arquivo, index=None)
    print(Fore.GREEN + f"Arquivo limpo salvo como {nome_arquivo}." + Style.RESET_ALL)

def limp_geral(caminho):
    #Principal função que realiza a limpeza de dados
    sec = random.randint(1, 4)
    print(Fore.CYAN + f"Aguarde por {sec} segundos, verificando arquivos..." + Style.RESET_ALL)
    time.sleep(sec)

    arquivo = carregar_arquivo(caminho)
    if arquivo is None:
        return

    print(Fore.CYAN + f"Totais de linhas: {arquivo.shape[0]}, Totais de colunas: {arquivo.shape[1]}" + Style.RESET_ALL)
    arquivo = ver_duplicatas(arquivo)
    arquivo = ver_nulos(arquivo)

    print(Fore.GREEN + f"Dados limpos com sucesso! Total de linhas: {arquivo.shape[0]}, Total de colunas: {arquivo.shape[1]}" + Style.RESET_ALL)
    salvar_arquivo(arquivo)

if __name__ == "__main__":
    print(Fore.CYAN + "Olá, seja bem-vindo! Vamos limpar seus dados?" + Style.RESET_ALL)
    caminho = input(Fore.YELLOW + "Entre com o nome do arquivo (ou caminho completo): " + Style.RESET_ALL)
    limp_geral(caminho)
