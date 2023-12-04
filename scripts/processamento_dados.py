import csv
import json 

class Dados:
    
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipos_dados = tipo_dados
        self.dados = self.leituraDados() # Verificará se temos dados em json, csv ou lista.
        self.nomes_colunas = self.getColumns() # Retornará uma lista com nomes de colunas preenchidos do arquivo.
        self.qtdd_linhas = self.sizeData() # Retonará a quantidade de linhas do arquivo no qual está sendo trabalhado.
        
    def renameColums(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
                new_dados.append(dict_temp)

        self.dados = new_dados
        self.nomes_colunas = self.getColumns()

    def leituraJson(self):
        dados_json = []
        with open(self.path, 'r') as file:
        
            dados_json = json.load(file)
        return dados_json


    def leituraCsv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
        
                dados_csv.append(row)
        return dados_csv        

    def leituraDados(self):
        dados = []
        if self.tipos_dados == 'csv':
            dados = self.leituraCsv()   
        elif self.tipos_dados == 'json':
            dados = self.leituraJson()
        elif self.tipos_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        
        return dados

    def getColumns(self):
        return list(self.dados[-1].keys())
    
    def sizeData(self):
        return len(self.dados)
    
    def Join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list, 'list')
    
    def transformandoDadosTabela(self):
        dados_combinados_tabela = [self.nomes_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna, 'Indisponível'))  
            dados_combinados_tabela.append(linha)
            
        return dados_combinados_tabela
    
    def salvandoDados(self, path):
        
        dados_combinados_tabela = self.transformandoDadosTabela()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
