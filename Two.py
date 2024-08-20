'''
Atividade: Construa um analisador, com as seguintes funções:

- Função1: Leia a entrada de caracteres com letras maiúsculas e minúsculas. 

- Função2: Reconheça, considere e modifique os caracteres encontrados das letras maiúsculas e minúsculas como equivalentes isto é: 

Exemplos: 

- Digite as strings em letras maiúscula: BEGIN, mostrar na saída da tela Minúscula: begin,

- Digite as strings letras em minúsculas: begin, mostrar na saída da tela maiúsculas: BEGIN,

- Digite as strings em letras maiúsculas e minúscula: BEgin, saída maiúscula e minúscula:  BEGIN, begin, beGIN. 
'''

def convert_to_uppercase(s):
    return s.upper()

def convert_to_lowercase(s):
    return s.lower()

def swap_cases(s):
    return s.swapcase()

def menu(user_input):
    while True:
        print("\n--- Menu ---")
        print("1. Transformar a string para maiúsculas")
        print("2. Transformar a string para minúsculas")
        print("3. Trocar entre minúsculas e maiúsculas")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1/2/3/4): ")
        
        if choice == '4':
            print("Saindo...")
            break
        
        if choice == '1':
            print("Saída maiúscula:", convert_to_uppercase(user_input))
        elif choice == '2':
            print("Saída minúscula:", convert_to_lowercase(user_input))
        elif choice == '3':
            print("Saída da troca:", swap_cases(user_input))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    user_input = input("Digite a string: ")
    menu(user_input)
