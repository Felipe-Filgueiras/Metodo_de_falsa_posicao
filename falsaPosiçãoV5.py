#equação do exemplo: f(x) = (x ** 3)- 9*x +3, a = 0, b = 1, erro máximo = 0.01, iterações máximas = 10
#(e**-x)*((3.2*sin(x))-(0.5*cos(x)))

from math import *

def metodo_fp(func, a, b, erro_aceito, max_it):

    def f(x):
        f = eval(func)
        return f
    
    i = 0
    erro = ()
    loopCondition = True

    while loopCondition == True:

        xi = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            print("Erro! Método de falsa posição não é válido!")
            quit()
        
        elif f(xi) * f(a) < 0:
            erro = abs((xi - b)/xi)
            if i == 0:
                print(f"i={i+1}, a = {a}, b = {b}, xi = {xi}, f(a) = {f(a)}, f(b) = {f(b)}, f(xi) = {f(xi)}")
            else:
                print(f"i={i+1}, a = {a}, b = {b}, xi = {xi}, f(a) = {f(a)}, f(b) = {f(b)}, f(xi) = {f(xi)}, erro = {erro}")
            b = xi
            i = i + 1
            if i == max_it:
                print("Erro de caso 1! Muitas iterações!" , str(i))
                quit()
        
        elif f(xi) * f(b) < 0:
            erro = abs(xi - a)
            if i == 0:
                print(f"i={i+1}, a = {a}, b = {b}, xi = {xi}, f(a) = {f(a)}, f(b) = {f(b)}, f(xi) = {f(xi)}")
            else:
                print(f"i={i+1}, a = {a}, b = {b}, xi = {xi}, f(a) = {f(a)}, f(b) = {f(b)}, f(xi) = {f(xi)}, erro = {erro}")
            a = xi
            i = i + 1
            if i == max_it:
                print("Erro de caso 2! Muitas iterações!" , str(i))
                quit()

        
        else:
            print("Algo deu errado!")
            quit()
        
        if erro <= erro_aceito:
            loopCondition = False
    else:
        if f(xi) * f(a) < 0:
            print(f"A raiz aproximada é {b}.")
        
        elif f(xi) * f(b) < 0:
            print(f"A raiz aproximada é {a}.")
        
print("Método de falsa posição em python.")
print("Por favor seguir as instruções:")
print("Para sen use sin(), para cos use cos(), para tan use tan()")
print("Não esqueça de usar parenteses quando necessário.")
print()

inp1 =input("Insira a função f(x): ")
inp2 =input("Insira o limite inferior: ")
inp3 =input("Insira o limite superior: ")
inp4 =input("Insira o erro máximo aceito: ")
inp5 =input("Insira o número máximo de iterações: ")

inp1 = str(inp1)
inp2 = float(inp2)
inp3 = float(inp3)
inp4 = float(inp4)
inp5 = float(inp5)

metodo_fp(inp1, inp2, inp3, inp4, inp5)