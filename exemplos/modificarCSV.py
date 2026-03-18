import pandas as pd

# caminho do arquivo
caminho_do_arquivo = 'zwei.csv'

# Crie um dicionário com os novos dados.
novo_resultado = {
    'P1': 1,
    'P2': 9,
    'frequencia': 15,
    'atual': 0,
    'ultimo': 2830,
    'maior': 300,
    'media': 95.5
}

try:
    # Carregue o arquivo CSV

    try:
        df = pd.read_csv(caminho_do_arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{caminho_do_arquivo}' não encontrado. Um novo arquivo será criado.")
        df = pd.DataFrame(columns=novo_resultado.keys())

    # 3. Converta o resultado 
    novo_df = pd.DataFrame([novo_resultado])

    # ignore_index=True é importante para resetar o índice da nova linha
    df_atualizado = pd.concat([df, novo_df], ignore_index=True)
    
    print("--- Últimas 5 linhas do arquivo (após adicionar o novo resultado) ---")
    print(df_atualizado.tail())

    # Salve o DataFrame atualizado 
    df_atualizado.to_csv(caminho_do_arquivo, index=False)
    
    print(f"\nDados adicionados com sucesso ao arquivo '{caminho_do_arquivo}'!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

import pandas as pd

caminho_do_arquivo = 'zwei.csv'

# Carregue o arquivo
df = pd.read_csv(caminho_do_arquivo)



# .loc é usado para localizar linhas e colunas por nome/condição
condicao = (df['P1'] == 10) & (df['P2'] == 33)

# Segundo argumento de .loc é a coluna que quero alterar
df.loc[condicao, 'frequencia'] = 41

# Salve as alterações de volta no arquivo
df.to_csv(caminho_do_arquivo, index=False)

print("Linha modificada com sucesso!")
