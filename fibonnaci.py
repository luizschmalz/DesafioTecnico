
numero = 5 #numero a ser escolhido

def fibonacci_sequence(n):
    fib_seq = [0, 1]
    
    #  geração da sequencia de fibbonaci, depois disso vamos verificar se o numero escolhido está na sequencia ou não
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq

def is_fibonacci(num):
    fib_seq = fibonacci_sequence(num)
    
    if num in fib_seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# exemplo de uso
print(is_fibonacci(numero))