def insertion_sort(inputlists):
    for i in range(1, len(inputlists)):
        j = i-1
        nxt_element = inputlists[i]
        while (inputlists[j] > nxt_element) and (j >= 0):
            inputlists[j + 1] = inputlists[j]
            j = j-1
        inputlists[j + 1] = nxt_element


lists = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(lists)
print(lists)
