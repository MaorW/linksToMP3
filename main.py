# import requests

"""
###  linksToMp3 - Create MP3 files with Youtube links  ###
This program will download Youtube's songs using their links -> download them and put them on a sub-folder.

## The program steps: ##
1. Create a CSV file named "songs_links.csv" if not exists - Titles will be "date" and "link".
2. Check if the file is blank. If it does, exit the program and send a message to the user.
   If the file is not empty:
    A. Get the Youtube link from the current line.
    B. Find the song by using get request. If there's an issue. Exit and send a message to the user.
    C. Create a folder which will be named by the current date (If doesn't exist already)
    D. Download the file and put it to the current date's folder
    E. Mark on the CSV file that this song has been downloaded on the current row
3. Repeat those subtasks until the last row

"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    # Create a CSV file named "songs_links.csv" if not exists
    #


