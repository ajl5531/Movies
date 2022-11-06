import sys
from dataclasses import dataclass
from timeit import default_timer as timer
from operator import itemgetter

"""...."""
@dataclass
class Movie:
    tconst: str
    titleType: str
    primaryTitle: str
    startYear: str
    runTime: int
    genres: str


@dataclass
class Rating:
    tconst: str
    averageRating: float
    numVotes: int


def readFile(text_file1, text_file2):
    """
    The readFile function reads the movie and rating dataset into a dictonary. It does this by opening both
    files and turns each line into a object which will be added to the dictionary with it's tconstant as it's
    key and will return the movie and rating datasets as a dictionary.
    :param text_file1:
    :param text_file2:
    :return: dict_movie, dict_rating
    """

    movie_count = 0
    rating_count = 0
    dict_movie = {}
    dict_rating = {}

    # opens the movie data file and adds the objects into a dictionary
    print("reading", text_file1, "into dict...")
    start_time = timer()
    with open(text_file1, encoding='utf-8') as f:
        f.readline()
        for line in f:
            fields = line.split('\t')
            if fields[4] == '0':
                while '\\N' in fields[7]:
                    fields[7] = '0'
                movie_temp = Movie(
                    tconst=fields[0],
                    titleType=fields[1],
                    primaryTitle=fields[2],
                    startYear=(fields[5]),
                    runTime=(fields[7]),
                    genres=fields[8].strip('\n')
                )
                dict_movie[movie_temp.tconst] = movie_temp
                movie_count += 1
    elapsed = timer() - start_time
    print("time elapsed (s):", elapsed, "\n")
    print("reading " + text_file2 + " into dict...")

    # opens the Rating data file and adds them to a dictioanry
    start_time = timer()
    with open(text_file2, encoding='utf-8') as f:
        f.readline()
        for line in f:
            fields = line.split('\t')
            rating_temp = Rating(
                tconst=fields[0],
                averageRating=float(fields[1]),
                numVotes=int(fields[2])
            )
            dict_rating[rating_temp.tconst] = rating_temp
            rating_count += 1
    elapsed = timer() - start_time

    # prints the time elapsed and the total movies and ratings
    print("time elapsed (s):", elapsed, "\n")
    print("Total movies: ", movie_count, "\n",
          "Total ratings: ", rating_count, "\n", sep='')
    # print(dict_movie)
    # print('')
    # print(dict_rating)
    # x = dict_movie['tt0033467']
    # print(x.titleType)
    return dict_movie, dict_rating


