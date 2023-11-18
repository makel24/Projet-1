"""Module de gestion des données historiques des symboles boursiers.

Ce module permet d'extraire et d'afficher des valeurs historiques 
pour un ou plusieurs symboles boursiers
à partir de la source de données Pax.

Auteur: Mandy Kelly
Date: 13 novembre 2023
"""


import argparse
import datetime
from datetime import date
import sys
import json
import requests





def analyser_commande():
    """
    Analyse les arguments de la ligne de commande pour l'extraction 
    de valeur historique ou plusieurs symboles boursiers
    Cette fonction va utiliser le module argparse pour analyser les valeurs des arguments suivant:
    
    Arguments optionnels:
    - 'd DATE', '--debut DATE': Date recherchée la plus ancienne (format: AAAA-MM-JJ)
    - 'f DATE', '--fin DATE': Date rechercée la plus récente (format: AAAA-MM-JJ)
    - 'v {fermeture,ouverture,min,max,volume}, --valeur {fermeture,ouverture,min,max,volume}
      La valeur désirée (par defaut: fermeture)
        
    Argument positionnel:
    - 'symbole' : Nom du symbole boursier
    Returns:
    Un objet Namespace tel que retourné par parser.parse_args(). 
    Cet objet aura l'attribut «symboles» représentant la liste des symboles à traiter, 
    et les attributs «début», «fin» et «valeur»
    associés aux arguments optionnels de la ligne de commande.
    """

    parser = argparse.ArgumentParser(
        description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers"
        )
    parser.add_argument(
        '-d', '--debut', metavar='DATE', dest= 'debut', type=datetime.date.fromisoformat, 
        help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)"
        )
    parser.add_argument(
        '-f', '--fin', metavar='DATE', dest='fin', default=datetime.date.today(), 
        type=date.fromisoformat, help="Date recherchée la plus récente (format: AAAA-MM-JJ)"
        )
    parser.add_argument(
        '-v', '--valeur', dest='valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], 
        default='fermeture', help="La valeur désirée (par défaut: fermeture)"
        )
    parser.add_argument(
        'symbole', nargs= '+', metavar='symbole', help="Nom d'un symbole boursier"
        )
    args = parser.parse_args()
    if args.debut is None:
        args.debut = args.fin

    return args

analyser_commande()

def produire_historique(titre, debut, fin, valeur):
    """
    Récupère l'historique des valeurs boursières pour les symboles choisis.
    Elle accepte les arguments suivants:
    
    -titre (str): Liste des symboles boursiers selon l'historique.
    -debut (datetime): Date de début de la période d'extraction.
    -fin (datetime): Date de fin de la période d'extraction.
    -valeur (str): La valeur boursière à extraire parmi 
    ['fermeture', 'ouverture', 'min', 'max', 'volume']
    
    Returns:
    Une liste de tuples (date, valeur) correspondant à l'historique demandé
    """
    liste_historique = []
    for symbole in titre:
        liste_date = []
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
        params = {'début': str(debut), 'fin': str(fin)}
        reponse = requests.get(url=url, params=params, timeout=5)
        reponse = json.loads(reponse.text)
        if "message d'erreur" not in reponse:
            date_actuelle = debut
            while date_actuelle <= fin:
                if date_actuelle.weekday() < 5:
                    date_str = date_actuelle.strftime('%Y-%m-%d')
                    if date_str in reponse['historique']:
                        valeur_date = reponse['historique'][date_str][valeur]
                        liste_date.append((date_actuelle, valeur_date))
                date_actuelle += datetime.timedelta(days=1)
            liste_historique.append(liste_date)
        else:
            print("Entrée non-valide ; Ce symbole est inexistant")
            sys.exit(1)
    return liste_historique
arguments = analyser_commande()
liste_symbole = arguments.symbole
date_debut = arguments.debut
date_fin = arguments.fin
liste_valeur = arguments.valeur

def afficher_historique(symbole_affiche, debut_affiche, fin_affiche, valeur_affiche):
    """
    Affiche les valeurs historiques des valeurs bourisères selon la période et le symbole.
    
    Les arguments sont:
    -symbole_affiche: Liste des symboles boursiers selon l'historique.
    -debut_affiche: Date de début de la période d'extraction.
    -fin_affiche: Date de fin de la période d'extraction.
    -valeur_affiche: La valeur boursière à extraire parmi 
    ['fermeture', 'ouverture', 'min', 'max', 'volume']
    
    Returns:
    None
    """
    liste_tuples = produire_historique(symbole_affiche, debut_affiche, fin_affiche, valeur_affiche)
    for i in enumerate(symbole_affiche):
        print(
        f'titre={symbole_affiche}: début={debut_affiche}:'
        f'fin={fin_affiche}: valeur={valeur_affiche}'
        )
        print(liste_tuples[i])
afficher_historique(liste_symbole, date_debut, date_fin, liste_valeur)
