def process_ratings (filename):
    data = open(filename)
    updated_data = sorted(data)

    for line in updated_data: 
        updated_line = line.rstrip()
        process = updated_line.split(":") 
        print "%s rating is %s." % (process[0], process[1])     

#process_ratings("scores.txt")

def process_ratings2 (filename):
    data = open(filename)

    restaurant_dict = {}

    for line in data:
        updated_line = line.rstrip()
        process = updated_line.split(":")
        restaurant_dict[process[0]] = process[1]

    for key, value in sorted(restaurant_dict.items()):
        print "%s is rated at %s" %(key, value)

process_ratings2("scores.txt")
