# Copyright : romain_flcht

# Fichier contenant les chemins d'accèsw aux fichiers triés par langue.
#
# Si vous souhaitez ajouter une langue, placez les textes dans le dossier 'textes' et ajoutez votre langue dans
# 'LANGUAGE_TEXT_PATH' dans ce format :
# 'Langue': ('textes/nom_du_fichier.txt', ),

LANGUAGE_TEXT_PATH = {
    'Français': ('textes/fables_.txt', 'textes/lacomediehumaine_.txt'),
    'Anglais': ('textes/richardIII_.txt', 'textes/hamlet_.txt', 'textes/mobydick_.txt'),
    'Portugais': ('textes/osmaias_.txt', 'textes/lusiadas_.txt'),
    'Espagnol': ('textes/donquijote_.txt',),
    'Allemand': ('textes/faust_.txt',),
    'Italien': ('textes/ladivinecomedie_.txt',),
    'Néerlandais': ('textes/deondergangdereerstewareld_.txt',),
    # 'Langue': ('textes/nom_du_fichier1.txt', 'textes/nom_du_fichier2.txt'),
}

if __name__ == '__main__':
    print('Ce fichier doit être importé et non executé seul, '
          'essayez d\'executer le fichier \'main.py\' à la racine du projet.')
