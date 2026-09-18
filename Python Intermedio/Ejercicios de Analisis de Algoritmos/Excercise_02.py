def print_numbers_times_2(numbers_list): 
	#Esta funcion es 2(n) ya que recorre number_list n cantidad de veces
	for number in numbers_list: 
		print(number * 2) 


def check_if_lists_have_an_equal(list_a, list_b):
	#En el worst case si n != m la funcion es O(n.m) si n=m podemos decir que es O(n^2)
	#Ademas si el primer elemento de ambas listas son iguales la funcion es O(1)
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False


def print_10_or_less_elements(list_to_print):
	#Aunque la lista tenga un tamaño de 10,000 iteraciones "for" solo hace 10 iteraciones como maximo por lo que el worst case de la funcion es O(1)
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])


def generate_list_trios(list_a, list_b, list_c):
	#Worst case: listas con diferentes tamaños la funcion seria O(n.m.p) si las 3 listas son de igual cantidad de iteraciones se puede decir que es O(n^3)
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list