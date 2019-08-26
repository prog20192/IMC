#CALCULO DE IMC 2.0
nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if imc < 17.0:
    print('Seu IMC é {:.2f}! Você está muito abaixo do peso!'.format(imc))
elif imc >=17.0 and imc <= 18.5:
    print('Seu IMC é {:.2f}! Você está abaixo do peso normal!'.format(imc))
elif   imc >= 18.5 and imc <= 25.0:
    print('Seu IMC é {:.2f}! Você está dentro do normal!'.format(imc))
elif imc >= 25.0 and imc <= 30.0:
    print('Seu IMC é {:2.f}! Você está acima do peso!'.format(imc))
else:
    print('Seu IMC é {:.2f}! Você está muito acima do peso!'.format(imc))

#Obrigado!
