# pokemon v.01.6

def add_data(pokemon):
    pokemon.append(None)
    pLen = len(pokemon)
    pokemon[pLen - 1] = pokemon


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("OUT OF SPACE!")
        return

    pokemons.append(None)
    kLen = len(pokemons)

    for i in range(kLen - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 배열의 제일 뒤에 친구 추가


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("OUT OF SPACE!")
        return

    pLen = len(pokemons)
    pokemons[idx] = None  # data del

    for i in range(idx + 1, pLen):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 제일 위치 삭제

    del (pokemons[pLen - 1])


## list making ##
pokemons = []
menu = -1  # 1: Add, 2: Call, 3: Delete, 4: Exit

## main section ##
if __name__ == "__main__":

    while True:

        menu = int(input("Please select(1: Add, 2: Call, 3: Delete, 4: Exit)--> "))

        if (menu == '1'):
            data = input("Add pokemon name--> ")
            add_data(data)
            print(pokemons)
        elif (menu == '2'):
            pos = int(input("Where to add--> "))
            data = input("Additional data--> ")
            insert_data(pos, data)
            print(pokemons)
        elif (menu == '3'):
            pos = int(input("Which pokemon do you want to delete--> "))
            delete_data(pos)
            print(pokemons)
        elif (menu == '4'):
            print(pokemons)
            exit()
        else:
            print("Please enter a number between 1-4.")
            continue
