class Organism:

    def __init__(self, str_species, str_name, str_habitat):
        self.species = str_species
        self.name = str_name
        self.habitat = str_habitat

    def __str__(self):
        return (f"Species: {self.species} Name: {self.name} Habitat: {self.habitat}")

class Human(Organism):

    human_sounds = "Hello New World"

class Bird(Organism):

    bird_sounds = "Squawk Squawk"



