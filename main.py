#! python3

#data structure for languages
#-------------------------------------------
french = {
	'name': 'FR',
	'genders': ['male', 'female']
}
#-------------------------------------------


#class where we store "definitions"
#Definitions = [ {'word': 'toto', 'language': FR}, ... ]
#-------------------------------------------
class Dictionary:

	def __init__(self): #constructor
		self.storage = [] #create instance variable "storage"

	def add_word(self, word, language = french['name'], gender = 'male'): #add a word to the dicitonary
		definition = {}
		definition['word'] = word
		definition['language'] = language
		definition['gender'] = gender

		self.storage.append(definition)

	def find_word(self, word): #find a word in the dictionary
		answer = []
		for definition in self.storage:
			if definition['word'] == word:
				answer.append(definition)			
		return answer #return an array of definitions
#-------------------------------------------


#initialization
#-------------------------------------------
dictionary = Dictionary() #initialize the "database" by instanciating the "dictionary"
#-------------------------------------------


'''
#commented to ease testing

print("Que souhaitez vous faire ?")
print("1 - Sauvegarder un mot")
print("2 - Chercher un mot")
answer = input() #todo use answer
'''

#lines for testing
#-------------------------------------------
dictionary.add_word("toto") 
answer = "2"
#-------------------------------------------


#UI
#-------------------------------------------
if (answer == "1"):
	word = input("Entrez un mot svp : ")
	dictionary.add_word(word)

	print("Etat du dico", dictionary.storage)

else:
	word_to_find = input("Veuillez saisir le mot que vous cherchez :")
	words_found = dictionary.find_word(word_to_find)

	print("Nombre de mots trouvés :", len(words_found))
	print("Mots trouvés :")

	for word in words_found:
		print(word)
#-------------------------------------------
