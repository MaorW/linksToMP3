# import requests
import csv
import os
import sys
import platform

file_name = './songs_links.csv'


def csv_creation():
    with open('songs_links.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Song Name", "Author", "Youtube Link", "Status"])


def youtube_dl_install():
    # If OS is Windows - Do a Windows Installation
    if platform.system == 'Windows':
        windows_youtube_dl_install()
    elif platform.system == 'Linux':
        windows_youtube_dl_install()
    elif platform.system == 'Darwin':
        windows_youtube_dl_install()


def windows_youtube_dl_install():
    pass


def linux_youtube_dl_install():
    pass


def mac_youtube_dl_install():
    pass


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
    #Todo - Check if there's youtube_dl pip pkg installed

    # If there's no youtube_dl pip pkg - Install it
    youtube_dl_install()

    # Check if csv file exists and its values
    if not os.path.isfile(file_name):
        csv_creation()
        print("Please fill the 'songs_links.csv' fields")
        sys.exit()

