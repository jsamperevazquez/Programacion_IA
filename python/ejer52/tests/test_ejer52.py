from ejer52 import Characters


def test_characters():
    character = Characters("Luke Skywalker", 172, 77, "Blond", "Fair", "Blue", 19, "male", "masculine", "Tatooine",
                           "Human", ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"])
    assert character.name == "Luke Skywalker"
    assert character.height == 172
    assert character.mass == 77
    assert character.hair_color == "Blond"
    assert character.skin_color == "Fair"
    assert character.eye_color == "Blue"
    assert character.birdth_year == 19
    assert character.sex == "male"
    assert character.gender == "masculine"
    assert character.homeworl == "Tatooine"
    assert character.species == "Human"
    assert character.films == ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"]
