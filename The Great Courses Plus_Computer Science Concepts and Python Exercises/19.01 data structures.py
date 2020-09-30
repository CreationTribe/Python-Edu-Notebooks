# dict actions

nicknames = {}

nicknames["Superstar"] = "Sue Smith"
nicknames["DonkeyDongDoug"] = "Dude's Dad"
nicknames["Fraud Burger"] = "Joseph Smith"
nicknames["Dinkerhoffer"] = "Don Hoffman"

del nicknames["Dinkerhoffer"]

if "Dude's Dad" in nicknames:
    print("Dude's Dad is still here - we should ditch im!")
else:
    print("Dude's Dad is no longer with us :(  !")

# print(nicknames["Superstar"])
# print(nicknames["DonkeyDongDoug"])
# print(nicknames["Fraud Burger"])
# print(nicknames["Dinkerhoffer"])

# sets
# just like dict, but no key

my_set = {"Joe", "Mary", "Jane", "Dirk"}

if "Joe" in my_set:
    print("Yup, Joe's in here!")

# another way to instantiate a set
# use the "set" keyword
my_other_set = set(["Jake", "Donny", "Richie", "Gloria"])

if "Gloria" in my_other_set:
    print("Gloria be here!")

# NOTE: to create an empty set, you MUST use the set keyword. Empty
# curley braces will just make an empty dict
my_empty_set = set()

my_empty_set.add("LSD")
my_empty_set.add("DMT")
my_empty_set.add("psilocybin")
my_empty_set.add("marijuana")
my_empty_set.add("alcohol")

print(my_empty_set)

my_empty_set.remove('alcohol')

print(my_empty_set)

# Negation
print(my_empty_set - my_set)

# Union
print(my_set | my_other_set)

# Intersection
print(my_other_set & my_empty_set)

# Either (exclusive OR) Union minus Intersection
print(my_empty_set ^ my_set)
