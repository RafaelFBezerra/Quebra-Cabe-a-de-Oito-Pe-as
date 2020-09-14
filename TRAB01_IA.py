import numpy
import copy
import pandas as pd


matriz = []    
for i in range(3):
    linha = []
    for j in range (3):
        linha.append(input())
    matriz.append(linha)
global matriz_usuario 
matriz_usuario = matriz
matriz_orig = copy.deepcopy(matriz_usuario)

def imprime_matriz():
    

    for linha in matriz_usuario:
         print(linha)
    print('\n')

print('\n', 'MATRIZ DIGITADA: ')
imprime_matriz()


def func_manhattan():


    #func = matriz_usuario()
    matriz_user = matriz_usuario
    
    
    i=0
    j=0
    a=0
    b=0


    matriz_base = [[1,2,3],[4,5,6],[7,8,0]]
    vet_custos = []


    for i in range(3):
        for j in range (3):
            if int(matriz_user[i][j]) == int(matriz_base[i][j]):
                custo = 0
                vet_custos.append(custo)

            if int(matriz_user[i][j]) != int(matriz_base[i][j]):
                aux = matriz_user[i][j] 
                for a in range (3):
                    for b in range (3):
                        if int(aux) == int(matriz_base[a][b]) and int(aux) != 0 : #O número zero não entra no calculo 
                            custo_lin = abs(i - a)
                            custo_col = abs(j - b)
                            custo_total = int(custo_lin) + int(custo_col)
                            vet_custos.append(custo_total)
    global manhathan
    manhathan = sum(vet_custos)
    #print('\n',vet_custos)
    #print('\n','CUSTO DA MATRIZ: ',manhathan)
    return vet_custos,matriz_user, matriz_base



def atualiza_matriz():   
    
    func_manhattan()
    global custo_manhathaninicio
    custo_manhathaninicio = manhathan
    ok = False

    for i in range (3):
        for j in range (3):
            if int(matriz_usuario[i][j]) == 0:
                
                
                soma_i = i - 1
                if  soma_i < 0:
                    #posição acima do elemento zero não existe
                    vizinho_c = -1
                else:
                    vizinho_c = matriz_usuario[i-1][j]
                
                
                soma_i = 0
                soma_i = i+1
                if soma_i > 2:
                    #posição abaixo do elemento zero não existe
                    vizinho_b = -1
                else:
                    vizinho_b = matriz_usuario[i+1][j]
                
                soma_j = j-1
                if soma_j < 0:
                    #posição à esquerda do elemento zero não existe
                    vizinho_e = -1
                else:
                    vizinho_e = matriz_usuario[i][j-1]
                
                soma_j=0
                soma_j = j+1
                if soma_j > 2:
                    #posição à esquerda do elemento zero não existe
                    vizinho_d = -1
                else:
                    vizinho_d = matriz_usuario[i][j+1]
                
                
                ok = True
                pos_i = i
                pos_j = j
                break
        if ok:
            break
    return vizinho_c,vizinho_b,vizinho_e,vizinho_d,pos_i,pos_j


def troca_acima():

    func = atualiza_matriz()
    vizinho_c = func[0]
    i = func[4]
    j = func[5]
    if(int(vizinho_c) != -1):
        matriz_usuario[i-1][j] = matriz_usuario[i][j]
        matriz_usuario[i][j] = vizinho_c
        valid = True
    else:
        valid = False
    func_manhattan()
    return valid


def recursiva_acima():

    func = atualiza_matriz()
    vizinho_b = func[1]
    i = func[4]
    j = func[5]
    matriz_usuario[i+1][j] = matriz_usuario[i][j]
    matriz_usuario[i][j] = vizinho_b
    func_manhattan()
    

def troca_abaixo():

    func = atualiza_matriz()
    vizinho_b = func[1]
    i = func[4]
    j = func[5]
    if(int(vizinho_b) != -1):
        matriz_usuario[i+1][j] = matriz_usuario[i][j]
        matriz_usuario[i][j] = vizinho_b
        valid = True
    else:
        valid = False
    func_manhattan()
    return valid


def recursiva_abaixo():
    
    func = atualiza_matriz()
    vizinho_c = func[0]
    i = func[4]
    j = func[5]
    matriz_usuario[i-1][j] = matriz_usuario[i][j]
    matriz_usuario[i][j] = vizinho_c
    func_manhattan()
    


def troca_esquerda():
    
    func = atualiza_matriz()
    vizinho_e = func[2]
    i = func[4]
    j = func[5]
    if (int(vizinho_e) != -1):
        matriz_usuario[i][j-1] = matriz_usuario[i][j]
        matriz_usuario[i][j] = vizinho_e
        valid = True
    else:
        valid = False
    func_manhattan()
    return valid


def recursiva_esquerda():
    
    func = atualiza_matriz()
    vizinho_d = func[3]
    i = func[4]
    j = func[5]
    matriz_usuario[i][j+1] = matriz_usuario[i][j]
    matriz_usuario[i][j] = vizinho_d
    func_manhattan()


def troca_direita():

    func = atualiza_matriz()
    vizinho_d = func[3]
    i = func[4]
    j = func[5]
    if(int(vizinho_d)!= -1):
        matriz_usuario[i][j+1] = matriz_usuario[i][j]
        matriz_usuario[i][j] = vizinho_d
        valid = True
    else:
        valid = False
    func_manhattan()
    return valid


def recursiva_direita():
    
    func = atualiza_matriz()
    vizinho_e = func[2]
    i = func[4]
    j = func[5]
    matriz_usuario[i][j-1] = matriz_usuario[i][j]
    matriz_usuario[i][j] = vizinho_e
    func_manhattan()

