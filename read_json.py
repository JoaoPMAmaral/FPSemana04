nomeFicheiro = input("")
nomeFicheiroAberto = "data.json"
nome = ""
extensao = ""
extensaoJson = True

#verifica nome e extensao
for a in nomeFicheiro:
    if(a != "."):
        nome += a
ondePonto = nomeFicheiro.index(".")

for b in range(ondePonto + 1,len(nomeFicheiro)):
    extensao += nomeFicheiro[b]

if(extensao != "json"):
    extensaoJson = False

file = open(nomeFicheiro,"rt",encoding ="utf-8")

#verifica se vazio
primeiraLetra = file.readlines(1)

#verifica se campos vazios
keys = []
valores = []

linhas = file.readlines()

for linha in linhas:
    if ":" in linha:
        key,valor = linha.split(":",1)

        key = key.strip().strip('"').strip()
        valor = valor.strip().strip('",').strip()

        if(key == ""):
            keys.append(key)
        
        if(valor == ""):
            valores.append(key)

#FICHEIRO NAO EXISTE
try:
    assert nomeFicheiro != nomeFicheiroAberto, "Erro: Ficheiro Não Encontrado!\nProcesso Concluído!"
except:
    print("Erro: Ficheiro Não Encontrado!\nProcesso Concluído!")

#FICHEIRO NAO JSON
try:
    assert extensaoJson != True, "Erro: Ficheiro Não Contém JSON Válido!\nProcesso Concluído!"
except:
    print("Erro: Ficheiro Não Contém JSON Válido!\nProcesso Concluído!")

#FICHEIRO VAZIO
try:
    assert primeiraLetra == "", "Erro: Ficheiro Vazio!\nProcesso Concluído!"
except:
    print("Erro: Ficheiro Vazio!\nProcesso Concluído!")


#SEM CAMPOS
try:
    assert keys or valores,"Erro: Campos Obrigatórios em Falta!\nProcesso Concluído!"
except:
    print("Erro: Campos Obrigatórios em Falta!\nProcesso Concluído!")

    
#BEM FEITO
print("Processo Concluído!")