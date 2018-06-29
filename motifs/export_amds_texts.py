# deps
import pymysql.cursors
import itertools
from collections import defaultdict
from pprint import pprint
import csv


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='nosdeputes',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


with connection.cursor() as cursor:
    
    cursor.execute(""" SELECT id, expose from amendement WHERE sort !='rejeté' GROUP BY content_md5""")

    with open('amds_txt.csv','w') as outputfile:
        amds = csv.DictWriter(outputfile, fieldnames = ['id','expose'])
        amds.writeheader()
        for l in cursor:
            amds.writerow(l)  