"""
Replace the contents of this module docstring with your own details.
"""
import csv

def menu():
    print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
    menuChoice = str(input())
    while menuChoice != 'Q' or 'q':
        if menuChoice == 'L' or 'l':
            songsList()
            return
        elif menuChoice == 'A' or 'a':
            songsAdder()
            return
        elif menuChoice == 'C' or 'c':
            songsComplete()
            return
        else:
            break

def songsList():
    songRead = open("songs.csv", "r")
    songs = []
    for element in songRead:
        songs.append(element.split(','))
    for i in songs:
        i[3] = i[3].strip('\n')

    songCount = 0
    songsLearnt = 0
    songsToLearn = 0
    for songElement in songs:
        if songElement[3] == 'n':
            songElement[3] = ('*')
            songsToLearn += 1
        else:
            songElement[3] = (' ')
            songsLearnt += 1
        songCount += 1
        print("{}. {} {:40}- {:<30}({:4})".format(songCount, songElement[3], songElement[0], songElement[1],
                                                  songElement[2]))
    print("{:} songs learned, {:} songs still to learn".format(songsLearnt, songsToLearn))
    songRead.close()
    return songs

def songsAdder(songs):
    songAdd = open("songs.csv", "a+")
    songs.songElement[0] = str(input("Title: "))
    while songs.songElement[0] == '':
        songs.songElement[0] = str(input("Input cannot be blank."))
    songs.songElement[1] = str(input("Artist: "))
    while songs.songElement[1] == '':
        songs.songElement[1] == str(input("Input cannot be blank."))
    try:
        songs.songElement[2] = int(input("Year: "))
        while songs.songElement[2] < 1000:
            songs.songElement[2] = int(input("Enter a valid year: "))
    except ValueError:
        songs.songElement[2] = int(input("Invalid input; enter a valid year: "))
    print("{} by {} ({}) added to song list".format(songs.songElement[0], songs.songElement[1], songs.songElement[2]))



def songsComplete(songs):
    valid_input = False
    while not valid_input:
        try:
            songSelect = int(input("Enter the number of a song to mark as learned: "))
            valid_input = True
            while songSelect < 0:
                print("Number must be >= 0")
                songSelect = int(input("Enter the number of a song to mark as learned: "))

            if songs.songElement[3] == '*':
                print("{} by {} learned".format(songs.songElement[0],songs.songElement[1]))
            else:
                print("You have already learned {}".format(songs.songElement[0]))
        except ValueError:
            songSelect = int(input("Invalid input; enter a valid number: "))


def main(songs):
    userName = str(input("Please enter your name: "))
    print("Songs To Learn 1.0 - by {}".format(userName))
    print("{} songs loaded".format(songs.songCount))
    print(menu)
    #testing comment

if __name__ == '__main__':
    main()
