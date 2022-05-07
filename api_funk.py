import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv_func as csv

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
my_creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(my_creds)

def getf(num):
    curators = client.open('Maraphon_2').get_worksheet(num)
    get = curators.col_values(2)
    return get
def get_cf(num):
    curators = client.open('Maraphon_2').get_worksheet(num)
    get_c = curators.col_values(16)
    return get_c

def rep(members):
    for i in range(len(members)):
        members[i][1] = members[i][1].replace(',','.')
        members[i][1] = members[i][1].replace('"','')
    return members

print('---------------------START--------------------')


get = getf(6)
get_c = get_cf(6)
trus = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(trus)
csv.write('Curator/Трусь.csv', trus)

get = getf(2)
get_c = get_cf(2)
troc = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(troc)
csv.write('Curator/Троц.csv', troc)

get = getf(3)
get_c = get_cf(3)
vain = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(vain)
csv.write('Curator/Вайнилович.csv', vain)

get = getf(4)
get_c = get_cf(4)
evtu = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(evtu)
csv.write('Curator/Евтушик.csv', evtu)

get = getf(7)
get_c = get_cf(7)
greb = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(greb)
csv.write('Curator/Гребнева.csv', greb)

get = getf(5)
get_c = get_cf(5)
kots = [[get[i], get_c[i]] for i in range(2, len(get_c))]
rep(kots)
csv.write('Curator/Котусова.csv', kots)


def cust(count):
    return count[1]
def floating(list):
    for item in list:
        item[1] = float(item[1])
    return list

get = getf(0)
get_c = get_cf(0)
all = [[get[i], get_c[i]] for i in range(1, len(get_c))]
rep(all)
all = floating(all)
all.sort(reverse=True, key=cust)
csv.write('Curator/All.csv', all)

print('----------------------END---------------------')






