<!-- Slide number: 1 -->

![](GoogleShape237p22.jpg)
INTRODUCTION A
LA RECUPERATION DE DONNEES

### Notes:

<!-- Slide number: 2 -->
I.     LE TRAVAIL AVEC LES DONNÉES
II.    EXERCICE SUPER DIFFICILE
III.   RECUPERER LES DONNEES
IV.   ZOOM SUR LE SCRAPING ET LES API
V.    L’EXTRACTION DE PDF
VI.   LA COLLECTE MANUELLE
VII. CHATGPT?

SOMMAIRE

### Notes:

<!-- Slide number: 3 -->
Pour accéder aux slides et aux ressource de cours, c’est par ici:
→https://bit.ly/IJBA2024ressources
RESSOURCES COURS

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 4 -->

![](GoogleShape256p25.jpg)
LA DATA PIPELINE
LE TRAVAIL AVEC LES DONNÉES

### Notes:

<!-- Slide number: 5 -->

![](GoogleShape263p26.jpg)
7 GRANDES ETAPES
valable pour tout type de projet, de la brève sur le vote du budget municipal à l’enquête internationale sur l’évasion fiscale

TRAVAIL SOUVENT NON LINEAIRE
aller-retour entre étapes, répétition des étapes pour plusieurs jeux de données…)

LE TRAVAIL AVEC LES DONNÉES

### Notes:

<!-- Slide number: 6 -->

![](GoogleShape270p27.jpg)
CE QUE VOUS CONNAISSEZ
Problématique & hypothèses, demande d’accès aux documents publics, portails open data, filetype:xls…

LE TRAVAIL AVEC LES DONNEES

### Notes:

<!-- Slide number: 7 -->

![](GoogleShape277p28.jpg)
CE QUE L’ON VA VOIR AUJOURD’HUI
scraping, collecte manuelle, extraction...

![](GoogleShape278p28.jpg)
LE TRAVAIL AVEC LES DONNEES

### Notes:

<!-- Slide number: 8 -->

![](GoogleShape284p29.jpg)
MAIS AVANT...
UN PETIT EXERCICE

### Notes:

<!-- Slide number: 9 -->
→https://bit.ly/ijbaJAM2024
UN PETIT JEU

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 10 -->

![](GoogleShape296p31.jpg)
TROISIEME ETAPE
RECUPERER LES DONNEES

### Notes:

<!-- Slide number: 11 -->
3 GRANDES QUESTIONS
Où sont mes données ?
Sous quel format sont-elles conservées ?
Dois-je les transformer ?
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 12 -->
3 grandes questions
OÙ SONT MES DONNÉES ?
Sous quel format sont-elles conservées ?
Dois-je les transformer ?
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats
travail de groupe:

<!-- Slide number: 13 -->
OÙ SONT MES DONNÉES ?

| LOCALISATION | RECUPERATION | FORMATS |
| --- | --- | --- |
| Portail open data | Téléchargement | xls, csv, shp, pdf, ods, json, xml, sqlite |
| Dans le système informatique d’une administration ou d’une entitée privée (non publiées en ligne) | Demande d’accès | xls, csv, shp, pdf, ods, json, xml, sqlite (et bien pire…) |
| Dans les archives physiques d’une administration ou d’une entitée privée | Demande d’accès | papier, photos (!), microfilm (!?!), |
| Derrière une interface de programmation applicative (API) | En bidouillant un peu de code informatique | csv, json, xml |
| En libre accès sur le web | en fonction du format | html, pdf (ou tout autre format en existence) |
| Nulle part | collecte de données | lié au mode de collecte |
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats. Parmi les formats, quel est celui qui est fondamentalement différent des autres ?

<!-- Slide number: 14 -->
SOUS QUEL FORMAT SONT-ELLES CONSERVÉES ?

