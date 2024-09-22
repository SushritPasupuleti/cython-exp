cdef struct Person:
    char *name
    int age
    char *city
    char *country
    char *email

cdef str mainC(list[Person] data):

    for item in data:
        if item["age"] > 25:
            # print(item["name"], item["age"])
            return "Old"
        elif item["city"] == "New York":
            # print(item["name"], item["city"])
            return "New York"
        else:
            # print(item["name"], item["country"])
            return "Done"

def main(data):
    return mainC(data)
