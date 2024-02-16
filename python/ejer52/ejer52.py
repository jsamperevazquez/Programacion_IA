import csv
from typing import Union


def show_character(character: list):
    for c in character:
        print(c)


class Characters:

    def __init__(self, name: str, height: Union[int, str], mass: Union[float, str], hair_color: any, skin_color: any,
                 eye_color: any, birdth_year: any, sex: any, gender: str, homeworl: any,
                 species: any, films: list[str]):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birdth_year = birdth_year
        self.sex = sex
        self.gender = gender
        self.homeworl = homeworl
        self.species = species
        self.films = films

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Height: {self.height}\n"
            f"Mass: {self.mass}\n"
            f"Hair Color: {self.hair_color}\n"
            f"Skin Color: {self.skin_color}\n"
            f"Eye Color: {self.eye_color}\n"
            f"Birdth Year: {self.birdth_year}\n"
            f"Sex: {self.sex}\n"
            f"Gender: {self.gender}\n"
            f"Homeworl: {self.homeworl}\n"
            f"Species: {self.species}\n"
            f"Films: {', '.join(self.films)}\n"
        )


class Human(Characters):
    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birdth_year, sex, gender, homeworl,
                 species, films):
        super().__init__(name, height, mass, hair_color, skin_color, eye_color, birdth_year, sex, gender, homeworl,
                         species, films)

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Height: {self.height}\n"
            f"Mass: {self.mass}\n"
            f"Hair Color: {self.hair_color}\n"
            f"Skin Color: {self.skin_color}\n"
            f"Eye Color: {self.eye_color}\n"
            f"Birdth Year: {self.birdth_year}\n"
            f"Sex: {self.sex}\n"
            f"Gender: {self.gender}\n"
            f"Homeworl: {self.homeworl}\n"
            f"Species: {self.species}\n"
            f"Films: {', '.join(self.films)}\n"
        )


class Droid(Characters):
    def __init__(self, name, height, mass, birdth_year, gender, homeworl, films):
        super().__init__(name, height, mass, None, None, None, birdth_year, None, gender, homeworl,
                         None, films)
        self.name = name,
        self.height = height,
        self.mass = mass,
        self.birdth_year = birdth_year,
        self.gender = gender,
        self.homeworl = homeworl,
        self.films = films

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Height: {self.height}\n"
            f"Mass: {self.mass}\n"
            f"Birdth Year: {self.birdth_year}\n"
            f"Gender: {self.gender}\n"
            f"Homeworl: {self.homeworl}\n"
            f"Films: {', '.join(self.films)}\n"
        )


class Factory:
    characters = []
    droids = []
    humans = []
    first = True
    with open("starwars.csv", newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        # Evito la primera fila del csv que son las cabeceras
        for row in reader:
            if first:
                first = False
                continue
            # Creo los personajes pasando como parámetros los valores de las columnas de cada fila
            characters.append(
                Characters(row[0], int(row[1]) if row[1] != "NA" else str(row[1]),
                           float(row[2]) if row[2] != "NA" else str(row[2]), row[3], row[4], row[5], row[6],
                           row[7], row[8], row[9], row[10], row[11::]))
        for character in characters:
            if character.species == "Droid":
                droids.append(
                    Droid(character.name, character.height, character.mass, character.birdth_year, character.gender,
                          character.homeworl, character.films))
            elif character.species == "Human":
                humans.append(
                    Human(character.name, character.height, character.mass, character.hair_color,
                          character.skin_color, character.eye_color, character.birdth_year, character.sex,
                          character.gender, character.homeworl, character.species, character.films))
    # Imprimo todos los personajes
    show_character(characters)
    # Imprimo solamente los no droides
    show_character(humans)


if __name__ == '__main__':
    factory_characters = Factory()
