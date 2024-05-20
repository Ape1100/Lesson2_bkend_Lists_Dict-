##Task Three merge Two sorted lists

def merge_sorted_lists(lst1, lst2):
    i, j = 0, 0
    merged_list = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    return merged_list

#Time complexity: O(n+m) where n and m are the lengths of Lst1 and Lst2

#Space complexity: O(n+m) for the merged list.