```
    ___               _   __      ___    __  ___  __     ( )       
  //   ) ) //   / / // ) )  ) ) //   ) )  / /   //  ) ) / / \\ / / 
 //___/ / ((___/ / // / /  / / //   / /  / /   //      / /   \/ /  
//            / / // / /  / / ((___( (  / /   //      / /    / /\
```

🔌 Le monde dans un ordinateur, représentation virtuelle de la réalité

![Demo](https://s8.gifyu.com/images/demo89ed580835b4b321.gif)

## Pourquoi
J'étudiais un texte de Bergson à propos de la conscience lors de mon cours de philosophie quand la personne en face de moi s'indigna après avoir entendu que le monde dans lequel nous vivons pouvait être une simulation informatique. C'était tellement inconcevable pour lui que même les arguments de la professeur qui était pourtant fondés ne l'eut pas convaincu. C'est pourquoi j'ai décidé de prouver que tout peut être une simulation. J'ai créé ce petit programme en quelques jours avec les règles basiques de notre monde afin de le "virtualiser". J'ai aussi décidé de le rendre Open-Source pour ce [mois de l'Hacktoberfest](https://hacktoberfest.digitalocean.com/) pour partager ô combien il est facile de créer une simulation basique de nos vies. Si un simple adolescent de 17 ans a réussi à programmer ceci en quelques jours, on peut se demander si il est probable qu'en 2000 ans, un groupe de personnes expérimentées ait réussi à faire de notre monde une simulation.

## Comment ça fonctionne
Au démarrage du programme, la taille du monde est définie. Cette taille définit à son tour la capacité maximum de personnes que peut acceuillir le monde. Si la limite de la capacité est atteinte, le programme crash. Le nombre des premiers humains est aussi défnit (ils vont apparaitre dans le monde avant que tout commence dans le programme). Comme dans le vrai monde, on attribue un numéro d'identifiant à chacun dès sa naissance, cela nous permet de traquer ce que font les humains de la matrice.
Cette simulation a trois principaux concepts : **évènements**, **relations**, **cycle de la vie**

### Évènements
Ce monde a quatre évènements qui peuvent être déclenché sur n'importe lequel de ses habitants:

* Aller travailler (`W`)
* Aller faire ses courses (`S`)
* Rentrer chez soi (`H`)
* Donner naissance à quelqu'un (`B`)

Le programme décide aléatoirement sur qui doit être déclenché quel évènements et quand. Les humains n'ont seulement qu'une impression de choisir ce qu'ils font alors que ce choix leur est insufflé par le programme.

### Relations
À chaque fois que quelqu'un se situe au même endroit qu'une autre personne, ils créent un lien entre eux: une relation. Il y a trois types de relations dans le programme:
* Connaissance
* Ami
* Partenaire

Ce qu'il y a à savoir à propos du type "Partenaire":
* On ne peut avoir qu'un partenaire
* Dès lors que vous avez un partenaire vous pouvez donner naissance à quelqu'un

### Cycle de la vie
Le cycle de la vie commence dès lors que quelqu'un naît. À partir de cet instant cette personne vieillit de 1 an toutes les 0.1 secondes (Je sais c'est rapide mais ça aurait été ennuyant si l'on devait attendre 60 ans avant de voir quelqu'un mourrir dans le programme, je serai probablement mort avant... Donc je préfère que ça aille vite). Dès que quelqu'un a 60 ans, ils ont une probabilité de mourrir de 60% (on ne peut pas mourir avant 60 ans). Cette probabilité augmente alors de 1% à chaque année prise par la personne.

## Lire la matrice
J'en conviens, à première vu, ce que l'on peut voir de la matrice est vraiment étrange. Laissez moi vous expliquer.
Chaque ligne de la matrice est composée de:
```
Coordonnées.X:Coordonnées.Y:Identifiant:Évènement
```

De cette manière on peut voir qui fais quoi, où et quand.

Par exemple :
```
10:20:1:W
  |   | |
  |   | |_______________________________________________ Va au travail
  |   |___________________ La personne qui a pour Identifiant: 1
  |
L'endroit où il est
```

Vous pouvez alors vous demander, pourquoi faire ça ? C'est stupide il serait mieux d'afficher ceci :
```
La personne qui a pour identifiant: 1 va au travail aux coordonnées X:10; Y:20
```

C'est pas faux, mais à la vitesse de la matrice je vous mets au défi de réussir à lire ne serait-ce qu'un seul mot. C'est impossible. C'est pourquoi j'ai décidé de ne mettre que des lettres et des chiffres bien plus lisibles à haute vitesse.