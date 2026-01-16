import csv

input_csv = "Q_64_latest-2025-2026_RR-T-Vent.csv"
output_csv = "Q_64_latest-2025-2026_RR-T-Vent_clean.csv"

with open(input_csv, newline='', encoding='utf-8') as infile, \
     open(output_csv, "w", newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header[0].split(";")[0:6] + ["TM"])  # Écrire l'en-tête avec la colonne TM

    removed = 0
    for row in reader:
        row = row[0].split(";")#on split car le csv utilise des ; comme séparateur
        if len(row) > 17 and row[16] != "": #on vérifie que la 17ème colonne (index 16) n'est pas vide car elle correspond à TM la température
            writer.writerow(row[0:6] + [row[16]]) #on écrit les colonnes de 0 à 5 et la 16ème
        else:
            removed += 1
    

input_csv = "Q_64_latest-2025-2026_RR-T-Vent_clean.csv"
output_csv = "data.csv"

with open(input_csv, newline='', encoding='utf-8') as infile, \
     open(output_csv, "w", newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    print(header)
    writer.writerow(header[2:-1] + ["TMJ-4"] + ["TMJ-3"] + ["TMJ-2"] + ["TMJ-1"] + ["TM"])  # Écrire l'en-tête avec les colonnes TMJ-1 à TMJ-5

    adPost = ""
    lT = []
    for row in reader:
        if adPost == '':
            adPost = row[0]
            lT.append(row[6])
        elif adPost != row[0]:
            adPost = row[0]
            lT = []+ [row[6]]
        elif adPost == row[0] and len(lT) == 4:
            lT = lT + [row[6]]
            writer.writerow(row[2:6] + lT)
            lT= lT[1:]
        elif adPost == row[0] and len(lT) < 4:
            lT.append(row[6])
        else:
            print("Erreur inattendue lors du traitement des données.")

print(f"Nettoyage terminé. Fichier sauvegardé sous '{output_csv}'.")