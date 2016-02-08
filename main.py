class Definitions:

	def __init__(self):
		self.storage = []

	def add_word(word, language = "FR"):
		definition = {}
		definition["word"] = word
		definition["language"] = language

		Definitions.storage.append(definition) #not working !!!!!


'''
#comment to ease testing

print("Que souhaitez vous faire ?")
print("1 - Sauvegarder un mot")
print("2 - Chercher un mot")
answer = input() #todo use answer
'''
dictionary = Definitions() #initialize the "database"

answer = "1"

if (answer == "1"):
	word = input("Entrez un mot svp : ")
	dictionary.add_word(word)

	print("Etat du dico", dictionary.storage)

else:
	0
	#word_to_find = input("Veuillez saisir le mot que vous cherchez :")
