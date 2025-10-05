

def get_word_count(text):
    return len(text.split())


def get_char_count(text):

    character_counts = {}

    for char in text.lower():

        if char in character_counts:
            character_counts[char] +=1
        else:
            character_counts[char] = 1

    return character_counts


def get_sorted_list(character_counts: dict):
    sorted_list= []

    for key, value in character_counts.items():
        sorted_list.append({"char": key, "num": value})

    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)


    return sorted_list
    