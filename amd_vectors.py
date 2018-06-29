# deps
import pymysql.cursors
import itertools
from collections import defaultdict
from pprint import pprint
import csv
import re


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='nosdeputes',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

groupe_majorite = {15: ['LREM', 'MODEM'], 14: ['SRC','ECOLO', 'RRDP'], 13: ['UMP','NC']}


with connection.cursor() as cursor:
    
    # concurrence
    cursor.execute(""" SELECT group_concat(id) as ids, count(*) as nb_concurrent from amendement WHERE sort !='rejeté' GROUP BY legislature, texteloi_id, sujet""")
    concurrence = {}
    for l in cursor:
        for amd_id in l['ids'].split(','):
            concurrence[int(amd_id)] = l['nb_concurrent']

    # auteurs
    cursor.execute("""SELECT po.parlementaire_id as pid, o.nom as groupe
    FROM organisme as o JOIN parlementaire_organisme as po ON po.organisme_id = o.id
    WHERE o.type='groupe' AND fonction IN ('président','présidente')
    """)
    president_groupe = {c['pid']:c['groupe'] for c in cursor}
    

    cursor.execute("""SELECT amendement_id, 
        group_concat(parlementaire_id ORDER BY numero_signataire) as signataires,
        group_concat(parlementaire_groupe_acronyme ORDER BY numero_signataire) as groupes
    FROM parlementaire_amendement
    GROUP BY amendement_id""")
    nb_auteurs = {}
    presidents = {}
    groupes = {}
    for l in cursor:
        ss = l['signataires'].split(',')
        nb_auteurs[int(l['amendement_id'])] = len(ss)
        presidents[int(l['amendement_id'])] = president_groupe[int(ss[0])] if int(ss[0]) in president_groupe else None
        groupes[int(l['amendement_id'])] = set(l['groupes'].split(',')) 


    cursor.execute(""" SELECT id, sort, count(*) as duplicates, signataires, legislature from amendement WHERE sort !='rejeté' GROUP BY content_md5""")
    
    amds = {}
    for amendement in cursor:
        amendement_id = int(amendement['id'])
        amds[amendement_id] = amendement
        amds[amendement_id]['concurrents'] = concurrence[amendement_id] if amendement_id in concurrence else 0
        # auteurs
        if amendement_id in nb_auteurs:
            amds[amendement_id]['nb_signataires'] = nb_auteurs[amendement_id]
            amds[amendement_id]['signataire_special'] = "president_groupe" if presidents[amendement_id] else None
        elif re.match(r"Le Gouvernement",amendement['signataires'], re.I) :
            amds[amendement_id]['nb_signataires'] = 1
            amds[amendement_id]['signataire_special'] = "gouvernement"
        else:
            print("unknown signataires for %s : '%s'"%(amendement_id, amendement['signataires']))
        # majorité
        majorite = len(groupes[amendement_id] - set(groupe_majorite[int(l['legislature'])]) )==0 and groupes[amendement_id] & set(groupe_majorite[int(l['legislature'])]) :
        amds[amendement_id]['majorite'] = majorite

        # baaaa durty
        headers = amds[amendement_id]


    with open('amds_vectors.csv','w') as outputfile:
        csvfile = csv.DictWriter(outputfile, fieldnames = headers)
        csvfile.writeheader()
        
        for l in amds.values():
            csvfile.writerow(l)  