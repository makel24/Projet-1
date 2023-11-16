import argparse
import datetime
from datetime import date, timedelta
import requests
import json
import sys



def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers")
    parser.add_argument('-d', '--début', metavar= 'DATE', dest= 'début', type=datetime.date.fromisoformat, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument('-f', '--fin', metavar= 'DATE', dest= 'fin', default=datetime.date.today(), type=datetime.date.fromisoformat, help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument('-v', '--valeur', dest= 'valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default= 'fermeture', help="La valeur désirée (par défaut: fermeture)")
    parser.add_argument('symbole', nargs= '+', metavar= 'symbole', help="Nom d'un symbole boursier")
    args = parser.parse_args()
    if args.début is None:
        args.début = args.fin

    return args

analyser_commande()

def produire_historique(titre, début, fin, valeur):
    
    liste_historique = []
    for symbole in titre:
        liste_date = []
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
        params = {'début': str(début), 'fin': str(fin)}
        réponse = requests.get(url=url, params=params)
        réponse = json.loads(réponse.text)
        if "message d'erreur" not in réponse:
            date_actuelle = début
            while date_actuelle <= fin:
                date_actuelle = début 
                if date_actuelle.weekday() < 5:
                    liste_date.append((date_actuelle, réponse['historique'][date_] valeur_date))
                        valeur_date = réponse["historique"][date_str][valeur]
                        liste_historique.append((date_actuelle, valeur_date))
                        date_actuelle += datetime.timedelta(days=1)
               
    return liste_historique 
                
          
     

def afficher_historique(symbole_affiche, début_affiche, fin_affiche, valeur_affiche):
    print(f'titre={symbole_affiche}: début={début_affiche}: fin={fin_affiche}: valeur={valeur_affiche}')
    for j in range(len(valeur)):
        date, valeur = valeur[j]
        print(f'({date}, {valeur})', end=" ")
        print()  
       
        

arguments = analyser_commande()
liste_symbole = arguments.symbole
date_début = arguments.début
date_fin = arguments.fin
liste_valeur = arguments.valeur
liste_historique = produire_historique(liste_symbole, date_début, date_fin, liste_valeur)
afficher_historique(liste_symbole, date_début, date_fin, liste_valeur)




    



    




