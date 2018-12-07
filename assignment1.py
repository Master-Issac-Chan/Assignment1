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
    ListOfSongs = []
    for element in songRead:
        ListOfSongs.append(element.split(','))
    for i in ListOfSongs:
        i[3] = i[3].strip('\n')

    songCount = 0
    songsLearnt = 0
    songsToLearn = 0
    for songElement in ListOfSongs:
        if songElement[3] == 'n':
            songElement[3] = ('*')
            songsToLearn += 1
        else:
            songElement[3] = (' ')
            songsLearnt += 1
        songCount += 1
        print("{}. {} {:40}-{:<30}({:10})".format(songCount, songElement[3], songElement[0], songElement[1],
                                                  songElement[2]))
    print("{:} songs learned, {:} songs still to learn".format(songsLearnt, songsToLearn))
    songRead.close()

def songsAdder():
    songAdd = open("songs.csv", "a+")
    songList = {}

def songsComplete():

def main():
    userName = str(input("Please enter your name: "))
    print("Songs To Learn 1.0 - by {}".format(userName))
    print("{} songs loaded".format(songCount))
    print(menu)
    #testing comment

if __name__ == '__main__':
    main()
