# pokemon v.01.2


pokemons = ["Pikachu", "Eevee", "Dragonite", "Krogre", "Palkia"]


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of range")
        return

    pokemons.append(None)  # 빈칸 추가
    pLen = len(pokemons)  # 배열의 현재 크기

    for i in range(pLen - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


insert_data(2, 'Palkia')
print(pokemons)
insert_data(6, 'Eevee')
print(pokemons)

# pokemons = list()  # Empty array


#def add_data(pokemon):
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
