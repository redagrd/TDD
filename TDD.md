# Test Driven Development (TDD)

## Test à retenir

1. Test unitaire = test d'une fonction
2. Test d'intégration = test d'une fonction qui utilise une autre fonction
3. Test fonctionnel = test d'une fonctionnalité qui regroupe plusieurs fonctions (ex: test d'un site web ou d'une application)

Coverage = pourcentage de code testé, on veut un coverage de 100% mais on visera 80% pour le projet

## Bonne pratique

FIRST = Fast, Isolated, Repeatable, Self-validating, Timely  
Fast = les tests doivent être rapides  
Isolated = les tests doivent être indépendants les uns des autres, ils ne doivent pas dépendre d'autres tests  
Repeatable = les tests doivent être répétables, ils doivent donner le même résultat à chaque fois  
Self-validating = les tests doivent être automatiques et ne doivent pas nécessiter d'intervention humaine  
Timely = les tests doivent être écrits en même temps que le code voire avant

Red-Green-Refactor  
Red = on écrit un test qui échoue  
Green = on écrit le code qui fait passer le test(minimum pour qu'il passe)  
Refactor = on améliore le code  

Un fichier de test doit être nommé `test_<nom_du_fichier_a_tester>.py` et le nom de la classe ou de la fonction de test doit être `Test<nom_du_fichier_a_tester>` ou `test_<nom_de_la_fonction_a_tester>`  

## Pytest

Pytest est une librairie de test unitaire pour Python.  
Pour executer les tests, il suffit de taper `pytest` dans le terminal à la racine du projet, suivi du nom du fichier de test à executer.  

## Unittest

Unittest est une librairie de test unitaire pour Python.  
Comparé à Pytest, Unittest permet de créer des rapports de test plus détaillés.  
Pour executer les tests, il suffit de taper `python -m unittest` dans le terminal à la racine du projet, suivi du nom du fichier de test à executer.  

## Mock

Mock est une librairie de test unitaire pour Python. Elle fonctionne avec Pytest et Unittest.  
Mock permet de mocker (simuler) des objets, des fonctions, des classes, des modules, etc.  
Pour utiliser Mock, il faut l'importer dans le fichier de test avec `from unittest.mock import Mock` et créer un objet Mock avec `mock = Mock()`.  
Pour mocker une fonction, il faut utiliser `mock = Mock(return_value=<valeur_de_retour>)`.  
Pour mocker une classe, il faut utiliser `mock = Mock(spec=<nom_de_la_classe>)`.  
l'intérêt de mocker est de pouvoir tester une fonction qui utilise une autre fonction sans avoir à tester la fonction utilisée.  

