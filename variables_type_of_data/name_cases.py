# exercise 2.3 - messagem pessoal
name = "Lucas"
message = "Hello " + name + ", how are you?"
print(message)

# exercise 2.4 - letras maiúsculas e minúsculas em nomes
name = "lucas pires"
print(name.lower())
print(name.upper())
print(name.title())

# exercise 2.5 - citação famosa
message = '\tAbraham Lincoln certa vez disse: '
message+= '"Se eu tivesse oito horas para derrubar uma árvore, passaria seis afiando meu machado."'
print(message)

# exercise 2.6 - citação famosa 2
famous_person = "Abraham Lincoln"
message = '\t' + famous_person + ' certa vez disse: '
message+= '"Só tem o direito de criticar aquele que pretende ajudar"'
print(message)

# exercise 2.7 - removendo espaçoes em branco de nomes
name = "\tLucas \n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
