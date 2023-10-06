# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import os

# Ottieni il percorso della directory corrente
current_directory = os.path.dirname(os.path.abspath(__file__))
# Costruisci il percorso completo al file CSV
file_path = os.path.join(current_directory, 'nato_phonetic_alphabet.csv')

import pandas
data = pandas.read_csv(file_path)

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()