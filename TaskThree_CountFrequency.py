#Task 3 Count Frequencty of Words

def count_word_frequencies(word_list):
    frequency = {}
    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

#Time Complexity: O(n) where n is the number of words in the list

#Space Complexity: O(m) where m is the number ofd unique words