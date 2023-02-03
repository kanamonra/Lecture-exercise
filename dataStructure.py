# example 115p 응용예제
# 카톡 친구 자동 삽입하기

# find and add def section
def find_add_insert_data(friend, k_count):
    """
    Finding itself space and adding an new data in kakaot friends list
    :param friend: person name
    :param k_count: number of contacts
    :return: list of friends contact and number
    """
    findPos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            findPos = i
            break
    if findPos == -1:
        findPos = len(katok)

    insert_data(findPos, (friend, k_count))

def insert_data(position, name):
    if position < 0 or position > len(katok):
        print('Out of space')
        return
    katok.append(None)
    klen = len(katok)
    for i in range(klen - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i -1] = None

    katok[position] = name

# making tuple list for name and number of contact
katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
# main section
if __name__ == "__main__":

    while True:
        data = input('추가할 친구 -->')
        count = int(input('연락처 입력-->'))
        find_add_insert_data(data, count)
        print(katok)