def bubble_sort(list_to_sort):

    for outer_i in range(0, len(list_to_sort)-1):

        made_changes = False

        for i in range(len(list_to_sort)-1, outer_i, -1):
            current_item = list_to_sort[i]
            previous_item = list_to_sort[i-1]

            print(f"Iteracion: {outer_i}, {i}, Item Anterior: {previous_item}, Item Actual: {current_item}")
            
            if current_item < previous_item:
                print("Item Actual es menor al anterior, intercambiando...")
                list_to_sort[i] = previous_item
                list_to_sort[i-1] = current_item
                made_changes = True

        if not made_changes:
            return


testing_list = [3, 2, 10, 7, 5, 9]
bubble_sort(testing_list)
print(testing_list)