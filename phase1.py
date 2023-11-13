import argparse
import datetime


def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers")
    parser.add_argument('-d', '--début', metavar= 'DATE', dest= 'début', type= ...help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument('-f', '--fin', metavar= 'DATE', dest= 'fin', type= help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument('-v', '--valeur', dest= 'valeur', choices= ['fermeture', 'ouverture', 'min', 'max', 'volume'], default= 'fermeture', help="La valeur désirée (par défaut: fermeture)")
    parser.add_argument('symbole', nargs= '+', metavar= 'symbole', help="Nom d'un symbole boursier")
    args = parser.parse_args()
    if args.début is None:
        args.début = args.fin

    return args

analyser_commande()
    




