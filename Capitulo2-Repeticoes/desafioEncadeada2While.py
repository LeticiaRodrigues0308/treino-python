nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca_infectocontagiosa=="NAO":
    print("Encaminhe o paciente para sala BRANCA")
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
