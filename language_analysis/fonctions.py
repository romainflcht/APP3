# Copyright : romain_flcht

def parse_file(file: str) -> list:
    """
    :param file: Chaine de caractère correspondant au chemin du fichier texte.
    :return: Renvoie une liste contenant chaque caractère du fichier transformé en entier ASCII.
    """
    parsed_tab = []
    with open(file, 'r', encoding='utf-8-sig') as file_to_read:
        file_content = file_to_read.read()

    # Suppression des caractères de retour à la ligne, espace... Et convertion de chaque caractère en ASCII.
    for index in range(1, len(file_content)):
        character = file_content[index].lower()
        if character not in ' \n-.,\'"\t':
            parsed_tab.append(ord(file_content[index].lower()))

    # Renvoie du tableau mis en forme.
    return parsed_tab


def counting_sort(parsed_tab: list) -> list:
    """
    :param parsed_tab: Liste de caractère converti en ASCII.
    :return: Renvoie un histogramme des caractères dans cette liste.
    """
    max_value = max(parsed_tab)

    # Création de l'histogramme vide.
    histogram = [0 for _ in range(max_value + 1)]

    for char in parsed_tab:
        histogram[char] = histogram[char] + 1

    # Renvoie de l'histogramme complet.
    return histogram


def get_most_used_char(text_list: list, nb_char: int) -> dict:
    """
    :param text_list: Liste de caractère converti en ASCII.
    :param nb_char: Entier qui correspond au nombre de caractère notre fonction retournera.
           exemple : 5 renvera les 5 lettres les plus fréquente dans le fichier.
    :return: Renvoie un dictionnaire avec les 'nb_char' caractère les plus fréquent avec leur fréquence associée.
    """
    histogram = counting_sort(text_list)
    result = {}

    # Récupère les 'nb_char' caractères qui ont le plus grand nombre d'occurences et les ajoute à un dictionnaire.
    for _ in range(nb_char):
        max_value = max(histogram)
        max_index = histogram.index(max_value)

        result[chr(max_index)] = (max_value * 100) // len(text_list)
        histogram[max_index] = -999

    # Renvoie du dictionnaire contenant les plus grandes occurences du fichier mis en paramètre.
    return result


if __name__ == '__main__':
    print('Ce fichier doit être importé et non executé seul, '
          'essayez d\'executer le fichier \'main.py\' à la racine du projet.')
