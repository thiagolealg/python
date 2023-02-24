import pandas as pd
import glob

# Get CSV files list from a folder
path = 'C:\\Users\\f9329149\\PycharmProjects\\tudo'
csv_files = glob.glob(path + "/*.csv")

# Read each CSV file into DataFrame
# This creates a list of dataframes
df_list = (pd.read_csv(file) for file in csv_files)

df = pd.DataFrame(data=csv_files, columns=['nome_arquivo'])
df.drop(index=df.index[0], axis=0, inplace=True)
df.replace(to_replace='C', value='a', regex=True)
# Concatenate all DataFrames
big_df = pd.concat(df_list, ignore_index=True)
big_df.to_csv("lista_servicos.csv")

