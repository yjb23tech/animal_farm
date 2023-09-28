from classes import Human, Bird 

test_Human = Human("Homo Sapien", "Yuri Orlov", "Cosmopolitan City")
test_Bird = Bird("Black Tern", "Gbenga Adewale", "Grand Canyon")

print(test_Human)
print(test_Bird)

#Code above worked; class Human and Bird were able to inherit the __str__ method from class Organism 
#I can abstract both __init__(self, params) and __str__(self) into the parent class away from the children class(es)

print(test_Human.human_sounds)
print(test_Bird.bird_sounds)