metro = float(input("Digite o valor de metros: ")) #o float é uma função que converte uma string em um número decimal.
centimetro = metro * 100
print(f"{metro} metros é igual a {centimetro} centímetros.")

import cowsay #o import cowsay é uma biblioteca que permite criar mensagens engraçadas com animais.

cowsay.trex("Dracarys")
cowsay.dragon("Dracarys")
cowsay.cow("Dracarys")
cowsay.tux("Dracarys")
cowsay.trex("Dracarys")

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

    semaforo = int(input("informe a cor do semaforo (1-vermelho, 2-amarelo, 3-verde): "))
if semaforo == 1: #o if é uma estrutura de controle de fluxo que permite executar um bloco de código se uma condição for verdadeira.
        print("Pare!")
elif semaforo == 2: #o elif é uma estrutura de controle de fluxo que permite testar várias condições.
        print("Atenção!")
elif semaforo == 3:
            print("Siga!")
else: # o else é uma estrutura de controle de fluxo que permite executar um bloco de código se nenhuma das condições anteriores for verdadeira.
        print("Cor inválida!")

        opção = 2 
        match opção: #o match é uma estrutura de controle de fluxo que permite comparar um valor com vários padrões possíveis.
            case 1:
                print("Opção 1 selecionada.")
            case 2:
                print("Opção 2 selecionada.")
            case 3:
                print("Opção 3 selecionada.")
            case _:
                print("Opção inválida.")



for i in range(5, 55, 2):
    print("numero:", i) #o i é o contador do loop, que vai de 5 até 55, pulando de 2 em 2.

