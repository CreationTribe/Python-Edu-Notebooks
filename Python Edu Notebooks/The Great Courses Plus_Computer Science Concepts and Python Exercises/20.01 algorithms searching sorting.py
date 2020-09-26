def is_in(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            return True
        else:
            i += 1
    return False


favorite_foods = ['pizza', 'ice cream', 'gumbo', 'tacos', 'corn']
print(is_in(favorite_foods, 'ice cream'))
print(is_in(favorite_foods, 'bacon'))

# in does the same thing
print('ice cream' in favorite_foods)
print('bacon' in favorite_foods)


# loop invariant is the condition that needs to stay the same for the loop to continue

# binary sort ...
def binary_in(s_list, value):
    low = 0
    high = len(s_list)-1

    if s_list[low] == value:
        return low
    elif s_list[high] == value:
        return high

    while low < high-1:
        midpoint = low + (high - low) // 2

        if s_list[midpoint] == value:
            return midpoint
        elif s_list[midpoint] < value:
            low = midpoint
        else:
            high = midpoint
    return -1


fucking_numbers_why = list(range(0, 99))
print(fucking_numbers_why)
print(binary_in(fucking_numbers_why, 30))


# SORTING!!!  #####################################################################

def selection_sort(slist):
    maxindex = len(slist) - 1

    for i in range(0, maxindex-1):
        # find the smallest remaining
        mindex = i

        for j in range(i+1, maxindex+1):
            if slist[j] < slist[mindex]:
                mindex = j

        # swap item
        temp = slist[i]
        slist[i] = slist[mindex]
        slist[mindex] = temp


evil_disney_characters = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                          "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                          "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                          "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

selection_sort(evil_disney_characters)

print(evil_disney_characters)

# insertion sort


def insertion_sort(slist):
    for i in range(0, len(slist)):
        temp = slist[i]
        j = i-1

        while j >= 1 and slist[j] > temp:
            slist[j+1] = slist[j]
            j -= 1

        slist[j+1] = temp


evil_disney_characters_2 = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                            "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                            "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                            "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

insertion_sort(evil_disney_characters_2)
print(evil_disney_characters_2)


# built-in sorting
evil_disney_characters_3 = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                            "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                            "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                            "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

evil_disney_characters_4 = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                            "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                            "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                            "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

evil_disney_characters_5 = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                            "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                            "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                            "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

evil_disney_characters_6 = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                            "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                            "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                            "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

# inplace sorting
evil_disney_characters_3.sort()
print(evil_disney_characters_3)

# inplace reversed
evil_disney_characters_3.sort(reverse=True)
print(evil_disney_characters_3)
