#Solução elaborada a partir do algoritmo exemplificado no portal 
#https://www.macoratti.net/alg_cpf.htm

import numpy

def validacaodados_9_digitos():
    while True:
        cpf_Sem_DV = input('Digite os 9 primeiros digitos do seu CPF: ')
        print('')
        if not cpf_Sem_DV.isdecimal() or ((len(str(cpf_Sem_DV))) != 9) == True:
            print('\033[31mERRO! Valor inválido! Tente Novamente.\n\033[m')
            continue
        else:
            return cpf_Sem_DV
        
def validacaodados_2_digitos():
    while True:
        cpf_DV = input('Digite os 2 últimos digitos do seu CPF: ')
        print('')
        if not cpf_DV.isdecimal() or ((len(str(cpf_DV))) != 2) == True:
            print('\033[31mValor inválido! Tente Novamente.\n\033[m')
            continue
        else:
            return cpf_DV

loop = True
while loop == True:
    cpf_Sem_DV = validacaodados_9_digitos()
    cpf_DV = validacaodados_2_digitos()
        
    numValidacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    dadoTratado = []
    dadoTratado += map(int, cpf_Sem_DV)
    
    restDivisao = sum(numpy.multiply(numValidacao, dadoTratado))%11
  
    if restDivisao >=2:
        digVerificador01 = 11 - restDivisao
    else:
        digVerificador01 = 0
        
    dadoTratado.append(digVerificador01)
    numValidacao.insert(0, 11)

    restDivisao = sum(numpy.multiply(numValidacao, dadoTratado))%11

    if restDivisao >=2:
        digVerificador02 = 11 - restDivisao
    else:
        digVerificador02 = 0

    dado_calculado = str(digVerificador01) + str(digVerificador02)

    if cpf_DV == dado_calculado:
        print('CPF Validado com sucesso!')
        loop = False
        
    else:
        print('\033[31mCPF Inválido! Tente novamente.\n\033[m')
        continue