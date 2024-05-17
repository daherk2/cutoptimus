import streamlit as st
import copy as cp

# Função para importar e processar o arquivo
def ImportFile(data):
    data_aux = data.split('\n')
    data = []
    for str1 in data_aux:
        aux = str1.split()
        for d in aux:
            data.append(float(d))
    return data

# Cabeçalho da aplicação
st.title('Otimização de Corte de Barras')

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha o arquivo de dados", type=['txt'])
if uploaded_file is not None:
    stringio = uploaded_file.read().decode("utf-8")
    dados = ImportFile(stringio)
    dados_orig = sorted(dados, reverse=True)
    dados = cp.deepcopy(dados_orig)
    
    tam = 12
    i_barra = []
    while len(dados) > 0:
        q_barra = 0
        dados_aux = cp.deepcopy(dados)
        linha = []
        for i in range(len(dados)):
            if dados[i] <= (tam - q_barra):
                q_barra += dados[i]
                linha.append(dados[i])
                dados_aux.remove(dados[i])
            if q_barra == tam:
                break
        i_barra.append(linha)
        dados = cp.deepcopy(dados_aux)

    sobra = 0
    for i in range(len(i_barra)):
        sobra += tam - sum(i_barra[i])
    
    # Exibindo os resultados
    st.write("***** CONFIGURAÇÃO FINAL *****")
    st.write(f"Total de barras: {len(i_barra)}")
    st.write(f"Total de produção: {len(dados_orig)}")
    perda = round(100 * sobra / (12 * len(i_barra)), 2)
    st.write(f"Perda: {perda}%")
    st.write("--- Distribuição ---")
    for i in range(len(i_barra)):
        st.write(f"id: {i+1}, Compr(m): {tam}, Sobra: {round(tam - sum(i_barra[i]), 2)}, Cortes: {i_barra[i]}")

