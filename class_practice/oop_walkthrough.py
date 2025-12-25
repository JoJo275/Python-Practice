# oop_walkthrough.py

# STEP 0: A plain dictionary (what you already know)
cat_dict = {"name": "Mochi", "mood": "happy"}

def meow_dict(cat):
    print(cat["name"], "says meow! Mood:", cat["mood"])

meow_dict(cat_dict)

print("DICT:", cat_dict)
print()


# STEP 1: A class (cookie cutter / blueprint)
class Cat:
    pass

# Make an object (a cat cookie)
cat1 = Cat()

# Give it attributes (stickers)
cat1.name = "Mochi"
cat1.mood = "happy"

print("CLASS OBJECT:", cat1)
print("cat1.name =", cat1.name)
print("cat1.mood =", cat1.mood)
print()


# STEP 2: Show the "backpack" (internal attribute storage)
print("cat1 backpack (internal storage) =", cat1.__dict__)
print()


# STEP 3: Add a method (a button the object can press)
class Cat:
    def meow(self):
        print(self.name, "says meow! Mood:", self.mood)

cat2 = Cat()
cat2.name = "Sushi"
cat2.mood = "sleepy"

cat2.meow()
print()


# STEP 4: The big mystery: what is self?
# self is just: "this object right here"
# These two lines do the same thing:
cat2.meow()
Cat.meow(cat2)   # calling the function inside the class manually
print()


# STEP 5: Use __init__ so every cat is born with stickers already
class Cat:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def meow(self):
        print(self.name, "says meow! Mood:", self.mood)

cat3 = Cat("Pudding", "excited")
cat3.meow()

print("cat3 backpack =", cat3.__dict__)
print()


# STEP 6: A slightly more realistic example: a counter
class Counter:
    def __init__(self):
        self.value = 0  # sticker starts at 0

    def add_one(self):
        self.value += 1

c = Counter()
print("Counter starts at:", c.value)
c.add_one()
c.add_one()
print("Counter after two add_one():", c.value)
print("Counter backpack:", c.__dict__)
