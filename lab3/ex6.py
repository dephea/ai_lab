orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter(lambda a: True if a % 2 == 0 else False, orig_list)
odd_list = filter(lambda a: True if a % 2 != 0 else False, orig_list)

print("even list:", list(even_list))
print("odd list:", list(odd_list))