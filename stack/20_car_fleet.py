def carFleet(target,position,speed):
    combined = sorted(zip(position, speed), reverse=True)  # Sort by position descending
    stack = []  # This will track fleets

    for pos, spd in combined:
        arrival_time = (target - pos) / spd  # Calculate time to reach target

        # If stack is empty or the new car takes longer than the last fleet, it's a new fleet
        if not stack or arrival_time > stack[-1]:
            stack.append(arrival_time)  # Push fleet arrival time

    return len(stack)  # Number of separate fleets

# Time Complexity: O(n log n), due to sorting the cars by position.
# Space Complexity: O(n), for storing the stack in the worst case.