| LOCALISATION | RECUPERATION | FORMATS |
| --- | --- | --- |
| Portail open data | Téléchargement | xls, csv, shp, pdf, ods, json, xml, sqlite |
| Dans le système informatique d’une administration ou d’une entitée privée (non publiées en ligne) | Demande d’accès | xls, csv, shp, pdf, ods, json, xml, sqlite (et bien pire…) |
| Dans les archives physiques d’une administration ou d’une entitée privée | Demande d’accès | papier, photos (!), microfilm (!?!), |
| Derrière une interface de programmation applicative (API) | En bidouillant un peu de code informatique | csv, json, xml |
| En libre accès sur le web | en fonction du format | html, pdf (ou tout autre format en existence) |
| Nulle part | collecte de données | lié au mode de collecte |
RECUPERER LES DONNEES

### Notes:
poser la question sur qui connaît les formats. Parmi les formats, quel est celui qui est fondamentalement différent des autres ?

<!-- Slide number: 15 -->
DOIS-JE LES TRANSFORMER ?

| FORMAT | RECUPERATION |
| --- | --- |
| XLS, CSV, SHP, ODS, JSON, XML, SQLITE | Pas d’étapes supplémentaires |
| PDF créé numériquement | Extraction des données via Tabula, ou manuellement |
| PDF scanné | Reconnaissance optique de caractère (OCR) ou manuellement |
| Papier, Photographie, Microfilm | Scanner + OCR ou manuellemenet |
| HTML | collecte automatisée (scraping) ou manuellement |
|  |  |
RECUPERER LES DONNEES

### Notes:
manuellement ne veut pas dire tout seul: le travail d’équipe peut être important ici, et le crowdsourcing peut jouer. Exemple des déclaration des députés à la Hautre Autorité pour la Transparence de la Vie Publique

<!-- Slide number: 16 -->

![](GoogleShape336p37.jpg)
ZOOM SUR
LE SCRAPING

### Notes:

<!-- Slide number: 17 -->

![](GoogleShape342p38.jpg)
MAIS AVANT...
UN PETIT EXERCICE

### Notes:

<!-- Slide number: 18 -->
Comment un site web est-il structuré ?
→ https://x-ray-goggles.mouse.org/
LE SCRAPING

### Notes:
expliquer la structure HTML du web. Une balise <p>, c’est un bloc de texte. Une balise <img /> c’est une image etc.

<!-- Slide number: 19 -->
RECUPERER DES DONNEES HTML SUR INTERNET = SCRAPER

C’est parce que c’est structuré qu’on peut facilement automatiser l’extraction.

Démonstration par la preuve: scrapons Wikipedia avec Google Sheets

→ https://bit.ly/IJBAscraping2024

Créer un onglet à son nom
Choisir un site web à scraper
Utiliser importHTML
LE SCRAPING

### Notes:
c’est parce que c’est structuré qu’on peut facilement automatiser l’extraction.

<!-- Slide number: 20 -->
RECUPERER DES DONNEES HTML SUR INTERNET = SCRAPER

On utilise la formule IMPORTHTML

![](GoogleShape363p41.jpg)
LE SCRAPING

### Notes:
Expliquer les bases d’utilisation d’un tableur

<!-- Slide number: 21 -->
RECUPERER DES DONNEES HTML SUR INTERNET = SCRAPER

Le niveau de difficulté est très variable, mais les outils sont nombreux

Démonstration par la przvueve:

![](GoogleShape370p42.jpg)

![](GoogleShape372p42.jpg)
Wikipedia? IMPORTHTML
IKEA? webscraper.io
Mais aussi avec des programmes payants, ou en codant soi-même etc.
LE SCRAPING

### Notes:
Démonstrer webscraper.io avec les délibérés municipaux.

<!-- Slide number: 22 -->
Un autre scraper: webscraper.io

Gratuit et puissant
un peu difficile à prendre en main au début
ne fonctionne que sur Chrome/Chromium
→ webscraper.io
LE SCRAPING

### Notes:
montrer l’extraction des délibérations

<!-- Slide number: 23 -->

![](GoogleShape387p44.jpg)
ZOOM SUR
LES API

### Notes:

