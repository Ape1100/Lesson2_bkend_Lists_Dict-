#Intersection of two Dictionaries

def intersect_dictionaries(dict1, dict2):
    return {k: dict1[k] for k in dict1 if k in dict2}

#Time Complexity: O(n) where n is the number of keys in dict1

#Space Complexity: O(k) where k is the number of common keys