
{% set num = 14 %}
{% set titre = "Fusion de tables"%}
{% set theme = "donneestable" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 


!!! note "Remarque"
    Les exemples des activités sont volontairement courts et simples pour introduire les concepts, des exemples plus conséquents seront traités en exercice.

{{ titre_activite("Opérateur de concaténation",[],0) }}


Pour un exposé, deux élèves de premières ont du faire des recherches sur la démographie de quelques pays européens, Antoine s'est chargé des trois pays suivants : France, Allemagne et Pologne, ses résultats sont dans le fichiers `csv` suivant :
{{telecharger("Démographie Fra-All-Pol","./files/C14/pays_antoine.csv")}}
Justine a réuni les *mêmes données* pour les pays suivants : Italie, Espagne et Grèce :
{{telecharger("Démographie Ita-Esp-Gre","./files/C14/pays_justine.csv")}}


1. Utiliser le module `csv` de Python pour lire les données de ces tables et les récupérer dans les listes de dictionnaires `pays_antoine` et `pays_justine`

    !!! aide
        On rappelle qu'on peut lire les données d'une table sous la forme d'une liste de dictionnaire à l'aide du module `csv` de Python :

        ```python
        import csv
        # Remplacer <nom du fichier> par le nom du fichier (avec éventuellement le chemin d'accès)
        fichier=open(<nom du fichier>,"r",encoding="utf-8")
        contenu = list(csv.DictReader(fichier,delimiter=','))
        fichier.close()
        ```
        En cas de difficultés, se référer au [chapitre sur la lecture et le traitement des données en table](https://fabricenativel.github.io/NSIPremiere/donneestable/#activite-2-lecture-et-traitement){target=_blank}

2. Recopier et compléter en utilisant le vocabulaire des données en table : *descripteur*, *enregistrement*, *tables*, *champ*
> "*Ces deux ..... partagent exactement les mêmes ....... mais contiennent des ......... différents. Chaque ...... est identifié de façon unique par le ...... `nom`. Les données sont exprimées dans la même unité : kilomètre carré pour la surface et nombre d'habitants pour la population.*"

3. Pour obtenir une table contenant les six pays, on peut simplement **concaténer** les deux listes grâce à l'opérateur `+` en python. Le programme s'écrit alors :
```python
import csv

# Données de la table d'Antoine
fichier=open("pays_antoine.csv","r",encoding="utf-8")
pays_antoine = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

# Données de la table de Justine
fichier=open("pays_justine.csv","r",encoding="utf-8")
pays_justine = list(csv.DictReader(fichier,delimiter=','))
fichier.close()

# Concaténation des deux tables
pays = pays_justine + pays_antoine
```

Recopier et executer ce programme, quelles conditions permettent cette concaténation ?


{{ titre_activite("Combiner les données de deux tables",[]) }}

Jessica et Albert ont  travaillé sur le même exposé, mais différemment. Jessica a crée un fichier `csv` contenant la population des 6 pays (Allemagne, France, Pologne, Italie, Espagne, Grèce) tandis qu'Albert a crée un fichier contant la surface de ces 6 mêmes pays.

{{telecharger("Surface","./files/C14/population_jessica.csv")}}

{{telecharger("Population","./files/C14/surface_albert.csv")}}
Ils souhaitent maintenant, fusionner leurs données de façon à créer une table contenant la population et la surface pour les six pays.

1. Ecrire un programme python permettant de lire ces deux tables et de les convertir en deux listes de dictionnaires `population` et `surface`.

    !!! aide
        Voir l'activité précédente pour la lecture d'un fichier `csv` sous forme de liste de dictionnaire. Après lecture, la liste de  dictionnaires  `population` devrait contenir :
        ```python
        [{'Nom': 'Allemagne', 'Population': '83129285'}, {'Nom': 'France', 'Population': '67422241'}, {'Nom': 'Pologne', 'Population': '38386158'}, {'Nom': 'Italie', 'Population': '60494785'}, {'Nom': 'Espagne', 'Population': '47329981'}, {'Nom': 'Grèce', 'Population': '10709606'}]
        ```
        Et la liste de dictionnaires `surface` devrait contenir :
        ```python
        [{'Nom': 'Allemagne', 'Surface (km²)': '357386'}, {'Nom': 'France', 'Surface (km²)': '551695'}, {'Nom': 'Pologne', 'Surface (km²)': '312679'}, {'Nom': 'Italie', 'Surface (km²)': '302072'}, {'Nom': 'Espagne', 'Surface (km²)': '505992'}, {'Nom': 'Grèce', 'Surface (km²)': '132049'}]
        ```

2. Obtient-on le résultat attendu en effectuant la concaténation des deux tables ? Pourquoi ?
3. Recopier et compléter avec les mots : *tables*, *descripteur*, *enregistrement*

    > Les deux ...... n'ont pas exactement la même structure, en effet elles partagent un ........ commun (`Nom`). Mais les autres descripteurs sont différents. Pour fusionner ces tables, on doit rapprocher les ........... des deux tables qui ont la même valeur sur le ............. commun. On dit qu'on fait une **jointure** des deux tables.

4. Compléter la fonction `get_surface` ci-dessous qui prend en argument un nom de pays et renvoie sa surface (la variable `surface` est la liste de dictionnaire de la question 1.)

    ```python
    def get_surface(nom_pays):
        for pays in surface:
            if pays[......]==.....:
                return ....['Surface (km²)']
    ```

5. Pour générer la jointure des deux tables sur le descripteur commun `Nom` on propose l'algorithme suivant :  
:one: Parcourir les pays du dictionnaire `population`  
:two: Récupérer la surface de chaque pays à partir du descripteur commun `Nom` (fonction `get_surface` ci-dessus)  
:three: Stocker les informations dans une nouvelle liste de dictionnaire   

Recopier, compléter et tester le programme correspondant :
```python
fusion = []
for pays in population:
    nom_pays = pays['Nom']
    population_pays = ......
    surface_pays = ........
    fusion.append({'Nom':nom_pays,'Population':population_pays,'Surface':surface_pays})
```
## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}
 

## Exercices

{{ exo("Concaténation de deux tables",[],0) }}



{{ exo("Jointure de deux tables",[],0) }}
