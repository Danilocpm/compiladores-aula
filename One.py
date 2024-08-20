'''
Atividade: Construa um analisador simples de caracteres (String, palavras, símbolos, números, espaços em brancos...) com as seguintes funções:

 - Entrada: encontre caracteres e leia sequencialmente os caracteres e espaços em brancos.

- Execução: identifique os caracteres e espaços em brancos e faça a contagem da quantidade de caracteres e espaços em brancos encontrados.
   
- Saída: mostre na tela a sequencia dos caracteres lidos sem os espaços em branco indicando o total de caracteres encontrados e o total de espaços em brancos encontrados.

Obs: no final mostrar todos os caracteres encontrados numa linha só sem os espaços em brancos.

Utilize a ferramenta linguagem C ++, ou a ferramenta do seu melhor domínio.

Exemplo: Entrada: “Boa noite turma de compiladores”
                                
Saída de tela:          1. - Total de caracteres encontrados: 28
                                2. - Total de espaços em branco encontrados: 04
                                3. – Total de caracteres com espaços em branco encontrados 32 
  4. – Saída na tela sem os espaços em branco:   
            “Boanoiteturmadecompiladores” 
'''

def analisador_de_caracteres(texto):
    # Contadores
    contagem_caracteres = 0
    contagem_espacos = 0
    
    # Lista para armazenar caracteres não espaçados
    caracteres_sem_espacos = []
    
    for caractere in texto:
        if caractere.isspace():
            contagem_espacos += 1
        else:
            caracteres_sem_espacos.append(caractere)
            contagem_caracteres += 1
    
    # Junta a lista de caracteres sem espaços em branco em uma única string
    resultado_sem_espacos = ''.join(caracteres_sem_espacos)

    # Calcula a soma total de caracteres e espaços em branco
    total_caracteres_espacos = contagem_caracteres + contagem_espacos
    
    # Exibe os resultados
    print(f"Sequência dos caracteres lidos sem os espaços em branco: {resultado_sem_espacos}")
    print(f"Total de caracteres encontrados: {contagem_caracteres}")
    print(f"Total de espaços em branco encontrados: {contagem_espacos}")
    print(f"Total de caractres com espaços em branco encontrados: {total_caracteres_espacos}")

# Solicitar entrada do usuário
entrada_usuario = input("Digite uma sequência de caracteres: ")

# Chamar a função para analisar os caracteres
analisador_de_caracteres(entrada_usuario)
