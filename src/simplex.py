# Bruno Lauand Ferrão - 32217994

import pulp

resolver = pulp.LpProblem("Resolver", pulp.LpMaximize)
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

r = int(input("Digite o número de restrições: "))
v = 2

# Entrada dos coeficientes
for i in range(r):
    print(f"Restrição {i+1}:")
    coefX = int(input("Digite o coeficiente de x: "))
    coefY = int(input("Digite o coeficiente de y: "))
    fo = int(input("Digite o valor da função objetivo: "))
    print("Escolha qual restrição deseja usar (>=, <=, =):")
    while True:
        restricao = input()
        if restricao == '<=':
            resolver += coefX * x + coefY * y <= fo
            break
        elif restricao == '=':
            resolver += coefX * x + coefY * y <= fo
            resolver += coefX * x + coefY * y >= fo
            break
        elif restricao == '>=':
            resolver += coefX * x + coefY * y >= fo
            break
        else:
            print("Restrição inválida, digite: >=, <=, =")

# Função objetivo
print("Função Objetivo:")
coefXFO = int(input("Digite o coeficiente de x: "))
coefYFO = int(input("Digite o coeficiente de y: "))
resolver += coefXFO * x + coefYFO * y

# Resolver o problema
resolver.solve()

print("A solução ótima é:")
print("x = ", pulp.value(x))
print("y = ", pulp.value(y))
print("Função objetivo: ", pulp.value(resolver.objective))
