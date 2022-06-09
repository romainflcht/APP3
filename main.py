# Copyright : romain_flcht

import matplotlib.pyplot as plt
from language_analysis.FILE_PATHS import LANGUAGE_TEXT_PATH
from ASCII_art import LOGO
from language_analysis.fonctions import parse_file, get_most_used_char
# pip install matplotlib OR pip3 install matplotlib

TEXT_PATH = 'text.txt'
NUM_MOST_FREQ_CHAR = 5
SHOW_HIST = True

if __name__ == '__main__':
    print(LOGO, end='\n\n\n')
    # Récupérations des occurences des caractères pour chaques langues.
    stats = {}
    for language in LANGUAGE_TEXT_PATH:
        for file in LANGUAGE_TEXT_PATH[language]:
            stats[language] = get_most_used_char(parse_file(file), NUM_MOST_FREQ_CHAR)

    # Affichage en mode graphique ou console.
    if SHOW_HIST:
        for language in stats:
            plt.title(f'{language}')
            plt.ylabel('Occurences des caractères (en %)')
            plt.xlabel(f'Les {NUM_MOST_FREQ_CHAR} caractères les plus fréquents')
            plt.bar(stats[language].keys(), stats[language].values(), color='lightskyblue')
            plt.show()
    else:
        print('Occurences des caractères dans chaques langues :')
        print('═' * 256)
        for language in stats:
            print(f'\t• {language} -> ', end='')
            for char in stats[language]:
                print(f'{char} : {stats[language][char]}%', end=' | ')

            print('\n' + '═' * 256)

    # Récupération des occurences du fichier à analyser.
    text = get_most_used_char(parse_file(TEXT_PATH), NUM_MOST_FREQ_CHAR)

    # Affichage en mode graphique ou console.
    if SHOW_HIST:
        plt.title(f'Texte entré')
        plt.ylabel('Occurences des caractères (en %)')
        plt.xlabel(f'Les {NUM_MOST_FREQ_CHAR} caractères les plus fréquents')
        plt.bar(text.keys(), text.values(), color='lightskyblue')
        plt.show()
    else:
        print('Occurences des caractères dans le texte entré : \n\t', end='')
        for char in text:
            print(f'| {char} : {text[char]}', end=' | ')
        print('\n')

    print('Comparaison avec les fichiers de réferences : ')

    # Comparaison des données du texte à analyser et des textes de réferences.
    pourcent_match = {elt: 0 for elt in stats}
    for language in stats:
        pourcent = []
        for char in text:
            # Calcul du pourcentage de proximité entre les lettres du fichier à analyser et du fichier de réference.
            if stats[language].get(char) is not None:
                pourcent.append(text[char] * 100 / stats[language].get(char))

            else:
                # Si le caractère du texte à analyser n'est pas dans le texte de réference alors on ajoute 0%
                pourcent.append(0)

        somme = 0

        # Calcul de la moyenne de chaque lettre pour donner le pourcentage final.
        for elt in pourcent:
            somme += elt

        # Ajout du résultat dans un dictionnaire.
        pourcent_match[language] = somme / len(pourcent)
        print(f'\t• Le texte entré ressemble à {(somme / len(pourcent)):.2f}% à du {language}')

    maximum_value = 0
    maximum_key = ''

    # Recherche de la langue la plus proche du texte à analyser.
    for language in pourcent_match:
        if pourcent_match[language] > maximum_value:
            maximum_value = pourcent_match[language]
            maximum_key = language

    # Affichage final.
    print('\n\n═ Résultat ' + '═' * 245)
    print(f'La langue detecté pour le texte entré est : {maximum_key} ({maximum_value:.2f}%)')
