def data(data):
    data_lista = data.split('/')
    ano = int(data_lista[0])
    mes = int(data_lista[1])
    dia = int(data_lista[2])
    dicio_data = {'Ano':ano, \
                  'Mês':mes, \
                  'Dia':dia}
    return  dicio_data

def status(status):
    if status[-2:] == '\n':
        status = status[:-1]
    if status == 'SIM':
        return True
    elif status == 'NAO':
        return False

def separa(infos):
    lista_infos = infos.split(':')

def le_arquivo(arq):
    arq.seek(0,0)
    linhas = arq.readlines()
    infos = []
    for line in linhas:
        infos.append(line)
    arq.close()
    return infos

def main():
    arq = open('cadastro.txt','r')
    infos = le_arquivo(arq)
    dados = []
    for j in infos:
        dados.append(separa(info[j]))
    cadastros = []
    for j in dados:
        dicio_dados = {'CPF':dados[j][0],\
                       'Nome':dados[j][1],\
                       'Data_de Nascimento':data(dados[j][2]),\
                       'Data_de_Cadastro':data(dados[j][3]),\
                       'Ativo':status(dados[j][4]),\
                      }
        cadastros.append(dicio_dados)
    print(cadastros)

main()