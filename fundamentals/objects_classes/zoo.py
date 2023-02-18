class Zoo:
    __animals: int = 0

    def __init__(self, input_name: str) -> None:
        self.name: str = input_name
        self.mammals: list = []
        self.fishes: list = []
        self.birds: list = []

    def add_animal(self, species_list: str, animal_to_add: str):
        if species_list == "mammal":
            self.mammals.append(animal_to_add)
        elif species_list == "fish":
            self.fishes.append(animal_to_add)
        else:
            self.birds.append(animal_to_add)
        Zoo.__animals += 1

    def get_info(self, species: str):
        result: str = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        else:
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
num_animals = int(input())

zoo = Zoo(zoo_name)

for i in range(num_animals):
    species, animal = input().split(" ")
    zoo.add_animal(species, animal)

species_to_print = input()
print(zoo.get_info(species_to_print))

# def zoo(input_name: str):
#     animals: int = 0
#     name: str = input_name
#     mammals: list = []
#     fishes: list = []
#     birds: list = []

#     def add_animal(species_list: str, animal_to_add: str):
#         nonlocal animals
#         if species_list == "mammal":
#             mammals.append(animal_to_add)
#         elif species_list == "fish":
#             fishes.append(animal_to_add)
#         else:
#             birds.append(animal_to_add)
#         animals += 1

#     def get_info(species: str):
#         nonlocal name, mammals, fishes, birds, animals
#         result: str = ""
#         if species == "mammal":
#             result += f"Mammals in {name}: {', '.join(mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {name}: {', '.join(fishes)}\n"
#         else:
#             result += f"Birds in {name}: {', '.join(birds)}\n"
#         result += f"Total animals: {animals}"
#         return result

#     return add_animal, get_info


# zoo_name = input()
# num_animals = int(input())

# add_animal, get_info = zoo(zoo_name)

# for i in range(num_animals):
#     species, animal = input().split(" ")
#     add_animal(species, animal)

# species_to_print = input()
# print(get_info(species_to_print))
