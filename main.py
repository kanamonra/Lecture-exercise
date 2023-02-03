# pokemon v.01.3


pokemons = ["Pikachu", "Eevee", "Dragonite", "Krogre", "Palkia"]


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of range")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon


def del_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pLen = len(pokemons)
    pokemons[idx] = None  # del data
    for i in range(idx +1 , pLen):
        pokemons[i] = None
    for i in range(idx, 7):
        # pokemons[i + 1] = pokemons[i]
        pokemons.pop()

    temp = pokemons[:idx]

    # del pokemons[i]

    # del (pokemons[pLen - 1])


if __name__ == "__main__":
    insert_data(2, 'Eevee')  # instead, there is an way of class.insert to add data
    # pokmons.insert(2, 'Eevee')   => for example

    print(pokemons)
    insert_data(6, 'Star')
    print(pokemons)

    # deleting data
    del_data(1)
    print(pokemons)

# pokemons = list()  # Empty array


# def add_data(pokemon):
#    pokemons.append(None)
#    # lenPokemons = len(pokemons) // other way to make lenght of array
#    pokemons[-1] = pokemon


# add_data('Pikachu')
# add_data('Eevee')
# add_data('Dragonite')
# add_data('Krogre')
# add_data('Palkia')
# 
# print(pokemons)
