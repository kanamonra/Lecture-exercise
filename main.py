# pokemon
pokemons = list()  # Empty array


def add_data(pokemon):
    pokemons.append(None)
    # lenPokemons = len(pokemons) // other way to make lenght of array
    pokemons[-1] = pokemon


add_data('Pikachu')
add_data('Eevee')
add_data('Dragonite')
add_data('Krogre')
add_data('Palkia')

print(pokemons)
