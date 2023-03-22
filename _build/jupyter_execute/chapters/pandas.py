#!/usr/bin/env python
# coding: utf-8

# #  Pandas 
# 
# <img src="https://pandas.pydata.org/docs/_static/pandas.svg" alt=" " class="bg-primary mb-1" width="200px">
#  
# 
# A documentação do pacote Pandas se encontra disponível em: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/) .
# <!-- 
# 
# $
# 1+2
# $
# 
# \begin{gather*}
# a_1=b_1+c_1\\
# a_2=b_2+c_2-d_2+e_2
# \end{gather*}
# 
# \begin{align}
# a_{11}& =b_{11}&
#   a_{12}& =b_{12}\\
# a_{21}& =b_{21}&
#   a_{22}& =b_{22}+c_{22}
# \end{align}
#   -->
# 
# 

# ```{contents} 
# ```

# ## Criação de dois dataframes para aplicação das ferramentas do Pandas
# 
# Serão criados dois dataframes com notas de alunos em algumas disciplinas em meses do ano de 2023. Os nomes dos alunos são gerados aleatoriamente, bem como suas as notas. Se você não tiver disposto a seguir o processo de geração das bases de dados, pule para a próxima seção, onde os dataframes serão lidos de arquivos e usados para treinar o uso das ferramentas do Pandas. 

# In[1]:


# importação do pandas
import pandas as pd
# versão
pd.__version__ 


# In[2]:


df_1 = pd.DataFrame(columns=['aluno', 'identificacao', 'mes',   'nota matematica', 'nota fisica'])
df_2 = pd.DataFrame(columns=[          'identificacao',  'turma', 'mes','nota geografia', 'nota historia']) 
# O dataframe 2 não possui nome do aluno, somente identificação


# In[3]:


# ! pip install names_generator
 # instala pacote que gera nomes aleatórios


# In[4]:


from names_generator import generate_name

# guarda lista de 40 nomes gerados aleatoriamente
list_names = []
for i in range(40): 
    list_names.append(generate_name(style='capital', seed=i)) 


# In[5]:


# mostrando os 5 primeiros nomes
list_names[0:5]


# In[6]:


# atribuindo nomes gerados aos alunos do dataframe 1
df_1['aluno'] = list_names


# In[7]:


# 5 primeiras linhas do dataframe 1
df_1.head()


# In[8]:


# o número de identificação dos alunos também será escolhido aleatoriamente com o pacote numpy
import numpy as np
# semente randômica para reproduzir lista
np.random.seed(0)

# lista de numéros aleatórios do tamanho do dataframe 1 (sem haver repetição) 
df_1['identificacao'] = np.random.choice(range(1200,1500), size=len(df_1), replace=False)

# a mesma lista é atribuída para o dataframe 2
df_2['identificacao'] = df_1['identificacao'] 


# In[9]:


# turma escolhida entre A e B com 50% de alunos em cada
df_2['turma'] = int(len(df_2)/2)*['A'] + int(len(df_2)/2)*['B'] # preenche a primeira metade de valores como turma A e segunda metade com turma B 
df_2['turma'].describe() 


# In[10]:


# definiremos os meses (de aula) de fevereiro a novembro do ano de 2023, assim cada aluno terá uma nota por disciplina em cada mês

meses = pd.date_range(start = '2023-02-01', end = '2023-10-01').to_period('M').unique() 

df1 = pd.DataFrame() # novos dataframes com os meses de 2023
df2 = pd.DataFrame()

for mes in meses:
    df_1_aux = df_1.copy() # dataframe auxiliar para guardar o original
    df_1_aux['mes'] = mes
    df_2_aux = df_2.copy() 
    df_2_aux['mes'] = mes
    df1 = pd.concat([df1, df_1_aux])
    df2 = pd.concat([df2, df_2_aux])


# In[11]:


# Atribuiremos notas aleatórias nos dois dataframes onde, alguns valores, intencionalmente serão deixados como nulos.

# definindo uma lista de disciplinas para simplificar
disciplinas = ['fisica','matematica', 'geografia','historia']

for id in df1['identificacao'].unique():
    for disciplina in disciplinas:
        if np.random.random() < 0.95:   # em 95% atribui nota, em 5% as notas serão valores nulos
            
            if disciplina in ['fisica','matematica']:
                df1.loc[df1['identificacao']==id, 'nota '+disciplina]  = round((np.random.uniform(0,10)),1) # float com uma casa decimal
            else:
                df2.loc[df2['identificacao']==id, 'nota '+disciplina]  = round((np.random.uniform(0,10)),1)    


# In[12]:


# dataframes finais
display(df1)
display(df2)


# ## Ferramentas básicas de manipulação de dataframes

# In[13]:


# mostrar nome de todas as colunas de df1
print(df1.columns.values)
#ou
df1.columns.tolist()


# In[14]:


# ver quantidade maxima de linhas e colunas que são exibidas por padrão
qtd_cols_padrao = pd.options.display.max_columns
qtd_rows_padrao = pd.options.display.max_rows
print('quantidade máxima de linhas exibidas por padrão: '+str(qtd_rows_padrao))
print('quantidade máxima de colunas exibidas por padrão: '+str(qtd_cols_padrao))

# configurar o pandas para mostrar todas as colunas em todos os dataframes
pd.set_option('display.max_columns', 900)
# ou
# pd.options.display.max_columns = None

# retornar o padrão à quantidade inicial
# pd.options.display.max_columns = qtd_cols_padrao
pd.set_option('display.max_columns', qtd_cols_padrao)


# In[15]:


# mostrar todas as linhas por padrão
pd.set_option('display.max_rows', 900)
# ou
# pd.options.display.max_rows = 900

# retornar o padrão à quantidade inicial
# pd.options.display.max_columns = qtd_rows_padrao
pd.set_option('display.max_rows', qtd_rows_padrao)


# ## Ferramentas de análise descritiva

# In[ ]:




