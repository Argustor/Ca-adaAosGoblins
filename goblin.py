import time
import random

arma = 0
#Caça aos goblins

print("Bem-vindo à caça aos goblins")
time.sleep(5)
print("começando a aventura...")
time.sleep(6)

print("Você acorda em um quarto escuro e sujo, está desarmado e sem saber o que fazer, há apenas um corredor à sua frente")
print("Instruções: escreva 'norte', 'sul', 'leste' ou 'oeste' para andar.")
time.sleep(3)

acao = input("o que você faz?\n")

if (acao == "norte"):
    print("você segue pelo corredor")
else:
    print("você bateu na parede")
    

time.sleep(3)

print("enquanto seguia pelo corredor escuro, um nojento e fedorento goblin pulou à sua frente, não tem para onde ir, terá que lutar")
jogador = input("instruções: aperte 'a' para lançar um dado de 6 lados:\n")

time.sleep(3)

if (jogador == "a"):
    print("você atacou...")
    dado = random.randint(1, 6)
time.sleep(2)
print("o goblin atacou...")
goblin1 = random.randint(1, 6)
time.sleep(2)
print("a sorte decidirá seu destino...")
time.sleep(4)
if(dado > goblin1):
    print("você enxeu o goblin de porrada e o matou")
elif(dado == goblin1):
    print("você e o goblin trocaram socos até morrerem")
else:
    print("o goblin te matou de tanto soco")

time.sleep(5)
if(dado > goblin1):
    print("Após encher o goblin de porrada, você segue pelo corredor escuro")

acao = input("Você se depara em uma bifurcação, você seguirá para 'leste' ou 'oeste?\n")

time.sleep(3)

if(acao == "oeste"):
    print("você segue para oeste, se deparando em uma cozinha imunda, em cima da mesa, um corpo mutilado, com um cutelo afiado cravado no crânio")

elif(acao == "leste"):
    print("você segue para leste, você se depara com uma porta")

time.sleep(3)
acao = input("você pega o machado? [s/n]")

time.sleep(3)
if(acao == "s"):
    arma = 1
    print("você se equipa com o machado")
else:
    print("você não pega o machado")

time.sleep(3)

acao = input("seguir pelo outro caminho? [s/n]")

time.sleep(3)
if(acao == "s"):
    print("você segue para leste, você se depara com uma porta")

time.sleep(3)
acao = input("você abre a porta?[s/n")

time.sleep(3)
if (acao == "s"):
    print("você abriu a porta...")

time.sleep(5)

if (arma == 1):
    print("goblins te cercaram, mas você está armado com o cutelo e, graças a isso recebe +1 de ataque. Aperte 'a' para atacar:\n")
time.sleep(3)

if (jogador == "a"):
  
    dado = random.randint(1, 6) + 1
    print("você atacou...")
    
    print("os goblins atacaram...")
    goblin = random.randint(1, 6)

    print("a sorte decidirá seu destino...")
    time.sleep(5)

if (dado > goblin):
    print("Você massacrou as criaturas da noite e sobreviveu ao pesadelo")

elif( dado == goblin):
    print("a batalha foi sangrenta, os goblins morreram e você também")


else:
    print("os goblins arrancaram a sua pele")