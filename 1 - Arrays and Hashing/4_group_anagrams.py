def groupAnagrams(strs):
    my_dict = {}

    for string in strs:
        # Sort the string to create a key that represents its anagram group
        sorted_key = ''.join(sorted(string))

        # If the sorted key is already in the dictionary, append the string
        if sorted_key in my_dict:
            my_dict[sorted_key].append(string)
        else:
            # Otherwise, create a new entry in the dictionary
            my_dict[sorted_key] = [string]

    # Prepare the output list to return the grouped anagrams
    out = []
    for key in my_dict:
        out.append(my_dict[key])

    return out

'''
Time Complexity: O(n * k log k), where n is the number of strings in strs
and k is the maximum length of a string. This is due to sorting each string.
Space Complexity: O(n * k), where n is the number of strings and k is the
maximum length of a string, for storing the grouped anagrams in the dictionary.
'''