# essa função retira os dados da tabela na web e transforma em dataframe
#defina os nomes das colunas, devem ter a mesma quantidade de linhas 
rows = 1 + len(driver.find_elements(By.XPATH, "incluir xpath aqui até o tr")) #inclua o xpath no campo anterior
cols = len(driver.find_elements(By.XPATH, "incluir xpath aqui até o td")) #inclua o xpath no campo anterior
colunas = ["incluir a lista aqui do nome das colunas"]

def table_to_dataframe(xpath_caminho, tamanho_lista):
	tamanho_lista = int(tamanho_lista
        for r in range(1, rows):
            for p in range(1, cols - 1):
                # obtaining the text from each column of the table
                value = driver.find_element(By.XPATH,
                    xpath_caminho + str(
                        r) + "]/td[" + str(p) + "]").text
                print(value)
                list.append(value)
            print(list)
        mat = []
        while list != []:
            mat.append(list[:tamanho_lista])
            list = list[tamanho_lista:]
            print(list)
        tabela = pd.DataFrame(data=mat, columns=colunas)
        tabela.to_csv("escolha o nome do arquivo" + ".csv")