def contains(title_type, word: str, dict_movie: dict):
    """
    The contains function to search for a movie in two stages. It first checks if the title type matches
    the movie. Second, it checks if the mname of the movie contains a word. There are two possible outcomes.
    If a movie is found, then it would print it's descriptiom. Else, the console states that the movie
    has not been found.
    :param dict_movie:
    :param word:
    :param title_type:
    :return: None
    """
    list1 = []
    sort_list = []

    # a for loop is used to iterate over the dictionary and if it matches the title_type and word parameters
    # then it is added to a list where it will be sorted
    start_time = timer()
    print('processing: CONTAINS', title_type, word)
    for key in dict_movie:
        if dict_movie[key].titleType == title_type:
            temp_list = [dict_movie[key].tconst, dict_movie[key].primaryTitle, dict_movie[key].titleType,
                         dict_movie[key].startYear, dict_movie[key].runTime, dict_movie[key].genres]
            list1.append(temp_list)
            for i in range(len(list1)):
                if word in list1[i][1]:
                    sort_list.append(list1[i])

    # if the list is empty then no match is found
    # else the list is sorted and then printed
    if len(sort_list) == 0:
        print('\t' + 'No match found!')
    else:
        sort_list = sorted(sort_list, key=itemgetter(1))
        for i in range(len(sort_list)):
            print('\t', 'Identifier: ', sort_list[i][0],
                  ', Title: ', sort_list[i][1],
                  ', Type: ', sort_list[i][2],
                  ', Year: ', sort_list[i][3],
                  ', Runtime: ', sort_list[i][4],
                  ', Genres: ', sort_list[i][5], sep='')

    # prints the time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def lookUp(dict_movie: dict, dict_rating: dict, tconst: str):
    """
    The lookUp function checks to see if the movie or rating is located in the data file.
    There are two outcomes, if the movie or rating is found then it would output its full description.
    Else, the console would state that it could not be found.
    :param tconst:
    :param dict_movie:
    :param dict_rating:
    :return: a data structure
    """

    # checks if the movie dictionary contains the tconstant
    print('processing: LOOKUP ' + tconst)
    start_time = timer()
    if tconst in dict_movie:
        print('\t', 'MOVIE: Identifier: ', dict_movie[tconst].tconst, ', Title: ', dict_movie[tconst].primaryTitle,
              ', Type: ', dict_movie[tconst].titleType, ', Year: ', dict_movie[tconst].startYear,
              ', Runtime: ', dict_movie[tconst].titleType, ', Genres: ', dict_movie[tconst].genres, sep='')
    else:
        print('\t' + 'Movie not found!')

    # checks if the rating dictionary contains the tconstant
    if tconst in dict_rating:
        print('\t', 'RATING: Identifier: ', dict_rating[tconst].tconst, ' Rating: ', dict_rating[tconst].averageRating,
              ', Votes: ', dict_rating[tconst].numVotes, sep='')
    else:
        print('\t' + 'Rating not found!')

    # prints the total time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def yearAndGenre(dict_movie: dict, title_type, start_year, genre):
    """
        The yearAndGenre function checks if a movie's start year and genre matches. it does this by
        checking if the title type and start year matches the movie. The function then checks if the genre matches
        the movie. The function then prints the sorted movies.
        :param genre:
        :param start_year:
        :param title_type:
        :param dict_movie:
        :return: None
    """
    list1 = []
    sort_list = []
    start_time = timer()
    print('processing: YEAR_AND_GENRE', title_type, start_year, genre)

    # a for loop is used to iterate over the dictonary and if it matches the title_type and start year parameters
    # then it is added to a list where it will be sorted
    for key in dict_movie:
        if dict_movie[key].titleType == title_type and dict_movie[key].startYear == start_year:
            temp_list = [dict_movie[key].tconst, dict_movie[key].primaryTitle, dict_movie[key].titleType,
                         dict_movie[key].startYear, dict_movie[key].runTime, dict_movie[key].genres]
            list1.append(temp_list)
    for i in range(len(list1)):
        if genre in list1[i][5]:
            sort_list.append(list1[i])

    # if the list is empty then no match is found
    # else the list is sorted and then printed
    if len(sort_list) == 0:
        print('\t' + 'No match found!')
    else:
        sort_list = sorted(sort_list, key=itemgetter(1))
        for i in range(len(sort_list)):
            print('\t', 'Identifier: ', sort_list[i][0],
                  ', Title: ', sort_list[i][1],
                  ', Type: ', sort_list[i][2],
                  ', Year: ', sort_list[i][3],
                  ', Runtime: ', sort_list[i][4],
                  ', Genres: ', sort_list[i][5], sep='')

    # prints the time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def runTime(dict_movie, title_type, start: int, end: int):
    """
        The runTime function prints the movies whose runtime is between two numbers (inclusive)
        It first checks if the title type matches the movie. Second, it sorts the filtered list alphabetically
        and by the number of votes. Then it prints the sorted movies.
        :param start: the start year
        :param end: the end year
        :param title_type: a title type
        :param dict_movie: a dictionary of ratings with it's tconst as they key
        :return: None
    """
    list1 = []
    sort_list = []
    start_time = timer()
    print('processing: RUNTIME', title_type, start, end)
    for key in dict_movie:
        if dict_movie[key].titleType == title_type:
            temp_list = [dict_movie[key].tconst, dict_movie[key].primaryTitle, dict_movie[key].titleType,
                         dict_movie[key].startYear, dict_movie[key].runTime, dict_movie[key].genres]
            list1.append(temp_list)
    for i in range(len(list1)):
        if start <= int(list1[i][4]) <= end:
            sort_list.append(list1[i])

    # if the list is empty then no match is found
    # else the list is sorted and then printed
    if len(sort_list) == 0:
        print('\t' + 'No match found!')
    else:
        sort_list = sorted(sort_list, key=itemgetter(1))
        for i in range(len(sort_list)):
            print('\t', 'Identifier: ', sort_list[i][0],
                  ', Title: ', sort_list[i][1],
                  ', Type: ', sort_list[i][2],
                  ', Year: ', sort_list[i][3],
                  ', Runtime: ', sort_list[i][4],
                  ', Genres: ', sort_list[i][5], sep='')

    # prints the time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def mostVotes(dict_rating, dict_movie, title_type, num):
    """
        The most votes function prints the top number of up voted movies specified by the num parameter.
        It first checks if the title type matches the movie. Second, it sorts the filtered list alphabetically
        and by the number of votes. Then it prints the sorted movies.
        :param dict_rating: a dictionary of ratings with it's tconst as they key
        :param dict_movie: a dictionary of movies with it's tconst as they key
        :param title_type: a title type
        :param num: a number
        :return: None
    """
    list1 = []
    start_time = timer()
    print('processing: MOST_VOTES', title_type, num)
    for key in dict_movie:
        try:
            if dict_movie[key].titleType == title_type:
                temp_list = [dict_rating[key].numVotes, dict_movie[key].tconst, dict_movie[key].primaryTitle,
                             dict_movie[key].titleType, dict_movie[key].startYear, dict_movie[key].runTime,
                             dict_movie[key].genres]
                list1.append(temp_list)
        except KeyError as e:
            pass

    # the list is sorted alphebetically and then sorted by the number of votes
    list1.sort(key=itemgetter(2))
    list1.sort(key=itemgetter(0), reverse=True)

    # if the list is empty then no match is found
    # else the list is printed
    if len(list1) == 0:
        print('\t' + 'No match found!')
    else:
        try:
            for i in range(int(num)):
                print('\t', i + 1, '.  '' Votes: ', list1[i][0],
                      ' Identifier: ', list1[i][1],
                      ', Title: ', list1[i][2],
                      ', Type: ', list1[i][3],
                      ', Year: ', list1[i][4],
                      ', Runtime: ', list1[i][5],
                      ', Genres: ', list1[i][6], sep='')
        except IndexError as e:
            pass

    # prints the time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def top(dict_movie, dict_rating, title_type, num, start, end):
    """
        The Top function prints a list of movies that have at least 1000 votes for each year in a range of years
        It first checks if the title type matches the movie. Second, it takes the range of the years and
        adds the movies according to it's year. The list of movies in each year is then sorted alphabetically
        and sorted by its rating and is then printed.
        :param dict_movie: a dictionary of movies with it's tconst as they key
        :param dict_rating: a dictionary of ratings with it's tconst as they key
        :param title_type: a title type
        :param num: a number
        :param start: start year
        :param end: end year
        :return: None
    """
    list1 = []
    start_time = timer()
    print('processing: TOP', title_type, num, start, end)
    for key in dict_movie:
        try:
            if dict_movie[key].titleType == title_type:
                temp_list = [dict_rating[key].averageRating, dict_rating[key].numVotes, dict_movie[key].tconst,
                             dict_movie[key].primaryTitle, dict_movie[key].titleType, dict_movie[key].startYear,
                             dict_movie[key].runTime, dict_movie[key].genres]
                list1.append(temp_list)
        except KeyError as e:
            pass
    len_year = int(end) - int(start) + 1
    year_list = []
    for i in range(len_year):
        year_list.append([])
    year_temp = int(start)

    for i in range(int(len_year)):
        for x in range(len(list1)):
            if year_temp == int(list1[x][5]):
                year_list[i].append(list1[x])
            else:
                pass
        year_temp += 1

    # if the list is empty then no match is found
    # else the list is sorted and then printed
    year_temp2 = int(start)
    for i in range(len(year_list)):
        print('\t', 'YEAR: ', year_temp2, sep='')
        year_temp2 += 1
        if len(year_list[i]) == 0:
            print('\t' + '\t' + 'No match found!')
        else:
            year_list[i].sort(key=itemgetter(3))
            year_list[i].sort(key=itemgetter(0), reverse=True)
            for x in range(len(year_list[i])):
                if year_list[i][x][1] >= 1000:
                    print('\t', '\t' , x + 1, '. Rating: ', year_list[i][x][0],
                          ', Votes: ', year_list[i][x][1],
                          ', Identifier: ', year_list[i][x][2],
                          ', Title: ', year_list[i][x][3],
                          ', Type: ', year_list[i][x][4],
                          ', Year: ', year_list[i][x][5],
                          ', Runtime: ', year_list[i][x][6],
                          ', Genres: ', year_list[i][x][7], sep='')

    # prints the time elapsed
    elapsed = timer() - start_time
    print('elapsed time (s):', elapsed, '\n')


