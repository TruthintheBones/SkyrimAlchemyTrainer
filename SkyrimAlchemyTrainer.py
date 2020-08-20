import csv

class Potion:
    def __init__(self,ing_1, ing_2, ing_3):
        self.ing_1 = ing_1
        self.ing_2 = ing_2
        self.ing_3 = ing_3
        self.allTwelveEffects = [Ingredients[ing_1][2], Ingredients[ing_1][4], Ingredients[ing_1][6], Ingredients[ing_1][8], Ingredients[ing_2][2], Ingredients[ing_2][4], Ingredients[ing_2][6], Ingredients[ing_2][8], Ingredients[ing_3][2], Ingredients[ing_3][4], Ingredients[ing_3][6], Ingredients[ing_3][8]]

        self.effects=[]
        for i in range(12):
            if self.allTwelveEffects.count(self.allTwelveEffects[i])>1:
                if self.allTwelveEffects[i] not in self.effects:
                    self.effects.append(self.allTwelveEffects[i])

        self.power = len(self.effects)

        self.discovery_score = 0
        for ing in [self.ing_1, self.ing_2, self.ing_3]:
            for i in range(2,9,2):
                if Ingredients[ing][i] in self.effects and int(Ingredients[ing][i+1])==0:
                    self.discovery_score += 1

    def discover(self):
        for ing in [self.ing_1, self.ing_2, self.ing_3]:
            for i in range(2,9,2):
                if Ingredients[ing][i] in self.effects and int(Ingredients[ing][i+1])==0:
                    Ingredients[ing][i+1]=1

    def recipe(self):
        print(Ingredients[self.ing_1][0], " + ", Ingredients[self.ing_2][0], " + ", Ingredients[self.ing_3][0], " = ", self.effects)


    def brew(self):
        working_inventory[self.ing_1] = working_inventory[self.ing_1] - 1
        working_inventory[self.ing_2] = working_inventory[self.ing_2] - 1
        working_inventory[self.ing_3] = working_inventory[self.ing_3] - 1
        self.recipe()


path = './SkyrimAlchemyTrainer.csv'

Ingredients=[]

with open(path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        Ingredients.append(row)

working_inventory=[]
for i in range(len(Ingredients)):
    working_inventory.append(int(Ingredients[i][1]))

print("Ah, so you're an alchemist, then?",'\n')

while (1):
    best_potion = 0
    d_score_to_beat = 0
    for a in range(len(Ingredients)):
        if working_inventory[a]>0:
            for b in range(a+1,len(Ingredients),1):
                if working_inventory[b]>0:
                    for c in range(b+1,len(Ingredients),1):
                        if working_inventory[a]>0 and working_inventory[b]>0 and working_inventory[c]>0:
                            pot=Potion(a,b,c)
                            if pot.discovery_score > d_score_to_beat:
                                d_score_to_beat=pot.discovery_score
                                best_potion=pot
    if d_score_to_beat >0:
        best_potion.brew()
        best_potion.discover()
    else:
        answer = None
        while answer not in ("y", "n"):
            answer = input('\n'+"No more discoverable effects. Continue to brew? (y/n): ")
            if answer not in ["y", "n"]:
                print("invalid input")
        break

while (answer == "y"):
    best_potion = 0
    p_score_to_beat = 0
    for a in range(len(Ingredients)):
        if working_inventory[a]>0:
            for b in range(a+1,len(Ingredients),1):
                if working_inventory[b]>0:
                    for c in range(b+1,len(Ingredients),1):
                        if working_inventory[a]>0 and working_inventory[b]>0 and working_inventory[c]>0:
                            pot=Potion(a,b,c)
                            if pot.power > p_score_to_beat:
                                p_score_to_beat=pot.power
                                best_potion=pot
    if p_score_to_beat >0:
        best_potion.brew()
    else:
        print('\n',"No more viable potions. End of session")
        break

answer = None
while answer not in ("y", "n"):
    answer = input('\n'+"Update save file? (y/n): ")
    if answer == "y":
        for i in range(len(Ingredients)):
            Ingredients[i][1]=working_inventory[i]
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(Ingredients)
        print('\n',"File Updated. Remember to update inventory in CSV before running script again.")
    elif answer == "n":
        print('\n',"Until next time.")
    else:
    	print('\n',"invalid input")