arr = ["apple", "banana", "orange", "pear", "kiwi", "mango"]
new_arr = [s for s in arr if len(s) < 7]
print(new_arr)