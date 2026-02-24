<!-- Slide number: 1 -->

![](GoogleShape237p22.jpg)
INTRODUCTION AU
NETTOYAGE DE DONNÉES

### Notes:

<!-- Slide number: 2 -->
Avant de commencer…
Téléchargez le logiciel Tabula https://tabula.technology/

On l’utilisera cet après-midi

### Notes:

<!-- Slide number: 3 -->
I.     RAPPEL : LA DATA PIPELINE
II.    QU’EST-CE QU’UNE DONNEE
III.   LA VERIFICATION
IV.   LE NETTOYAGE
V.   LES OUTILS

SOMMAIRE

### Notes:

<!-- Slide number: 4 -->

![](GoogleShape255p25.jpg)
LA DATA PIPELINE
QUELQUES RAPPELS

### Notes:

<!-- Slide number: 5 -->

![](GoogleShape262p26.jpg)
7 GRANDES ETAPES
valable pour tout type de projet, de la brève sur le vote du budget municipal à l’enquête internationale sur l’évasion fiscale

TRAVAIL SOUVENT NON LINEAIRE
aller-retour entre étapes, répétition des étapes pour plusieurs jeux de données…)

RAPPELS

### Notes:

<!-- Slide number: 6 -->
CE QUE VOUS AVEZ DÉJÀ VU

Qu’est-ce que l’open data ?
Définir son projet d’enquête
Trouver les sources de données
Récupérer les données

![](GoogleShape269p27.jpg)
RAPPELS

### Notes:
open data →

<!-- Slide number: 7 -->
EXEMPLE: DOSSIER MATERNITÉS DU MONDE

Problématique: Sur quel critère choisir une maternité lorsque l’on est enceinte ? Y a-t-il des profils type d’établissements ?

Hypothèse supposée : certains établissements se distinguent par un taux de médicalisation de l’acte plus fort (césarienne…)

Recherche de données : enquête nationale périnatale, base statistique annuelle des établissements de santé (SAE), l’Agence technique de l’information hospitalière (ATIH) et la Fédération française de recherche en santé périnatale (FFRSP)

Problèmes avec les données : fiabilité: données aberrantes, encodage non standardisé
exhaustivité: actes non encodés

![](GoogleShape276p28.jpg)
RAPPELS

### Notes:

<!-- Slide number: 8 -->

![](GoogleShape284p29.jpg)
CE QUE L’ON VA VOIR AUJOURD’HUI

Méthodes de vérification
Nettoyage de données tabulaires

![](GoogleShape285p29.jpg)
CE QUE L’ON VA VOIR

### Notes:

<!-- Slide number: 9 -->

![](GoogleShape291p30.jpg)
MAIS AU FAIT
QU’EST-CE QU’UNE DONNÉE ?

### Notes:

<!-- Slide number: 10 -->
Qu’est-ce qu’une donnée ?
Qu’est-ce qu’une donnée ?
Qu’est-ce qu’une donnée ?
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 11 -->
Une représentation structurée du monde
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 12 -->
Une représentation structurée du monde
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 13 -->
Une représentation structurée du monde
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 14 -->
structuration
représentativité
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 15 -->
représentativité
données mal encodées
(qualité)
bonnes données
structuration
hallucinations
données falsifiées ou erronées
(fiabilité / exhaustivité)
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 16 -->
| Tableau 1 : Importations de véhicules en Côte d'Ivoire sur la période 2017-2018 |  |  |  |
| --- | --- | --- | --- |
| Mois | Type | Nombre |  |
|  |  | 2017 | 2018 |
| Juillet | Neufs | 793 | 993 |
|  | Usagés | 4482 | 4682 |
| Août | Neufs | 609 | 809 |
|  | Usagés | 1477 | 1677 |
| Septembre | Neufs | 583 | 783 |
|  | Usagés | 738 | 938 |
| Octobre | Neufs | 739 | 939 |
|  | Usagés | 515 | 715 |
| Novembre | Neufs | 664 | 864 |
|  | Usagés | 539 | 739 |
| Source : Rapport 2018 |  |  |  |
données mal encodées
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 17 -->
| Mois | Type | Nombre | Année |
| --- | --- | --- | --- |
| Juillet | Neufs | 793 | 2017 |
| Juillet | Neufs | 993 | 2018 |
| Juillet | Usagés | 4482 | 2018 |
| Juillet | Usagés | 4682 | 2018 |
| Août | Neufs | 609 | 2017 |
| Août | Neufs | 809 | 2018 |
| Août | Usagés | 1477 | 2017 |
| Août | Usagés | 1677 | 2018 |
| Septembre | Neufs | 583 | 2017 |
| Septembre | Neufs | 783 | 2018 |
| Septembre | Usagés | 738 | 2017 |
| Septembre | Usagés | 938 | 2018 |
| Octobre | Neufs | 739 | 2017 |
| Octobre | Neufs | 939 | 2018 |
| Octobre | Usagés | 515 | 2017 |
| Octobre | Usagés | 715 | 2018 |
bonnes données
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 18 -->
| Mois | Type | Nombre | Année |
| --- | --- | --- | --- |
| Juillet | Neufs | 793 | 2017 |
| Juillet | Neufs | 993 | 2018 |
| Juillet | Usagés | 4482 | 2018 |
| Juillet | Usagés | 4682 | 2018 |
| Août | Neufs | 609 | 2017 |
| Août | Neufs | 809 | 2018 |
| Août | Usagés | 1477 | 2017 |
| Août | Usagés | 1677 | 2018 |
| Septembre | Neufs | 583 | 2017 |
| Septembre | Neufs | 783 | 2018 |
| Septembre | Usagés | 738 | 2017 |
| Septembre | Usagés | 938 | 2018 |
| Octobre | Neufs | 739 | 2017 |
| Octobre | Neufs | 939 | 2018 |
| Octobre | Usagés | 515 | 2017 |
| Octobre | Usagés | 715 | 2018 |
données falsifiées ou erronées

