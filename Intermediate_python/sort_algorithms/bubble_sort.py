def bubble_sort(list_to_sort):

    for outer_i in range(0, len(list_to_sort)-1):

        made_changes = False

        for i in range(0, len(list_to_sort)-1-outer_i):
            current_item = list_to_sort[i]
            next_item = list_to_sort[i+1]
            
            if current_item > next_item:
                list_to_sort[i] = next_item
                list_to_sort[i+1] = current_item
                made_changes = True

        if not made_changes:
            return