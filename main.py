class Definition:
	def __init__(self, word):
		self.word = word

	def print_word(self):
		return self.word

'''
#comment to ease testing

print("Que souhaitez vous faire ?")
print("1 - Sauvegarder un mot")
print("2 - Chercher un mot")
answer = input() #todo use answer
'''

answer = "1"

if (answer == "1"):
	word = input("Entrez un mot svp : ")

	definition = Definition(word)
	print("Le mot rentré est", definition.print_word) #problem ! Does not return a string, but an object ...

else:
	print("Fonction non encore implémentée")
