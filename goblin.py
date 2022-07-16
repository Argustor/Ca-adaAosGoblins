import time
import random

arma = 0


print("Bem-vindo à caça aos goblins")
time.sleep(3)
print("começando a aventura...")
time.sleep(6)
print("Você acorda em um quarto escuro e sujo, está desarmado e sem saber o que fazer, há apenas um corredor à sua frente")
print("Instruções: escreva 'norte', 'sul', 'leste' ou 'oeste' para andar.")
time.sleep(1)

acao = input ("o que você faz?\n")

while (acao != "norte"):
    print("você bate na parede")
    acao = input ("o que você faz?\n")

if (acao == "norte"):
    print("você segue pelo corredor...")

time.sleep(3)


print("enquanto seguia pelo corredor escuro, um nojento e fedorento goblin pulou à sua frente, não tem para onde ir, terá que lutar")
jogador = input("instruções: aperte 'a' para atacar:\n")

time.sleep(2)


if (jogador == "a"):
    print("você atacou...")
    dado = random.randint(1, 6)
time.sleep(1)
print("o goblin atacou...")
goblin1 = random.randint(1, 3)
time.sleep(1)
print("a sorte decidirá seu destino...")
time.sleep(4)
if(dado > goblin1):
    print("você enxeu o goblin de porrada e o matou")
    print("Após encher o goblin de porrada, você segue pelo corredor escuro")

elif(dado == goblin1):
    print("você e o goblin trocaram socos até morrerem")
else:
    print("o goblin te matou de tanto soco")
    
if(dado <= goblin1):
    time.sleep(3)
    print("você morreu")
    

if (dado > goblin1):
    acao = input("Você se depara em uma bifurcação, você seguirá para 'leste' ou 'oeste'?\n")
    if (acao == "leste"):
        print("você segue para lese, você se depara com uma porta")
        acao = input("você abre a porta?[s/n]")
    if(acao == "oeste"):
        print("você segue para oeste, se deparando em uma cozinha imunda, em cima da mesa, um corpo mutilado, com um cutelo afiado cravado no crânio")
        acao = input("você pega o cutelo? [s/n]")
    
        if(acao == "s"):
            arma = 1
            print("você se equipa com o cutelo")
        else:
            print("você não pegua o cutelo")

        acao = input("não há mais nada para fazer aqui, seguir para outro caminho? [s/n]")

        if(acao == "s" ):
            print("você segue para leste, você se depara com uma porta")
            acao = input("vocÊ abre a porta?[s/n]")
        
        while (acao == "n"):
            print("você continua na cozinha...")
            acao = input("não há mais nada para fazer aqui, seguir para outro caminho? [s/n]")
            print("você segue para o leste, você se depara com uma porta")
            acao = input("você abre a porta?[s/n]")

    while (acao == "n"):
        print("você fica encarando a porta")
        acao = input ("você abre a porta?[s/n]")

if(acao == "s" or acao == "leste"):
    print("você abriu a porta...")


    while (arma == 1):
        acao = input("goblins te cercaram, mas você está armado com o cutelo e, graças a isso recebe +1 de ataque. Aperte 'a' para atacar:\n")
    
        if (jogador == "a"):
  
            dado = random.randint(1, 6) + 1
            print("você atacou...")
            time.sleep(1)
            print("os goblins atacaram...")
            goblin = random.randint(1, 6)
            time.sleep(1)
            print("a sorte decidirá seu destino...")
            time.sleep(5)

        if (dado > goblin):
            print("Você massacrou as criaturas da noite e sobreviveu ao pesadelo")
            break
        elif( dado == goblin):
            print("a batalha foi sangrenta, os goblins morreram e você também")
            break
        else:
            print("os goblins arrancaram a sua pele")
            print("você morreu")
            break
while (arma == 0):
        print("os goblins arrancaram a sua pele")
        break

  
