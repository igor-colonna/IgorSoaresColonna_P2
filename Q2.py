def inverte_matriz(matriz):


    det = (matriz[0][0] + matriz[1][1]) - (matriz[0][1]+\
        matriz[1][0])
    if det == 0:
        return 'None'
    var_temp = 1/det
    result = [matriz[1][1]*var_temp, matriz[0][1]* \
        -1*var_temp, matriz [1][0]*-1*var_temp, \
        matriz[0][0]*var_temp]
    return result

def main():
    a = float(input('Digite o valor de (0,0): '))
    b = float(input('Digite o valor de (0,1): '))
    c = float(input('Digite o valor de (1,0): '))
    d = float(input('Digite o valor de (1,1): '))
    lista1 = [a,b]
    lista2 = [c,d]
    matriz = [lista1,lista2]
    result = inverte_matriz(matriz)
    print(matriz,'\t',result)
