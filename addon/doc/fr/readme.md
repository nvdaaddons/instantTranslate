# instantTranslate #

* Auteurs : Alexy Sadovoy, ruslan, Beqa Gozalishvili et d'autres
  contributeurs de NVDA.
* Télécharger [version 2.2beta2][1]

Ce module complémentaire permet de traduire le texte sélectionné et ou le
texte copié dans le presse-papiers d'une langue à une autre.  Il utilise le
service Google Traduction.

## Configurer les langues ##

Pour configurer les langues source et destination, depuis le menu NVDA,
allez à Préférences, puis allez dans Paramètres de Instant Translate.  Il y
a deux zones de listes déroulentes appelées "traduire vers" et "traduire
vers".  Faites vos sélection et appuyez sur entrer sur le bouton Accepter.

## Comment utiliser ce module complémentaire ##

Il y a deux façons d'utiliser ce module complémentaire :

1. Sélectionnez du texte en utilisant les commandes de sélection (maj avec
   les flèches, par exemple). Appuyez en suite sur Maj+NVDA+T pour traduire
   le texte sélectionné. puis le texte traduit sera annoncé, en suposant que
   votre synthèse vocale supporte la langue.
2. Copiez du texte dans le presse-papiers. Appuyez en suite sur Maj+NVDA+Y
   pour traduire le texte du presse-papiers vers la langue sélectionnée.

## Changements pour la version 2.2 ##
* Nombre de caractères étendu à 1500.
* Ajout du raccourci t à l'élément de menu paramètres de Instant Translate
* Ajout d'une case à cocher pour configurer la copie du résultat de la
  traduction.
* Sauvegarde du fichier de configuration à la racine du dossier paramètres.
* Nouvelles langues : Aragonais, Arab, Portugais Brésilien, Croate,
  Néherlandais, Finnois, Français, Galicien, Allemand, Hongrois, Italien,
  Japonais, Coréen, Népalais, Polonais, Slovaque, Slovénien, Espagnol,
  Tamoul, Turque.

## Changements pour la version 2.1 ##
* Maintenant le module peut traduire du texte depuis le presse-papier en
  pressant NVDA+maj+y.

## Changements pour la version 2.0 ##
* Ajout d'un dialogue de configuration permettant de choisir la langue
  source et la langue cible.
* Ajout d'un élément de menu pour ce module dans le menu préférences.
* Les paramètres sont maintenant stockés dans un fichier de configuration
  séparé.
* Les résultats de traduction sont maintenant automatiquement copiés dans le
  presse-papier pour des manipulations ultérieures.

## Changements pour la version 1.0 ##
* Version initiale.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it
