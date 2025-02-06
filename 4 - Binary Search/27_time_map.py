class TimeMap:
    def __init__(self):
        self.timeMap = {}  # Dictionary to store key -> list of (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:    
            self.timeMap[key] = []  # Initialize list for key
        self.timeMap[key].append((timestamp, value))  # Store (timestamp, value)
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""  # Key not found

        values = self.timeMap[key]
        l, r = 0, len(values) - 1
        res = ""  # Default to empty string if no valid timestamp found
        
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]  # Store the closest valid value
                l = m + 1  # Move right to find larger valid timestamps
            else:
                r = m - 1  # Move left to find a smaller timestamp
        
        return res  # Return the last valid value found

# Time Complexity:
# - `set()`: O(1) (appends to a list)
# - `get()`: O(log n) (binary search)

# Space Complexity: O(n) (stores all key-value pairs)
