# import requests
import csv
import os
import sys

file_name = './songs_links.csv'


def csv_creation():
    with open('songs_links.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Song Name", "Author", "Youtube Link", "Status"])


def isFiedsEmpty(fileName):
    with open(fileName, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if row[0][0] == 'Song Name':
                continue
            if row[0][0]:
                print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Check if csv file exists and its values
    if not os.path.isfile(file_name):
        csv_creation()
        print("Please fill the 'songs_links.csv' fields")
        sys.exit()
