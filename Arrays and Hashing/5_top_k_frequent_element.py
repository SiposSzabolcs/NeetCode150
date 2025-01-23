def topKFrequent(nums, k):
    my_dict = {}
    
    # Count the frequency of each element in nums
    for element in nums:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
    
    out = []
    
    # Find the k most frequent elements
    for i in range(k):
        most_freq = 0
        max_freq = 0
        
        # Iterate through the dictionary to find the most frequent element
        for element in my_dict:
            if my_dict[element] > max_freq:
                most_freq = element
                max_freq = my_dict[element]
        
        # Append the most frequent element to the output list
        # Remove the element from the dictionary to avoid counting it again
        out.append(most_freq)
        del my_dict[most_freq]
        
    return out

'''
Time Complexity: O(n * k), where n is the number of elements in nums.
This is because for each of the k elements, we may need to scan the entire
dictionary to find the most frequent element.
Space Complexity: O(n), for storing the frequency count in my_dict.
'''

def topKFrequentBetter(nums, k):
    count = {}
    
    # Create a list of empty lists to hold elements by their frequency
    freq = [[] for i in range(len(nums) + 1)]
    
    # Count the frequency of each element in nums
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    # Populate the freq list with elements based on their frequency
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    
    # Collect the k most frequent elements from the freq list
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

'''
Time Complexity: O(n), where n is the number of elements in nums.
This is because we traverse the list to count frequencies and then
traverse the frequency list to collect the top k elements.
Space Complexity: O(n), for storing the frequency count in the count
dictionary and the freq list.
'''