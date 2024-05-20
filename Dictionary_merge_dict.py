#Task 1 Merge two dictionarys 

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


#Time Complexity: O(n) where n is the number of keys in dict2

#Space Complexity: O(n+M) where n and m are the sizes of dict1 and dict2, respectfully