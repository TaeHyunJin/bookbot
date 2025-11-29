def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def get_char_count(file_contents):
    char_count = {}
    for c in file_contents:
        if c.lower() not in char_count:
            char_count[c.lower()] = 1
        else:
            char_count[c.lower()] += 1
    return char_count

def sorted_list(char_dict):
    def helper(sorted_list):
        return sorted_list["num"]

    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char":key, "num":char_dict[key]})
    sorted_list.sort(reverse=True, key=helper)
    return sorted_list 
