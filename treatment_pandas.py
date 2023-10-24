# Importe a biblioteca pandas para trabalhar com dataframes
import pandas as pd

# Leia o arquivo CSV 'raw.csv' e forneça os nomes das colunas como ['data']
df = pd.read_csv('raw.csv', names=['data'])

# Divida a coluna 'data' em várias colunas com base em vírgulas (',') e crie um novo DataFrame
df = df.data.str.split(',', expand=True)

# Defina os nomes das colunas no DataFrame resultante
columns = ['nome', 'codigo_produto', 'salario', 'estado', 'ddd', 'telefone', 'cpf', 'produto']

# Descarte a coluna 8 (índice 8) do DataFrame - por causa da estruturação do csv, a última coluna retornou vazia
df.drop(8, axis='columns', inplace=True)

# Atribua os nomes de colunas corretos ao DataFrame
df.columns = columns

# Divida a coluna 'nome' em 'nome' e 'sobrenome' usando um espaço em branco como separador
df[['nome', 'sobrenome']] = df.nome.str.split(' ', n=1, expand=True)

# Insira 'sobrenome' na posição 1 na lista de colunas
columns.insert(1, 'sobrenome')

# Atualize o DataFrame para definir a ordem correta das colunas
df = df[columns]

# Defina uma função para formatar nomes
def format_name(name):
    name = name.capitalize()  # Primeira letra em maiúscula
    name = name.replace('@', 'a')  # Substitua '@' por 'a'
    return name

# Aplique a função de formatação aos valores nas colunas 'nome' e 'sobrenome'
df['nome'] = df['nome'].apply(format_name)
df['sobrenome'] = df['sobrenome'].apply(format_name)

# Remova caracteres não numéricos da coluna 'telefone' usando regex
df['telefone'] = df['telefone'].str.replace(r'[^0-9]', '', regex=True)

# Combine as colunas 'ddd' e 'telefone' para criar a coluna 'telefone' final
df['telefone'] = df['ddd'] + df['telefone']

# Descarte a coluna 'ddd', pois não é mais necessária
df.drop('ddd', axis='columns', inplace=True)

# Remova caracteres não numéricos da coluna 'cpf' usando regex
df['cpf'] = df['cpf'].str.replace(r'[^0-9]', '', regex=True)

# Crie um dicionário para mapear nomes completos de estados para suas siglas
siglas_estados = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}

# Mapeie os nomes completos dos estados para siglas na coluna 'estado'
df['estado'] = df['estado'].map(siglas_estados)

# Converta a coluna 'salario' para o tipo de dado float
df['salario'] = df['salario'].astype(float)

# Imprima o DataFrame formatado
print(df)