"""Takes a file of restaurant names and ratings, imports that data into a 
dictionary, then loops through the dictionary to print each restaurant and
its rating.
"""

def main():
    f = open("scores.txt")

    rest_ratings = {}
    sorted_by_rating = {}

    for line in f:
        data = line.split(":")
        data[1] = data[1].rstrip()
        rest_ratings[data[0]] =  int(data[1])

    sort_ratings = sorted(rest_ratings.values())
    print sort_ratings

    """Create new dictionary to contain key-value pairs where the key
    includes the rating.  
    """

    for restaurant, ratings in rest_ratings.iteritems():
        print "Restaurant %s is rated at %d." % (restaurant, ratings)

    print sorted(rest_ratings.items(), key = lambda x: x[1])

if __name__ == "__main__":
    main()
