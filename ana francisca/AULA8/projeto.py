print("Bem-vindo ao Shopping.")
acesso=input("Qual será a forma de acesso? tag ou ticket?  ")
ticket=1
Tag=2
print("Ticket = 1 e Tag = 2")
print("Acesso liberado")

if acesso ==1:
    print(f"Acesso Liberado")

elif acesso ==2:
    print("Pressione o botão para o Ticket sair")
    placa=input(f"Digite a placa do carro")

else:
    print("ERRO!")    
