def bubble_sort(list_to_sort):

    for outer_i in range(0, len(list_to_sort)-1): #O(n)

        made_changes = False #O(1)

        for i in range(0, len(list_to_sort)-1-outer_i): #O(n^2)
            current_item = list_to_sort[i] #O(1)
            next_item = list_to_sort[i+1] #O(1)
            
            if current_item > next_item: #O(1)
                list_to_sort[i] = next_item #O(1)
                list_to_sort[i+1] = current_item #O(1)
                made_changes = True #O(1)

        if not made_changes: #O(1)
            return


testing_list = [3, 2, 10, 7, 5, 9]
bubble_sort(testing_list) #O(n^2)
print(testing_list) #O(n)