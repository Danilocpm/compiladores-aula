'''
EXERCÍCIO – Projetar um analisador léxico para uma calculadora simples com números naturais e reais e operações básicas (soma, subtração, multiplicação e divisão)

❑Questões a considerar:
1. Que símbolo usar como separador de casadecimais?
2. A calculadora usa representação monetária?
3. A calculadora aceita espaços entre os operandos eoperadores?
4. O projetista é quem decide sobre as características desejáveis do compilador ou interpretador. Para a maioria das linguagens deprogramação existem algumas convenções quedevem ser respeitadas

❑ Exemplo - seja a cadeia 3.2 + (2 * 12.01), o
analisador léxico teria como saída:

3.2 => número real
+ => operador de soma
( => abre parênteses
52 => número natural
* => operador de multiplicação
12.01 => número real
) => fecha parênteses

1. Definição do Alfabeto
= {0,1,2,3,4,5,6,7,8,9,.,(,),+,-,*,/,\b}
– OBS.: projetista deve considerar TODOS os símbolos que são necessários para formar os padrões

2. Listagem dos tokens
– OPSOMA: operador de soma
– OPSUB: operador de subtração
– OPMUL: operador de multiplicação
– OPDIV: operador de divisão
– AP: abre parênteses
– FP: fecha parênteses
– NUM: número natural/real 

• OBS.: projetista deve considerar tokens especiais e cuidar para que cada token seja uma unidade significativa para o problema

3. Especificação dos tokens com definições regulares
– OPSOMA : +
– OPSUB : -
– OPMUL : *
– OPDIV : /
– AP : (
– FP : )
– NUM : [0-9]+.?[0-9]*

OBS.: Cuidar para que as definições regulares reconheçam padrões claros, bem formados e definidos
'''

import re
# Define as expressões regulares para cada token
token_specification = [
('NUM_REAL', r'[0-9]+\.[0-9]+'), # Números reais (exemplo: 2.5)
('NUM_INT', r'[0-9]+'), # Números inteiros (exemplo: 2)
('OPSOMA', r'\+'), # Operador de soma
('OPSUB', r'-'), # Operador de subtração
('OPMUL', r'\*'), # Operador de multiplicação
('OPDIV', r'/'), # Operador de divisão
('AP', r'\('), # Abre parênteses
('FP', r'\)'), # Fecha parênteses
('SKIP', r'[ \t\n]+'), # Espaços e quebras de linha
('MISMATCH', r'.'), # Qualquer outro caractere
]
# Compila as expressões regulares em um único padrão
master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in
token_specification)
master_re = re.compile(master_pattern)

def lexer(code):
    for match in master_re.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue  # This is fine if we're inside a loop
        if kind == 'MISMATCH':
            raise RuntimeError(f'Caractere inesperado: {value}')
        yield kind, value
        
# Solicita a entrada do usuário
user_input = input('Digite a expressão matemática: ')
# Testando o lexer com a entrada do usuário
print('Análise léxica:')
for token in lexer(user_input):
    print(token)