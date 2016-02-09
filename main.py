#! python3
class Definitions:

	def __init__(self):
		self.storage = [] #create instance variable "storage"

	def add_word(self, word, language = "FR"):
		definition = {}
		definition["word"] = word
		definition["language"] = language

		self.storage.append(definition)


'''
#comment to ease testing

print("Que souhaitez vous faire ?")
print("1 - Sauvegarder un mot")
print("2 - Chercher un mot")
answer = input() #todo use answer
'''
dictionary = Definitions() #initialize the "database" by instanciating the "dictionary"

answer = "1"

if (answer == "1"):
	word = input("Entrez un mot svp : ")
	dictionary.add_word(word)

	print("Etat du dico", dictionary.storage)

else:
	0
	#word_to_find = input("Veuillez saisir le mot que vous cherchez :")
