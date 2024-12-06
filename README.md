# Método simplex em python

## Sobre
Este projeto é uma implementação do Método Simplex utilizando a biblioteca Pulp do Python. O código resolve problemas de programação linear para maximizar uma função objetivo sujeita a restrições. Ele permite que o usuário insira os coeficientes e restrições diretamente pelo terminal, fornecendo a solução ótima para o problema formulado.

## Requisitos
- Python 3.6+
- Biblioteca Pulp

## Funcionamento
1. **Definição das variáveis**: O programa trabalha com duas variáveis x e y, que possuem limites inferiores iguais a 0 (não negatividade).

2. **Entrada de restrições**: O usuário pode adicionar múltiplas restrições lineares com coeficientes definidos para x e y.

3. **Função objetivo**: O programa solicita os coeficientes da função objetivo que será maximizada.

4. **Resolução**: Após a entrada dos dados, o método simplex resolve o problema e exibe:
    - Os valores ótimos de x e y.
    - O valor máximo da função objetivo.

## Autor
- Bruno Ferrão
