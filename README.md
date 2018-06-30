# Typologie des amendements

Ce dépôt contient des données et des scripts visant à construire une typlogie des amendements du parlement français. Ce travail s'appuie sur les données poduites par Regards Citoyens.

## données et périmètres

Pour le moment, seuls les amendements de l'Assemblée Nationale de la quinzième législature ont été analysées.

## variable par amendement

La typologie des amendements sera contruite sur la base de profils d'amendements contenant ces variables : 
x statut 
x nb auteur
x doublon
x concurrence 
x majorité
x type de premier auteur
	x gouvernement ddans signataire
	x président ou présidente de groupe : parlementaire_organismes dont organisme est de type groupe
x analyses bigrames des exposés des motifs
    x tf/idf par groupe
    x catégorisation à la main des 1000 bigrammes les plus fréquents

Variables qu'on pourrait/devrait rajouter
- Doublons flous : On calcule une mesure de similarité entre les textes et les exposés entre chaque paire d'amendements par sujet et par lecture. On construit un réseau en filtrant les liens peu similaire. on ajoute au vecteur d'amendement le nombre de doublons flous comme le degré des noeuds dans le réseau
- Raporteur
- type de texte dans dépôt metric csv
- procédure 
- séance/commission prépare_amendement dans tools dans factoryparser
- référence metlesliens sur les amendements

## Hypothèses de profils d'amendement

Voici les types d'amendemnt que nous cherchons à détecter.
Les critères de sélection propose un jeux de filtre isolant les amendements, les profils quantitatifs liste les tendances quantitatives des caractéristiques que ce type d'amendements devraient respecter. 

### technique
Amendements proposant des petites modifications techniques n'impactant pas l'esprit de la loi mais améliorant le texte d'une point de vu technique (juridique).

- critères de sélection  
    * motif court : ~<= 135 caractères
    * type du motif par TAL: cohérence, rédactionnel, précision, coordination, précision rédactionnel

- profil quantitatif attendu
    - peu de signataire
    - plutôt adopté
    - rapporteur

### guerilla parlementaire 
Amendements visant à faire entendre une très forte opposition sur un texte et à faire durer le débat afin de mobiliser l'opinion.

- critères de sélection
    + grand nombre de doublons floux
    + opposition 
    + beaucoup de concurrence

- profil quantitatif attendu
    - systématiquement rejeté
    - le texte d'une grande part de ces amendements commencent par "supprimer" 

### lobbying
Amendements rédigés par un lobby et repris par un.des parlementaire.s.

- critères de sélection
    + petit nombre de texte doublons floux
    + motif différent

- profil quantitatif attendu
    - ??

### amendement d'appel / idéologique

Amendement d'appel et amendement non appelé "d'appel" mais ressemblant. On cherche les amendements qui consiste à utiliser un amendement pour exposer une vision politique et non proposer une modification précise sur un texte de loi.

- critères de sélection
    - contient des bigrames 'intention' qui contient le gramme "rapport"
    - bi-gramme thématiques spécifiques et non technique

- profil quantitatif 
    - ratio d'amendement porté par le président de groupe
    - long motif

### amendements de consensus
- critères de sélection
    + nombre de doublons floux sur le texte
    + exposé des motifs différents
- profile
    + beaucoup de groupes
    + attention risque de recouvrement avec le lobbying

### travail juridique du parlement

- critères de sélection
Tous les autres amendements

- profile
    - plutôt adopté
    - majoritaire
    - pas de doublon

# structure du dépôt

## création des vecteurs

Il faut disposer d'une base de données contenant le dump de nosdéputés.fr
Il faut installer pymysql
Il faut utiliser python3

```bash
pip install pymysql
python3 amds_vectors.py
```

On obtient le fichier amds_vectors.csv qui contient une ligne par amendements et une colonne par variable.

## analyse des contenus des amendements

Dans le dossier motifs se trouvent des notebooks jupyter et scripts python qui traitent les contenus des amandements :
- extraction des bigrammes (sans stopwords) par fréquence
- catégorisation à la main des bigrammes dont la fréquence > 25 
- calcul du tf/idf par groupe parlementaire
- calcul des similarité entre texte et entre exposé par sujet et lecture


