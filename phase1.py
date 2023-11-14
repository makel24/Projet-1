import argparse
import datetime
from datetime import date


def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers")
    parser.add_argument('-d', '--début', metavar= 'DATE', dest= 'début', type=datetime.date.fromisoformat, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument('-f', '--fin', metavar= 'DATE', dest= 'fin', default=date.today(), type=datetime.date.fromisoformat, help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument('-v', '--valeur', dest= 'valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default= 'fermeture', help="La valeur désirée (par défaut: fermeture)")
    parser.add_argument('symbole', nargs= '+', metavar= 'symbole', help="Nom d'un symbole boursier")
    args = parser.parse_args()
    if args.début is None:
        args.début = args.fin

    return args

analyser_commande()


liste_date = []


from datetime import date
import requests
import json


def produire_historique(titre, début, fin, valeur):
    for symbole in titre:
        liste_date = []
      


    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    params = {'début': str(début), 'fin': str(fin)}
    réponse = requests.get(url=url, params=params)
    réponse = json.loads(réponse.text)
    

    for symbole in titre:


   



arguments = analyser_commande()
liste_symbole = arguments.symbole
date_début = arguments.début
date_fin = arguments.fin
liste_valeur = arguments.valeur
liste_historique = produire_historique(liste_symbole, date_début, date_fin, liste_valeur)





    



    




