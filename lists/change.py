# exercise 3.4 - lista de convidados
print("Exercício 3.4 - Lista de convidados")
guests = ['Alexandre', 'Taylor', 'CR7']
print("Querido, " + guests[0] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[1] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[2] + ", seria uma honra ter sua presença neste jantar.")

# exercise 3.5 - alterando a lista de convidados
print("\nExercício 3.5 - alterando a lista de convidados")
guest_remove = 'Taylor'
guests.remove(guest_remove)
guests.append('Messi')
print('Lista Atualizada')
print("Querido, " + guests[0] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[1] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[2] + ", seria uma honra ter sua presença neste jantar.")
print("Infelizmente houve uma desistência do nosso querido amigo " + guest_remove + ".")

# exercise 3.6 - mais convidados
print("\nExercício 3.6 - Mais convidados")
guests.insert(0, 'Marcos')
guests.insert(2, 'Ivaneide')
guests.append('André')
print('Nossa Lista aumentou')
print("Querido, " + guests[0] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[1] + ", seria uma honra ter sua presença neste jantar.")
print("Querida, " + guests[2] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[3] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[4] + ", seria uma honra ter sua presença neste jantar.")
print("Querido, " + guests[5] + ", seria uma honra ter sua presença neste jantar.")
message = "Caros amigos, teremos uma mesa maior para jantar, com isso aumentamos nossa lista de "
message += "convidados, sendo eles " + guests[0] + ", " + guests[2] + " e " + guests[-1] + "."
print (message)

# exercise 3.7 - reduzindo a lista de convidados
print("\nExercício 3.7 - Removendo a lista de convidados")
print("Caros amigos, sinto muito informar que teremos vagas para apenas 2 pessoas em nosso jantar.")
removed_person = guests.pop(1)
print("Meu caro amigo " + removed_person + ", sinto muito mas infelizmente seu convite foi cancelado")
removed_person = guests.pop()
print("Meu caro amigo " + removed_person + ", sinto muito mas infelizmente seu convite foi cancelado")
removed_person = guests.pop()
print("Meu caro amigo " + removed_person + ", sinto muito mas infelizmente seu convite foi cancelado")
removed_person = guests.pop()
print("Meu caro amigo " + removed_person + ", sinto muito mas infelizmente seu convite foi cancelado")

print(guests[0] + ", sua presença é indispensável, e conto com sua presença em nosso jantar.")
print(guests[1] + ", sua presença é indispensável, e conto com sua presença em nosso jantar.")

del guests[0]
del guests[0]

print(guests)


