import csv


#ler uma planilha em csv
def ler_csv():
    with open('mangas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)