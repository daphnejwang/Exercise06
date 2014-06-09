"""Takes a file of restaurant names and ratings, imports that data into a 
dictionary, then loops through the dictionary to print each restaurant and
its rating.
"""

def main():
    f = open("scores.txt")

    rest_ratings = {}

    for line in f:
        data = line.split(":")
        data[1] = data[1].rstrip()
        rest_ratings[data[0]] =  int(data[1])

    for restaurant in sorted(rest_ratings.keys()):
        print "Restaurant %s is rated at %d." % (restaurant, rest_ratings[restaurant])

if __name__ == "__main__":
    main()
