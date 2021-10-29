
{% set num = 8 %}
{% set titre = "Le web"%}
{% set theme = "web" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 
 
{{ titre_activite("Modèle client serveur",["video"],0) }}
<div class="centre"><iframe src="https://player.vimeo.com/video/138623558?color=b50067&title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

En faisant vos propres recherches et en vous aidant de la vidéo ci-dessus, répondre aux questions suivantes :

1. Quand et par qui a été inventé *le Web* ?
2. Peut-on dire *Internet* à la place du *Web* ?
3. Sur quel principe de fonctionnement repose *le Web* ?


{{ titre_activite("Les éléments d'une page Web",[]) }}

1. Squelette d'une page *Web*<br>
L'éditeur VS Code, permet d'insérer rapidement la structure de base d'une page web :

    * créer un fichier vide appelé `structure.html`,
    * ouvrir ce fichier dans VS Code,
    * taper simplement `!` et entrée (ou alors taper `html` et dans le menu d'abbreviation sélectioner `html:5`)

    Vous devriez obtenir le résultat suivant :
    ```html linenums="1"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    ```

    1. Un document {{sc("html")}} est constitué d'un *en-tête*, suivi d'un *corps*. Repéré les balises permettant de délimiter :
        1. Le document {{sc("html")}}
        2. L'en-tête
        3. Le corps
    2. L'entête contient une balise `<title>`, quel est son rôle ?

2. Ajout de contenu<br>
Dans le corps du document, c'est à dire entre les balises `<body>` et `<body>`, insérer le contenu suivant :

```html linenums="1"
<h1> La recette du carry de poulet

    <h2> Les ingrédients
        <ul>
            <li> un poulet découpé en morceaux
            <li> 3 oignons
            <li> 1 tomate
            <li> 5 gousses d'ail
        </ul>
    
    <h2> La préparation
        <p>Dans de l'huile chaude, faire revenir le poulet</p>
```

3. Créer un lien

4. Insérer une image

{{ titre_activite("L'apparence d'une page Web",[]) }}

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Corrections",[],0)}}

Corriger les erreurs dans les fragments de code HTML suivant :

1. `<h> Mon titre principal </h>`
2. `<href="http://www.wikipedia.fr">un lien vers Wikipedia</href>`
3. `<p> Ce paragraphe contient un <a href="autre_page.html">lien vers une autre page</p></a>`


{{ exo("Structurer une page Web",[]) }}





{{ exo("Modifier l'apparence d'une page web",[]) }}



{{ exo("Créer un mini-site",[]) }}

Réaliser  un mini site *Web*, en utilisant le html et les feuilles de style. Le sujet du site est au choix, par exemple : votre CV, vos films préférés, un site de recette de cuisines, un site sur un sport ou une de vos passions, ou sur une célébrité (sportif, acteur, chanteur ...) . Respecter le cahier des charges suivant :

* au moins 5 pages reliées entre elles par des liens internes et des liens vers des sites extérieurs
* au moins 5 images, attention à utiliser des images *libres de droits* ou à créer vos propres illustrations pour votre site
* au moins une page de votre site devra contenir des informations organisées sous la forme d'un tableau et donc utiliser les balises `<table>` et `<table>`.
* L'apparence du site sera uniformisé (c'est à dire que d'une page à l'autre on retrouvera les mêmes couleurs et la même présentation). Vous devrez pour cela utiliser une feuille de style dans un fichier séparé.
