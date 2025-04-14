import csv

years = {}
artists = {}
fix = {                                     #se tienen que hacer unas correcciones por el encoding que tiene cada csv
    "SinÍ©ad O'Connor": "Sinéad O’Connor",
    "CÍ©line Dion": "Céline Dion",
    "Puff Daddy & Faith Evans": "Faith Evans",
    "Los Del RÍ_o": "Los del Río",
    "All-4-One": "All for One",
    "Brandy & Monica": "Brandy & Monica",
    "Ms. Lauryn Hill": "Lauryn Hill"
}
fix2 = {                                            #este directamente no tenia datos para algunos
    "All for One": ["United States", "North America"],
    "Brandy & Monica" : ["United States", "North America"]
}
with open("NVDecades.csv") as csvfile:

    csvreader = csv.reader(csvfile)
    num = 0
    for line in csvreader:
        if num >100:
            if line[-1] not in years:
                years[line[-1]] = [line[2]]
            else:
                if line[2] in fix:
                    years[line[-1]].append(fix[line[2]])
                else:    
                    years[line[-1]].append(line[2])
        num+=1
        if num ==201:
            break


for i in years["1990s"]:
    if i not in artists:
        artists[i] = [1]
    else:
        artists[i][0] +=1


regions = {}

with open("Countries by continents.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    num = 0
    for i in csvreader:
        if num>0:
            if i[0] not in regions:
                regions[i[0]] = [i[1]]
            else:
                regions[i[0]].append(i[1])
        num+=1
for i in fix2:
    artists[i].extend([fix2[i][0], fix2[i][1]])

with open("artists.csv", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    num = 100
    for i in csvreader:
        artist = i[1].strip()
        if artist in artists and len(artists[i[1]]) != 3:
            #print(i[1], num)
            country = i[3]
            artists[artist].append(country)
            for j in regions:
                if country in regions[j]:
                    artists[i[1]].append(j)
            num-=1
        if num == 0: break



artists2 = []

for i in artists:
    artists2.append([i, artists[i][0], artists[i][1], artists[i][2]])

artists2 = sorted(artists2, key= lambda x : int(x[1]), reverse=True)

with open("Dataset_to_use.csv", mode='w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Artista', 'Apariciones', 'Pais', 'Region'])  # Escribir encabezados
    for i in range(len(artists2)):
        writer.writerow([artists2[i][0], artists2[i][1], artists2[i][2], artists2[i][3]])
print("Dataset creado")