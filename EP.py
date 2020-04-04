import random
dado1= random.randint(1,6)
dado2= random.randint(1,6)
dad01= random.randint(1,6)
dad02= random.randint(1,6)
s0ma= dad01 + dad02
soma= dado1 + dado2
fichas= 50
while fichas != 0:
    jogar= str(input("Deseja apostar?(s/n) "))
    if jogar == "s":
        print("Vamos começar o jogo (Fase de Come Out)")
        print("Você tem {} fichas" .format(fichas))
        aposta= int(input ("Quantas fichas deseja apostar?"))
        while aposta > fichas:
            print("Valor apostado, incorreto")
            aposta= int(input ("Quantas fichas deseja apostar?"))
        tipo1= int (input("Qual tipo de aposta: \n [1]Pass Line Bet \n [2]Field \n [3]Any Craps \n [4]Twelve \n Digite 1 tipo de aposta que quer fazer: "))
        pergunta= str(input("Deseja fazer outro tipo de aposta?(s/n) "))
        if pergunta == "s":
            tipo2= int (input("Qual tipo de aposta: \n [1]Pass Line Bet \n [2]Field \n [3]Any Craps \n [4]Twelve \n Digite 1 tipo de aposta que quer fazer: "))
            pergunta= str(input("Deseja fazer outro tipo de aposta?(s/n) "))
            if pergunta == "s":
                tipo3= int (input("Qual tipo de aposta: \n [1]Pass Line Bet \n [2]Field \n [3]Any Craps \n [4]Twelve \n Digite 1 tipo de aposta que quer fazer: "))
                pergunta= str(input("Deseja fazer outro tipo de aposta?(s/n) "))
                if pergunta == "s":
                    tipo4= int (input("Qual tipo de aposta: \n [1]Pass Line Bet \n [2]Field \n [3]Any Craps \n [4]Twelve \n Digite 1 tipo de aposta que quer fazer: "))
                elif pergunta == "n":
                    print("Vamos para o jogo")
            elif pergunta == "n":
                print("Vamos para o jogo")
        elif pergunta == "n":
            print("Vamos para o jogo")
            print("=====Come Out=====")
        numero= int(input("Escolha um numero para apostar:(0/12) "))
        if tipo1 == 1:
            if soma == 7 or 11:
                print(soma)
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+10))
            elif soma == 2 or 3 or 12:
                print("Você perdeu!")
                print("Agora você tem {} fichas" .format(fichas-aposta))
            elif soma == 4 or 5 or 6 or 8 or 9 or 10:
                point= soma
                print(point)
                print("=====Point=====")
                print("O valor apostado é {}" .format(aposta))
                if s0ma == point:
                    print("Vc ganhou")
                    print("Agora você tem {} fichas" .format(fichas+aposta))
                elif s0ma == 7:
                    print("Você perdeu!")
                    print("Agora você tem {} fichas" .format(fichas-fichas))
        elif tipo1 == 2:
            if soma ==  5 or 6 or 7 or 8:
                print("Você perdeu!")
                print("Agora você tem {} fichas" .format(fichas-fichas))
            elif soma == 3 or 4 or 9 or 10 or 11:
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+aposta))
            elif soma == 2:
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+aposta*2 +aposta))
            elif soma == 12:
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+aposta*3 +aposta))
        elif tipo1 == 3:
            if soma == 2 or 3 or 12:
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+aposta*7))
            else:
                print("Você perdeu!")
                print("Agora você tem {} fichas" .format(fichas-fichas))
        elif tipo1 == 4:
            if soma == 12:
                print("Vc ganhou")
                print("Agora você tem {} fichas" .format(fichas+aposta*30))
            else:
                print("Você perdeu!")
                print("Agora você tem {} fichas" .format(fichas-fichas))
            
    else:
        break
