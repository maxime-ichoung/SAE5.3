Mansour SY - Maxime ICHOUNG-THOE
# README pour le projet de reconnaissance faciale

## Description du Projet

Ce projet vise à développer un système de reconnaissance faciale en temps réel utilisant la caméra intégrée à un PC. Le système est capable de capturer des images de visages, de les associer à des noms pour construire un dataset, puis d'utiliser cet ensemble de données pour entraîner un modèle de classification. Ce modèle est ensuite utilisé pour prédire le nom de la personne devant la caméra en temps réel.

## Structure du Projet

Le projet est divisé en deux parties principales, implémentées dans deux notebooks Jupyter distincts :

1. **1_dataset.ipynb** : Ce notebook se concentre sur la création du dataset. Il implémente la capture d'images de visages à l'aide de la caméra du PC et les stocke dans un dossier local avec leurs noms associés.

2. **2_algo_XXXX.ipynb** : Ces notebooks mettent en œuvre différents algorithmes de classification et leur intégration dans le système de reconnaissance faciale en temps réel.

## Extensions et Adaptations

Nous avons réaliser différentes méthodes de classification en adaptant le 2ème notebook pour inclure :

- **La Régression Logistique**
- **L'Arbre de Décision**
- **Le SVC (Support Vector Classifier)**
- **Le MLP (Multi-Layer Perceptron)**


De plus, nous avons fait une adaptation spécifique pour la régression logistique permettant une reconnaissance binaire. En identifiant si le visage détecté est celui de l'utilisateur (admis) ou non (non admis), en utilisant un "seuil de confiance" dans les prédictions du modèle.

## Approfondissement

Nous avons également étudié et implémenté le fonctionnementet des réseaux de neurones convolutionnels (CNN) pour améliorer la précision de la classification.


## Comment Utiliser

Chaque notebook contient les instructions nécessaires sur son but, la mise en place de l'environnement nécessaire, et la manière d'exécuter le code.

## Configuration Requise

- Python 3.8 ou plus.
- Bibliothèques : OpenCV, scikit-learn, matplotlib, numpy, pickle, tensorflow.
- Caméra intégrée ou externe.

Chaque algorithme de classification utilisé dans le projet de reconnaissance faciale possède ses spécificités et répond à des défis particuliers liés à la reconnaissance faciale en temps réel. Voici une explication détaillée pour chacun, y compris la gestion des individus non reconnus à l'aide d'un seuil de confiance.

### Algorithme 1 : Régression Logistique

Notre **Régression Logistique** est utilisée comme un modèle de classification multiclasse. Elle prend les images de visages aplatis en entrée et apprend à associer ces images aux étiquettes (noms) correspondantes.

### Algorithme 2 : Arbre de Décision

Notre **Arbre de Décision** est un modèle de classification non linéaire qui prend des décisions basées sur des questions successives sur les données d'entrée. Dans le cas de la reconnaissance faciale, l'arbre de décision apprendra à poser une série de questions sur les caractéristiques des images de visage pour déterminer à quelle étiquette (nom) appartient chaque image.

### Algorithme 3 : Support Vector Classifier (SVC)

Notre **SVC** est un modèle puissant pour la classification multiclasse. Il fonctionne en trouvant l'hyperplan qui sépare au mieux les différentes classes dans l'espace des caractéristiques. Ici, il va chercher l'hyperplan qui sépare au mieux les visages des différentes personnes. Le kernel 'linear' est utilisé ici pour traiter le problème comme linéaire.

### Algorithme 4 : Régression Logistique avec Seuil de Confiance

Cet algorithme est une variante de la régression logistique qui ajoute un mécanisme de **seuil de confiance** pour gérer les cas où le visage détecté ne correspond à aucun des visages connus dans le dataset. Après avoir prédit la classe (le nom) d'un visage, l'algorithme évalue la probabilité (confiance) associée à cette prédiction. Si la confiance est inférieure à un seuil prédéfini (par exemple, 80%), l'algorithme classifie le visage comme "non admis" plutôt que de le rattacher à une personne connue. Nous avons utilisé cette technique pour ne pas identifier des visages inconnus comme étant ceux de personnes connues.

#### Fonctionnement du Seuil de Confiance

1. **Prédiction de la Classe et des Probabilités** : Pour chaque visage détecté, l'algorithme prédit non seulement la classe (nom) la plus probable mais aussi la distribution des probabilités pour toutes les classes possibles.

2. **Évaluation de la Confiance** : La confiance de la prédiction est évaluée en examinant la probabilité associée à la classe prédite. Si cette probabilité est inférieure au seuil défini, la prédiction est considérée comme incertaine.

3. **Décision Basée sur le Seuil** : Si la confiance est inférieure au seuil, l'algorithme attribue l'étiquette "non admis" au visage, indiquant qu'il ne reconnaît pas la personne avec une confiance suffisante.


## Conclusion

Ce projet nous offre une base pratique pour l'exploration de différentes techniques de classification d'images et pose les bases pour des projets plus complexes impliquant la reconnaissance d'images en temps réel.