Que signifie “Neufs” ?
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 19 -->
| Tableau 1 : Importations de véhicules en Côte d'Ivoire sur la période 2017-2018 |  |  |  |
| --- | --- | --- | --- |
| Mois | Type | Nombre |  |
|  |  | 2017 | 2018 |
| Juillet | Neufs | 0 | 110,5 |
|  | Usagés | 1 | 2 |
| Août | Neufs | -5 | 4 |
|  | Usagés | 2 | 7 |
| Septembre | Neufs | 0 | 9 |
|  | Usagés | 1 | 6 |
| Octobre | Neufs | -5 | 2 |
|  | Usagés | 2 | 2 |
| Novembre | Neufs | 5 | 210,7 |
|  | Usagés | 4 | -20 |
| Source : Rapport 2018 |  |  |  |
hallucinations
Cédric Lombion - 2018

### Notes:

<!-- Slide number: 20 -->

![](GoogleShape373p41.jpg)
ET MAINTENANT
UN EXERCICE PRATIQUE

### Notes:

<!-- Slide number: 21 -->
UN LIEN UNIQUE
POUR ACCÉDER AUX DOCUMENTS DE TRAVAIL

https://bit.ly/IJBA2024ressources
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 22 -->
ETAPES DEFINIR, TROUVER

Compléter ces étapes sur le thème: lutte contre la fracture numérique dans la métropole bordelaise

Pour trouver le tableau collaboratif:
https://bit.ly/IJBA2024ressources
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 23 -->

![](GoogleShape391p44.jpg)
ON REVIENT DONC VERS
LA VERIFICATION

### Notes:

<!-- Slide number: 24 -->
VERIFICATION: 3 ENJEUX
Fiabilité
Exhaustivité
Qualité
LA VERIFICATION

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 25 -->
Vérification: 3 enjeux
FIABILITE: les données représentent-elles la réalité ?
Exhaustivité
Qualité
«
«
par exemple, un taux d’épisiotomie plus élevé chez les multipares que chez les primipares, des taux d’épisiotomie à moins de 1 % ou à plus de 60 % (source: Le Monde)
LA VERIFICATION

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 26 -->
Vérification: 3 enjeux
Fiabilité
EXHAUSTIVITE: les données sont-elles complètes ?
Qualité
«
«
 tous les actes ne disposent pas d’un code spécifique, et même parmi ceux qui en ont, certains, non « tarifés », ne sont pas systématiquement saisis par les soignants, à l’image de l’épisiotomie. (source: Le Monde)
LA VERIFICATION

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 27 -->
Vérification: 3 enjeux
Fiabilité
Exhaustivité
QUALITE: Les données sont-elles structurées et documentées correctement ?

![](GoogleShape424p48.jpg)

![](GoogleShape425p48.jpg)
LA VERIFICATION

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 28 -->
VERIFICATION: 4 méthodes
Demander à la source: ce sont les meilleurs experts sur les données qu’ils produisent
Demander aux experts: de bons interlocuteurs quand la source ne coopère pas où quand il faut choisir entre plusieurs sources
Vérifications statistiques: moyenne, médiane, maximum, minimum, écart-type
Bon sens: est-ce que les hypothèses de bases sont vraies?
LA VERIFICATION

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 29 -->

![](GoogleShape437p50.jpg)
ON RETOURNE A NOTRE
TABLEAU COLLABORATIF

### Notes:

<!-- Slide number: 30 -->
1. Retrouver le jeu de données «Lieux d'inclusion numérique» sur le portail open data de Bordeaux métropole

2. Quelles questions de vérification poser à ce jeu de données ?
Ecrire les questions sur le jamboard
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 31 -->
Problèmes courants rencontrés lors de la vérification

