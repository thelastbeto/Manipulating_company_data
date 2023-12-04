from processamento_dados import Dados


################## LEITURA DOS DADOS ##################

path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'

dados_empresasA = Dados(path_json, 'json')
print(f"Nome das colunas da empresa A: {dados_empresasA.nomes_colunas}")
print(f"Quantidade de linhas do arquivo da empresa A: {dados_empresasA.qtdd_linhas}")

dados_empresasB = Dados(path_csv, 'csv')
print(f"Nome das colunas da empresa B: {dados_empresasB.nomes_colunas}")
print(f"Quantidade de linhas do arquivo da empresa B: {dados_empresasB.qtdd_linhas}")

############## TRANSFORMANDO OS DADOS #################

key_mapping = {
                'Nome do Item': 'Nome do Produto',
                'Classificacao do Produto':'Categoria do Produto',
                'Valor em Reais (R$)':'Preço do Produto (R$)',
                'Quantidade em Estoque':'Quantidade em Estoque',
                'Nome da Loja':'Filial',
                'Data da Venda': 'Data da Venda'
}

dados_empresasB.renameColums(key_mapping)
print(f"Dados da empresa B após renomeação das colunas: {dados_empresasB.nomes_colunas}")

dados_fusao = Dados.Join(dados_empresasA, dados_empresasB)
print(f"Retorno do objeto após a junção dos dados das duas empresas: {dados_fusao}")
print(f"Nome das colunas da Fusão dos dados: {dados_fusao.nomes_colunas}")
print(f"Quantidade de linhas após fusão dos dados: {dados_fusao.qtdd_linhas}")

###################### SALVANDO OS DADOS #######################


path_dados_combinados = 'pipeline_dados/data_processed/dados_combinados.csv'
dados_fusao.salvandoDados(path_dados_combinados)
print(f"Retorno do arquivo que foi gerado: {path_dados_combinados}")



