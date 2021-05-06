#Calculadora em Python
#Variável para manter a repetição
run=1
#Repetição da calculadora
while(run):

	#Cabeçalho explicativo
	print('***---***---***---***---***---***---***---***---***---***---***---***')
	print("	    __  ____ _        __ __ __ _      ____ ___    ___  ____   ____ ")
	print("	   /  ]/    | |      /  ]  |  | |    /    |   \\  /   \|    \ /    |")
	print("	  /  /|  o  | |     /  /|  |  | |   |  o  |    \\|     |  D  )  o  |")
	print("	 /  / |     | |___ /  / |  |  | |___|     |  D  |  O  |    /|     |")
	print("	/   \\_|  _  |     /   \\_|  :  |     |  _  |     |     |    \|  _  |")
	print("	\\     |  |  |     \\     |     |     |  |  |     |     |  .  \  |  |")
	print("	 \\____|__|__|_____|\\____|\\__,_|_____|__|__|_____|\___/|__|\_|__|__|")
	print("")
	print('***---***---***---***---***---***---***---***---***---***---***---***')

	print('***---***---***---***---***---***---***---***---***---***')
	print('Escolha dentre as opções abaixo...')
	print('1 - Adição')
	print('2 - Subtração')
	print('3 - Divisão')
	print('4 - Multiplicação')
	print('***---***---***---***---***---***---***---***---***---***')
	print('   Para sair Digite qualquer tecla diferente das opções')
	print('***---***---***---***---***---***---***---***---***---***')
	# Entrada de opção via teclado
	choice = input('Sua escolha é: ')
	print('')
	print('')
	print('')
	
	# Estrutura condicional
	# Condição de Adição
	if (choice == '1'):
		print('Você Escolheu Adição!!')
    	#Entrada de dados para adição
		num1 = float(input('Digite o primeiro Valor: '))
		num2 = float(input('Digite o segundo Valor: '))
		#Operação de adição
		resultado=(num1+num2)
		print("O Resultado é %2.f." %(resultado))
	#Condição de Subtração
	elif (choice == '2'):
		print('Você Escolheu Subtração!!')
		#Entrada de dados para subtração
		num1 = float(input('Digite o primeiro Valor: '))
		num2 = float(input('Digite o segundo Valor: '))
		#Operação de subtração
		resultado=(num1-num2)
		print("O Resultado é %2.f." %(resultado))
	#Condição de Divisão
	elif (choice == '3'):
		print('Você Escolheu Divisão!!')
		#Entrada de dados 
		num1 = float(input('Digite o primeiro Valor: '))
		num2 = float(input('Digite o segundo Valor: '))
		resultado=(num1/num2)
		print("O Resultado é %2.f." %(resultado))
	#Condição de Multiplicação
	elif (choice == '4'):
		print('Você Escolheu Multiplicação!!')
		num1 = float(input('Digite o primeiro Valor: '))
		num2 = float(input('Digite o segundo Valor: '))
		resultado=(num1*num2)
		print("O Resultado é %2.f." %(resultado))
	#Fechar Calculadora
	elif (choice == '0'):
		run = 0
	#Caracter digitado inválido
	else:
		print('Opção Inválida')