def main():
    """
    The main function uses the command line to determine if the data file will be large or small.
    The program will then prompt the user to input file names for the input files.
    The the input files would then be used to send the data to their respective queries
    :return None
    """
    input_file = 'input/all-small.txt'
    s = "small"
    if len(sys.argv) == 2 and sys.argv[1] == 'small':
        s = "small"
    dict_movie, dict_rating = readFile('data/' + s + '.basics.tsv'
                                       , 'data/' + s + '.ratings.tsv')
    with open(input_file) as f:
        for line in f:
            fields = line.split(' ')
            fields[len(fields) - 1] = fields[len(fields) - 1].strip('\n')

            # data will go to their respective list depending on it's 0 index in the field list
            if fields[0] == 'LOOKUP':
                lookUp(dict_movie, dict_rating, fields[1])
            elif fields[0] == 'CONTAINS':
                for i in range(len(fields)):
                    if len(fields) > 3:
                        word = ''
                        for k in range(2, len(fields)):
                            word += fields[k] + ' '
                        fields = [fields[0], fields[1], word]
                        fields[2] = fields[2].rstrip()
                contains(fields[1], fields[2], dict_movie)
            elif fields[0] == 'YEAR_AND_GENRE':
                yearAndGenre(dict_movie, fields[1], fields[2], fields[3])
            elif fields[0] == 'RUNTIME':
                runTime(dict_movie, fields[1], int(fields[2]), int(fields[3]))
            elif fields[0] == 'MOST_VOTES':
                mostVotes(dict_rating, dict_movie, fields[1], fields[2])
            elif fields[0] == 'TOP':
                top(dict_movie, dict_rating, fields[1], fields[2], fields[3], fields[4])


if __name__ == '__main__':
    main()
