# *********questao 1 ***********
'''p1= 10+20*30
print(p1) 
p2=4**2 / 3
print(p2)
p3=(9**4 +2) * 6-1
print(p3)
p4=(9*4 + 2 )**4 +(10/1)
print(p4)'''
#questao 2
'''def soma(a,b):
    vp=(2*a)*(3*b)
    print(f'o valor do produto do dobro de {a} pelo triplo de {3} é: {vp}')
a=int(input("insira o valor de a"))
b=int(input("insira o valor de a"))
soma(a,b)'''
#questao 3
#questao 4
'''def tempo(dias,anos):
    totald=dias*10/60
    totala=totald*365*anos
    print("voce perdeu ao longo desses anos{:.0f} dias ".format(totala))

dias=int(input("Quantos cigarros ao dia você usa?"))
anos=int(input("A quantos anos você fuma?"))
totald=dias*0.16
totala=totald*365*anos
tempo(dias,anos)'''
#questao 5
'''def quantidade(km,dias):
    somakm=km*0.15
    somadia=dias*60
    total=somakm*somadia
    print(f'voce rodou {km}km e ficou {dias} dias com o veiculo,portanto o valor a ser pago é: {total:.2f}')
km=int(input("quantos km ce percorreu"))
dias=int(input("quantos dias ce ficou com o veiculo"))
quantidade(km,dias)'''
#questao 6
#questao 7
'''def i(idade):
    if idade>=18:
        print ("você já pode encher a cara de cachaça")
    else:
        print("Aguenta mais um pouco")
        
idade=int(input("Qual a sua idade : "))
i(idade)'''
#questao 9
'''def n(nome1,nome2):
    if len(nome1)==len(nome2):
        print("verdadeiro")
    else:
        print("false")
nome1=input("insira um nome")
nome2=input("insira um nome")
n(nome1,nome2)'''
#questao 10
#questao 11
'''a=int(input("qual o tamanho do lado A"))
b=int(input("qual o tamnho do lado  B"))
base=int(input("qual o tamanho da base"))
area= base*a/2
perimetro=a+b+base
print(f' os medidas do triangulos são ladoA:{a} ladoB:{b} e sua base é :{base}\n')
print(f' A area do triangulo é {area} e seu perimetro é {perimetro}')'''
#questao 12
'''def soma(raio):
    area=3.14 * (raio**2)
    circu= 2* 3.14 * raio
    print(f' a area do raio é {area} e a  circuferencia é {circu}')

raio= float(input("insira o valor do raio"))
soma(raio)'''
#questao 13
'''Crie uma função que resolva a seguinte equação do segundo grau X² + 3x +3 = 0. Dica para calcular a raiz quadrada -> num ** 0.5'''
#questao 14
'''def patas(ga,v,p):
    galinhas=2*ga
    vacas=4*v
    porcos=4*p
    soma=galinhas+vacas+porcos
    return soma
ga=int(input("quantas galinha existem na fazenda?"))
v=int(input("quantas vacas existem  na fazenda?"))
p=int(input("quantos porcos existem na fazenda"))

x= patas(ga,v,p)
print(f' somando todos os animais existem {x} patas nessa fazenda')'''























