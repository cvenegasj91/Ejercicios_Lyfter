def bubble_sort(list_to_sort):
    #worst case es O(n^2) por que itera la lista n cantidad de veces hasta que la lista quede ordenada
    #entonces el loop interno deja de hacer cambios y made_changes queda en False rompiendo el ciclo
    #En el caso de que la lista este ordenada made_changes es False entonces la funcion es O(n) ya que la iteracion del loop interno se recorre una sola vez sin hacer cambios
    for outer_i in range(0, len(list_to_sort)-1):

        made_changes = False #O(1)

        for i in range(0, len(list_to_sort)-1-outer_i):
            current_item = list_to_sort[i]
            next_item = list_to_sort[i+1]
            
            if current_item > next_item:
                list_to_sort[i] = next_item 
                list_to_sort[i+1] = current_item 
                made_changes = True 

        if not made_changes:
            return


testing_list = [3, 2, 10, 7, 5, 9]
bubble_sort(testing_list)
print(testing_list) 