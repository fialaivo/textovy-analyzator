"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ivo Fiala
email: fiala.ivo@spszr.cz
discord: ivofiala
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

reg_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123" }
line = "-" * 40

user = input("username:")
password = input("password:")
print(line)

if (reg_users.get(user) and password == reg_users.get(user)):
	print(f"Welcome to the app, {user}")
	print("We have 3 texts to be analyzed.")
	print(line)
	text_number=input("Enter a number btw. 1 and 3 to select:")
	if text_number.isdigit() and (int(text_number) > 0 and int(text_number) < 4):
		text_number = int(text_number)
		print(line)

		words =  TEXTS[text_number - 1].replace(",","").replace(".","").split()
		count_words = len(words)
		print(f"There are {count_words} words in the selected text.")

		count_istitle = 0
		count_isupper = 0
		count_islower = 0
		count_isnumeric = 0
		sum = 0
		len_words = list()
		count_len_words = list()
		max_length = 0
		for i in range (count_words):
			length = len(words[i])
			if words[i].istitle():
				count_istitle += 1
			if words[i].isupper() and (not (words[i][0].isdigit())) :
				count_isupper += 1
			if words[i].islower():
				count_islower += 1
			if words[i].isnumeric():
				count_isnumeric += 1
				sum += int(words[i])
			if length > max_length:
				max_length = length
			len_words.append(length)
		print(max_length)
		print(len_words)
		for i in range (max_length+1):
			count_len_words.append(len_words.count(i))
			print(count_len_words)
		print(f"There are {count_istitle} titlecase words.")
		print(f"There are {count_isupper} uppercase words.")
		print(f"There are {count_islower} lowercase words.")
		print(f"There are {count_isnumeric} numeric strings.")
		print(f"The sum of all the numbers {sum}")
		print(line)
		print(f"LEN|{"OCCURENCES":^18}|NR.")
		print(line)
		
		for i in range (1, max_length+1):
			pocet_hvezdicek = "*" * count_len_words[i]
			if count_len_words[i] != 0:
				print(f" {i:>2}|{"*" * count_len_words[i]:<18}|{count_len_words[i]}")
	else:
		print("Invalid input, terminating the program..")
else:
	print("unregistered user, terminating the program..")