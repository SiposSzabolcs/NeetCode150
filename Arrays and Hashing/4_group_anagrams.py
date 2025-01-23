def groupAnagrams(strs):
    my_dict = {}

    for string in strs:
        sorted_key = ''.join(sorted(string))

        if sorted_key in my_dict:
            my_dict[sorted_key].append(string)
        else:
            my_dict[sorted_key] = [string]

    out = []
    for key in my_dict:
        out.append(my_dict[key])

    return out
        
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))