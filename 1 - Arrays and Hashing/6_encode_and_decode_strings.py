def encode(strs):
    if not strs:
        return ""
    size_list = []
    string = ""
    
    # Get sizes of string in strs list
    for element in strs:
        size_list.append(len(element))
        
    # Store the sizes at the start of string seperated by ,    
    for size in size_list:
        string += str(size)
        string += ","
        
    # Seperate the encoded message from sizes
    string += "#"
    
    # Add the encoded message to the string
    for s in strs:
        string += s
        
    return string

'''
Time Complexity: O(n), processes each character once.
Space Complexity: O(n), stores all characters plus metadata.
'''
    
def decode(s):
    if not s:
        return []
    
    sizes = []
    response = []
    start = 0
    temp_str = "" 
    
    # Populate the sizes array and sets the start var to the index where the string we need to decode starts
    for i in range(len(s)):
        if s[i] == "#":
            start = i + 1
            break
        
        # Useing temp_str for the occurance of numbers > 10
        if s[i] == ",":
            sizes.append(int(temp_str))
            temp_str = ""
        else:
            temp_str += s[i]
        
    # Slices the string based on the sizes array
    for size in sizes:
        print(sizes)
        response.append(s[start: start+size])
        start += size
            
    return response

'''
Time Complexity: O(n), iterates through s once for parsing and slicing.
Space Complexity: O(n), stores decoded strings matching input length.
'''