Valeurs manquantes
Valeurs manquantes remplacées par des valeurs ambigues comme  0 ou des dates par défaut (1900,1904, 1969, 1970 sont des défauts courant)
Lignes ou valeurs en double
Formats de dates qui varient au sein du même jeu de données
Unités de mesure non spécifiées
Noms de colonnes ambigus
Pas de documentation de la provenance ou méthodologie du jeu de donnée
Des valeurs suspectes sont présentes
Les données ne sont pas assez fines
Les totaux diffèrent des agrégats inclus
La feuille de calcul a exactement  65536 lignes (valeur max dans les anciennes versions d’Excel) ou 255 colonnes (valeur max  dans les anciennes versions de Numbers)
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 32 -->

![](GoogleShape457p53.jpg)
NOUS VOILA ENFIN AU
NETTOYAGE

### Notes:

<!-- Slide number: 33 -->
3 TYPES DE NETTOYAGE
Toilettage
Edition
Rapprochement
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 34 -->
3 types de nettoyage
TOILETTAGE
Edition
Rapprochement
Préparer les données à la vérification ou l’analyse, sans toucher au contenu : nettoyage de la structure des données.
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 35 -->
3 types de nettoyage
Toilettage
EDITION
Rapprochement
Préparer les données à l’analyse, en corrigeant les problèmes et/ou en enlevant le superflu: nettoyage du contenu des données
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 36 -->
3 types de nettoyage
Toilettage
Edition
RAPPROCHEMENT
Préparer les données à l’analyse, en les fusionnant avec des données additionnelles qui rajoutent du contexte ou de la précision
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 37 -->

![](GoogleShape490p58.jpg)
ALLEZ, UN PETIT
EXERCICE

### Notes:

<!-- Slide number: 38 -->
https://bit.ly/IJBA2024ressources

Ce que l’on va faire ensemble:

 Récupérer le fichier PDF marqué ‘EXO’
Télécharger le logiciel Tabula https://tabula.technology/
Extraire les données
Vérifier & Nettoyer les données

NETTOYER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 39 -->
Astuces à retenir pour l’étape de Nettoyage

Lors du toilettage vous serez souvent amené à:

Enlever les artefacts de mise en force (e.g. * NOM*)
en utilisant SUBSTITUTE()
Séparer les données en deux colonnes, par exemple pour séparer une valeur et son unité (e.g. 5 milliards)
en utilisant SPLIT()
Aligner les colonnes qui étaient décalées (par exemple après un export Tabula)
Scindre les donnée sur plusieurs lignes quand elles sont dans une seule cellule
par exemple avec SPLIT() et char(10)
Corriger les problèmes basiques d'orthographe qui affectent les filtres comme les formats de dates et les variations dans l’écriture des noms propres (New York, N.Y.)
en utilisant: IF() or IFS()
NETTOYER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 40 -->
Astuces à retenir pour l’étape de Nettoyage

Lors de l'Édition vous serez amené à faire:

Valeurs manquantes ou incorrectes: corriger ou supprimer ?
La seule solution peut être d’abandonner le jeu de donnée et aller en chercher un autre
Identifier et enlever les éléments en double
formule utile: UNIQUE()
fonctionnalité unique: Filters
Ajouter de colonnes de clarification (e.g. unités de valeur)
Ajouter des colonnes calculées (e.g. âge des individus quand vous n’avez que leurs date de naissance
formule utile: DATEDIF()
Ajouter des colonnes de catégorisation (e.g. tranches d’âges)
formules utiles: IF() or IFS()
Enlever des portions de données qui ne sont pas pertinentes pour votre analyse
NETTOYER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 41 -->
Astuces à retenir pour l’étape de Nettoyage

Lors de l'Édition vous serez amené à faire:

Valeurs manquantes ou incorrectes: corriger ou supprimer ?
La seule solution peut être d’abandonner le jeu de donnée et aller en chercher un autre
Identifier et enlever les éléments en double
formule utile: UNIQUE()
fonctionnalité unique: Filters
Ajouter de colonnes de clarification (e.g. unités de valeur)
Ajouter des colonnes calculées (e.g. âge des individus quand vous n’avez que leurs date de naissance
formule utile: DATEDIF()
Ajouter des colonnes de catégorisation (e.g. tranches d’âges)
formules utiles: IF() or IFS()
Enlever des portions de données qui ne sont pas pertinentes pour votre analyse
NETTOYER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 42 -->
Astuces à retenir pour l’étape de Nettoyage

Lors du Rapprochement vous serez amenés à faire:

Fusion de deux jeux de données (ou plus) en utilisant une colonne commune
formule utile: FILTER() et INDEX(MATCH())
NETTOYER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 43 -->
# A SUIVRE...

### Notes:
