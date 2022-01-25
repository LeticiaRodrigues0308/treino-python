nivel=input("Digite seu nível: ").upper()
genero=input("Digite seu gênero: ").upper()
resposta="SIM"

while resposta=="SIM":
    if nivel=="ADM":
        if genero=="MASCULINO":
            print("Olá Administrador")
        elif genero=="FEMININO":
            print("Olá administradora")
    elif nivel=="USR":
        if genero=="MASCULINO":
            print("Olá usuário")
        elif genero=="FEMININO":
            print("Olá usuária")
    elif nivel=="GUEST":
            print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta=input("Digite SIM para continuar: ").upper()