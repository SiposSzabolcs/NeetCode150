def longestConsecutive(nums):
    seqs = []
    curr_seq = 0

    nums.sort()

    for num in nums:
        # Initialize the first sequence if none exist yet
        if len(seqs) == 0:
            seqs.append([num])

        # Skip duplicates, as they do not contribute to the sequence length
        if seqs[curr_seq][-1] == num:
            pass
        # Extend the current sequence for consecutive numbers
        elif seqs[curr_seq][-1] + 1 == num:
            seqs[curr_seq].append(num)
        # Start a new sequence when numbers are not consecutive
        else:
            seqs.append([num])
            curr_seq += 1

    # Find the length of the longest sequence
    curr_max = 0
    for seq in seqs:
        if len(seq) > curr_max:
            curr_max = len(seq)

    return curr_max

# Space Complexity: O(n) - The `seqs` list can grow to contain all numbers in the input array in the worst case.
# Time Complexity: O(n log n) - Sorting the array takes O(n log n), and processing it in a single pass takes O(n).
