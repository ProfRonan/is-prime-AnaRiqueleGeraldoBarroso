num = int(input("Digite um número: "))
cont = 0
if num<=0:
    print("Número inválido")
else:    
    for c in range(1, num+1):
        if num%c==0:
            cont+=1
    if cont==2:
        print("Primo")
    else:
        print("Não primo")