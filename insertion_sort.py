def insertion_sort(inputlist1):
    for i in range(1, len(inputlist1)):
        j = i-1
        nxt_element = inputlist1[i]
        while (inputlist1[j] > nxt_element) and (j >= 0):
            inputlist1[j + 1] = inputlist1[j]
            j = j-1
        inputlist1[j + 1] = nxt_element


lists = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(lists)
print(lists)
