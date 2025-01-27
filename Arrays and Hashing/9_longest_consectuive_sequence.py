def longestConsecutive(nums):
    seqs = []
    curr_seq = 0
    nums.sort()
    for num in nums:
        if len(seqs) == 0:
            seqs.append([num])
        
        if seqs[curr_seq][-1] == num:
            pass
        elif seqs[curr_seq][-1]+1 == num:
            seqs[curr_seq].append(num)
        else:
            seqs.append([num])
            curr_seq += 1
        
    curr_max = 0
    for seq in seqs:
        if len(seq) > curr_max:
            curr_max = len(seq)
    
    return curr_max
    
nums = [0,3,2,5,4,6,1,1]

print(longestConsecutive(nums))