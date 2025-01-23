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
    
def decode(s):
    if not s:
        return ""
    
    sizes = []
    response = []
    start = 0
    
    for i in range(len(s)): 
        if s[i] == "#":
            start = i + 1
            break
        
        if s[i] == ",":
            pass
        else:
            sizes.append(int(s[i]))
        
        
    for size in sizes:
        response.append(s[start: start+size])
        start += size
            
    return response
        

print(decode(encode(["neet","code","love","you"])))