<!-- Slide number: 24 -->
Récupérer des données via une API: genderize.io
→ genderize.io/
LE SCRAPING

### Notes:
montrer l’utilisation de l’API via le navigateur

<!-- Slide number: 25 -->

![](GoogleShape400p46.jpg)
ZOOM SUR
L’EXTRACTION DE PDF

### Notes:

<!-- Slide number: 26 -->
LES TABLEAUX DE DONNEES EN PDF
LE PDF EST NUMERIQUE? Tabula

![http://3.bp.blogspot.com/-rChwX8tcyys/UojmET24afI/AAAAAAAAAtk/M4CY4rp1o08/s1600/tabula1.png](GoogleShape408p47.jpg)
L’EXTRACTION DE PDF

### Notes:
poser la question sur qui connaît les formats

<!-- Slide number: 27 -->
LES TABLEAUX DE DONNEES EN PDF
SI LE PDF EST SCANNE? Amazon Textracthttps://aws.amazon.com/fr/textract/

![](GoogleShape416p48.jpg)
L’EXTRACTION DE PDF

### Notes:
poser la question sur qui connaît les formats

<!-- Slide number: 28 -->
RECHERCHER DES DONNÉES A TRAVERS PLUSIEURS PDF
GOOGLE PINPOINT https://journaliststudio.google.com/pinpoint

![](GoogleShape424p49.jpg)
L’EXTRACTION DE PDF

### Notes:
Expliquer que ça fonctionne avec pleins de formats

<!-- Slide number: 29 -->

![](GoogleShape430p50.jpg)
ZOOM SUR
LA COLLECTE MANUELLE

### Notes:

<!-- Slide number: 30 -->
ET SI...
LES DONNÉES N’EXISTENT PAS?

LA COLLECTE MANUELLE

### Notes:

<!-- Slide number: 31 -->
ALORS IL FAUT LES CREER!

![](GoogleShape443p52.jpg)
CROWDSOURCING

![http://wildotters.com/wp-content/uploads/2017/10/ODK-image-1.png](GoogleShape445p52.jpg)
COLLECTE DE DONNEES SUR LE TERRAIN
LA COLLECTE MANUELLE

### Notes:

<!-- Slide number: 32 -->
COLLECTER SES PROPRES DONNEES N’EST PAS SIMPLE

→ Quelle méthodologie ?
→ Quelle structuration de mes données (colonnes) ?
→ Quel degré de précision ?
→ Quel niveau d’exhaustivité ?

Il vaut mieux prendre contact avec des spécialistes qui pourront vous aider à penser votre collecte (spécialistes de la statistique, de l’urbanisme…)
LA COLLECTE MANUELLE

### Notes:

<!-- Slide number: 33 -->

![](GoogleShape458p54.jpg)
MAIS QU’EN EST-IL DE
CHATGPT (ET AUTRES)?

### Notes:

<!-- Slide number: 34 -->
UN ASSISTANT UTILE A LA COLLECTE DE DONNEES

Peut être utile pour:

se rappeler des formules
“rappelle moi la formule de Google Sheets qui permet d’extraire du contenu HTML”
trouver pourquoi la formule ne fonctionne pas
“voici ma formule, mais j’ai le mauvais tableau en retour.”
faciliter l’écriture de petits scripts, si on a appris les bases
“voici les urls des délibérés de Bordeaux Métropole, aide moi à écrire un script curl pour télécharger les PDFs»
“voici la documentation de l’API de météo France, aide moi a construire une requête pour récupérer la température”
CHATGPT

### Notes:
Expliquer ChatGPT et LLMs

<!-- Slide number: 35 -->
UN ASSISTANT UTILE A LA COLLECTE DE DONNEES

Mais attention:

ChatGPT se trompe souvent, donc il faut vérifier les résultats systématiquements
ne jamais compter sur Chatgpt pour extraire sans erreurs de données d’un PDF:
CHATGPT

### Notes:

<!-- Slide number: 36 -->
# A SUIVRE...
(N’hésitez pas à poser des questions!)

### Notes:
