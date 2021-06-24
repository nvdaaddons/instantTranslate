# instantTranslate #

* Auteurs : Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino et d'autres contributeurs de NVDA.
* Télécharger [version stable][1]
* Télécharger [[version de développement][2]

Cette extension permet de traduire le texte sélectionné et ou le texte copié
dans le presse-papiers d'une langue à une autre.  Il utilise un service
externe.

## Configurer les langues ##
Pour configurer la langue source, destination et dans le cas d'une permutation, allez à : Menu NVDA >> Préférences >> Paramètres d'Instant Translate.

Il y a deux listes déroulantes  appelées "Langue source" et "Langue cible"
et une case à cocher pour décider si la traduction doit être copiée dans le
presse-papiers.

En outre, si vous avez sélectionné l'option automatique (le premier choix)
dans la liste déroulante "Langue source", Il y a aussi une liste déroulante
appelée "Langue d'alternance" et une case à cocher sur alternance
automatique.

La signification des deux premières listes déroulantes et de la case à
cocher pour la copie est claire, mais quelques mots au sujet du reste sont
nécessaires. Rappelez-vous toujours que les explications ci-dessous
supposent la langue source, définie sur l'option automatique.

La liste déroulante "Langue d'alternance" est utile lorsque vous permutez
par script (voir ci-dessous) la langue source et la langue cible ; en effet,
une langue cible définie sur l'option automatique n'a aucun sens, donc
l'extension lui affecte la valeur de la liste déroulante ci-dessus.

Alors, Imaginez cette situation : vous traduisez généralement vers l'Anglais
(votre langue principale), mais parfois (par exemple, lorsque vous écrivez
un document), vous avez besoin de traduire vers l'Italien (votre seconde
langue, supposons); vous pouvez définir la zone de liste déroulante  "Langue
d'alternance" à l'Italien, donc vous ferez la traduction de l'Anglais vers
l'Italien sans accéder directement aux paramètres de
l'extension. Évidemment, cette fonction a une utilité majeure ou mineure
selon vos besoins plus fréquents.

Maintenant, la case à cocher alternance automatique : elle apparaît si et
seulement si vous définissez l'option automatique dans la liste déroulante
"Langue source", et est directement connectée avec la liste déroulante
"Langue d'alternance". Si vous l'activez, l'extension tente de permuter
automatiquement depuis la configuration de votre source et destination à une
configuration où la destination devient la langue source, et la langue
sélectionnée dans la liste déroulante "Langue d'alternance" est la nouvelle
langue destination ; très utile si la langue source du texte que vous voulez
traduire est la langue destination.

Un exemple simple : reprenons à l'esprit la situation imaginée précédemment
; Si vous traduisez un texte dans une langue différente de l'Anglais, il n'y
a pas de problème, vous obtenez la traduction correcte en Anglais. Mais si
vous avez besoin de traduire un texte de l'Anglais, normalement vous obtenez
une traduction en Anglais  identique au texte original, et c'est un peu
inutile. Grâce à la fonction alternance automatique, cependant, en supposant
que vous voulez savoir comment votre texte sonne en Italien, l'extension
commute automatiquement la langue cible à l'Italien, donc elle retourne une
traduction valide.

En tout cas, il s'agit d'une configuration temporaire ; si cette option n'a
aucun effet (c'est expérimental), essayez de permuter manuellement à une
configuration stable, en utilisant le geste d'alternance décrites
ci-dessous. C'est expérimental car dans certaines situations (avec des
textes courts, typiquement), Google ne reconnaît pas la véritable langue
source correctement, et vous devrez permuter manuellement  les langues par
script, afin de forcer la langue source à la langue cible précédente
(Anglais dans notre exemple).

## Utilisation ##
Vous pouvez utiliser cette extension de deux façons :

1. Sélectionnez du texte en utilisant les commandes de sélection (maj avec
   les touches fléchées, par exemple) et appuyez sur la touche associée pour
   traduire. Le résultat de la traduction sera lu avec le synthétiseur que
   vous utilisez.
2. Vous pouvez également traduire le texte depuis le presse-papiers.

## Raccourcis clavier ##
Toutes les commandes suivantes doivent être frappées après la touche
modificatrice "NVDA+Maj+t":

* T: Traduit le texte sélectionné,
* Maj+t: Traduit le texte depuis le  presse-papiers,
* S: Permute les langues source et cible,
* A: Annonce la configuration courante,
* C: Copie le dernier résultat dans le presse-papiers,
* I: Identifie la langue du texte sélectionné,
* H: Annonce toutes les commandes disponibles pour l'utilisateur.

## Changements pour la version 4.1 ##
* InstantTranslate fonctionne à nouveau, maintenant avec le Service de
  Traduction Yandex au lieu de Google.

## Changements pour la version 4.0 ##
* La traduction est effectuée automatiquement après alternance.
* Corrigé un bug dans la mémoire cache.).

## Changements pour la version 3.0 ##
* La façon dont les Raccourcis sont utilisés a changé, maintenant vous
  pouvez appuyer sur  la touche modificatrice instantTranslate "NVDA+Maj+t",
  puis une touche avec une seule lettre pour effectuer une action (voir
  toutes les commandes dans la section "Raccourcis clavier").
* Mise en place des langues d'alternance.
* Le Format de configuration a été modifiée, maintenant nous pouvons changer
  les paramètres d'instant translate si nous sommes dans la sous-fenêtre
  uniquement en lecture, mais n'oubliez pas que cela va fonctionner avant le
  premier redémarrage de NVDA.
* La limite sur la quantité de texte qui peut être traduite a été supprimée.
* Ajout du raccourci t à l'élément de menu paramètres de Instant Translate
* L'option automatique est maintenant en première position dans la liste
  déroulante  source et absente dans la liste déroulante destination.
* Ajout d'une case à cocher pour configurer la copie du résultat de la
  traduction.
* Sauvegarde du fichier de configuration à la racine du dossier paramètres.
* Langues source et destination synchronisées avec ce que Google Translate
  expose actuellement (22 avril 2015).


## Changements pour la version 2.1 ##
* Maintenant le module peut traduire du texte depuis le presse-papier en
  pressant NVDA+maj+y.

## Changements pour la version 2.0 ##
* Ajout d'un dialogue de configuration permettant de choisir la langue
  source et la langue destination.
* Ajout d'un élément de menu pour ce module dans le menu préférences.
* Les paramètres sont maintenant stockés dans un fichier de configuration
  séparé.
* Les résultats de traduction sont maintenant automatiquement copiés dans le
  presse-papier pour des manipulations ultérieures.

## Changements pour la version 1.0 ##
* Version initiale.


[[!tag dev stable]]


[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