def avaliação_manhatthan():


    func_c = troca_acima()
    valid_c = func_c

    if valid_c == True:
        #imprime_matriz()
        troca_c = manhathan
        recursiva_acima()
        #imprime_matriz()
        
    else:
        troca_c = 50
        


    func_b = troca_abaixo()
    valid_b = func_b

    if valid_b == True:
        #imprime_matriz()
        troca_b = manhathan
        recursiva_abaixo()
        #imprime_matriz()
        
    else:
        troca_b = 50
        


    func_e = troca_esquerda()
    valid_e = func_e

    if valid_e == True:
        #imprime_matriz()
        troca_e = manhathan
        recursiva_esquerda()
        #imprime_matriz()
        
    else:
        troca_e = 50
        


    func_d = troca_direita()
    valid_d = func_d

    if valid_d == True:
        #imprime_matriz()
        troca_d = manhathan
        recursiva_direita()
        #imprime_matriz()
        
    else:
        troca_d = 50
        
    
    
    return troca_c, troca_b, troca_e, troca_d

def a_estrela():
    func = avaliação_manhatthan()
    troca_c = func[0]
    troca_b = func[1]
    troca_e = func[2]
    troca_d = func[3]
    global a


    #itens para criação do df
    vizinhos = [['Troca_c',int(troca_c)],['Troca_b',int(troca_b)],['Troca_e',int(troca_e)],['Troca_d', int(troca_d)]]

    #criação df
    vet_custosvizinhos = pd.DataFrame(vizinhos,columns=['Vizinhos','Custo_Troca'])
    #print('\n',vet_custosvizinhos,'\n')

    #ordenação por elemento
    vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
    print('\n',vet_custosvizinhos,'\n')

    a = 0
    check_a = False
    check_b = False
    check_c = False
    check_d = False


    while manhathan != 0:

        if(vet_custosvizinhos['Vizinhos'].iloc[0]) == 'Troca_c' and check_b != True:
            
            troca_acima()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = True
            check_b = False
            check_c = False
            check_d = False
            continue
            
        if(vet_custosvizinhos['Vizinhos'].iloc[0]) == 'Troca_b' and check_a != True:
            
            troca_abaixo()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = True
            check_c = False
            check_d = False
            continue


        if(vet_custosvizinhos['Vizinhos'].iloc[0]) == 'Troca_e' and check_d != True:
            
            troca_esquerda()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = True
            check_d = False
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[0]) == 'Troca_d' and check_c != True:
            
            troca_direita()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = False
            check_d = True
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[1]) == 'Troca_c' and check_b != True:
            
            troca_acima()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = True
            check_b = False
            check_c = False
            check_d = False
            continue
            
        if(vet_custosvizinhos['Vizinhos'].iloc[1]) == 'Troca_b' and check_a != True:
            
            troca_abaixo()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = True
            check_c = False
            check_d = False
            continue


        if(vet_custosvizinhos['Vizinhos'].iloc[1]) == 'Troca_e' and check_d != True:
            
            troca_esquerda()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = True
            check_d = False
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[1]) == 'Troca_d' and check_c != True:
            
            troca_direita()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = False
            check_d = True
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[2]) == 'Troca_c' and check_b != True:
            
            troca_acima()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = True
            check_b = False
            check_c = False
            check_d = False
            continue
            
        if(vet_custosvizinhos['Vizinhos'].iloc[2]) == 'Troca_b' and check_a != True:
            
            troca_abaixo()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = True
            check_c = False
            check_d = False
            continue


        if(vet_custosvizinhos['Vizinhos'].iloc[2]) == 'Troca_e' and check_d != True:
            
            troca_esquerda()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = True
            check_d = False
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[2]) == 'Troca_d' and check_c != True:
            
            troca_direita()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = False
            check_d = True
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[3]) == 'Troca_c' and check_b != True:
            
            troca_acima()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = True
            check_b = False
            check_c = False
            check_d = False
            continue
            
        if(vet_custosvizinhos['Vizinhos'].iloc[3]) == 'Troca_b' and check_a != True:
            
            troca_abaixo()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = True
            check_c = False
            check_d = False
            continue


        if(vet_custosvizinhos['Vizinhos'].iloc[3]) == 'Troca_e' and check_d != True:
            
            troca_esquerda()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = True
            check_d = False
            continue

        if(vet_custosvizinhos['Vizinhos'].iloc[3]) == 'Troca_d' and check_c != True:
            
            troca_direita()
            imprime_matriz()
            func = avaliação_manhatthan()


            troca_c = func[0]
            troca_b = func[1]
            troca_e = func[2]
            troca_d = func[3]


            vet_custosvizinhos = vet_custosvizinhos.sort_index()
            vet_custosvizinhos.iloc[0,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_c)
            vet_custosvizinhos.iloc[1,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_b)
            vet_custosvizinhos.iloc[2,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_e)
            vet_custosvizinhos.iloc[3,vet_custosvizinhos.columns.get_loc('Custo_Troca')] = int(troca_d)


            #ordenação por elemento
            vet_custosvizinhos = vet_custosvizinhos.sort_values(['Custo_Troca'])
            print('\n',vet_custosvizinhos,'\n')
            a = a + 1
            check_a = False
            check_b = False
            check_c = False
            check_d = True
            continue


a_estrela()
print('O PROBLEMA FOI SOLUCIONADO COM', a, 'MOVIMENTOS')


#ARMAZENAR CAMINHOS POSSÍVEIS NA FILA DE PRIORIDADES
