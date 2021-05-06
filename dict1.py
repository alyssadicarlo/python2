meal = {
    "entree": "pesto chicken",
    "drink": "fizzy water",
    "dessert": "ice cream"
}

print(meal["dessert"])
print("Tonight I will have %s for dinner with %s for dessert" % (meal["entree"], meal["dessert"]))

if "dessert" in meal:
    print("OF COURSE!! I had %s" % meal["dessert"])
else:
    print("No dessert")

print(meal)

meal["appetizer"] = "bacon"
meal["drink"] = "sweet pea"

del meal["dessert"]

print(meal)