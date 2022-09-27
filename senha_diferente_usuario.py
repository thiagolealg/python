print("Realize seu cadastroeu cadastro:")
usuario=str(input("indique o nome de usuário "))
senha=str(input("digite sua senha"))
while usuario==senha:
	print("Nome do usuário não poderá ser igual ao número da senha. Tente novamente")
	usuario=str(input("indique o nome de usuário "))
	senha=str(input("digite sua senha"))
else:
	print("cadastrado efetuado com sucesso")




