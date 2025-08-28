ingredients = {"flour", "sugar", "butter"}

ingredients.add("eggs")

ingredients.remove("sugar")
print(ingredients)

set_a = {"flour", "sugar", "butter"}
set_b = {"sugar", "eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)