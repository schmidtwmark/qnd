import random

ice_creams = ["Vanilla", "Chocolate", "Cookies and Cream"]
vanilla_count = 0
chocolate_count = 0
cookies_and_cream_count = 0
for i in range(0, 1000000):
    random_ice_cream = random.choice(ice_creams)
    if random_ice_cream == "Vanilla":
        vanilla_count += 1
    elif random_ice_cream == "Chocolate":
        chocolate_count += 1
    elif random_ice_cream == "Cookies and Cream":
        cookies_and_cream_count += 1
    

print(f"Vanilla: {vanilla_count}")
print(f"Chocolate: {chocolate_count}")
print(f"Cookies and Cream: {cookies_and_cream_count}")
