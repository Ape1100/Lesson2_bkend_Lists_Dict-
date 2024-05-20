##Task Two Reverse a Sublist 

def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

#Time Complexity: O(j-i+1) for splicing and reverseing the sublist

#Space Complexity:O(j-1+1) for the temporary reversed sublist
