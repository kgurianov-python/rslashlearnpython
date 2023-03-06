import ast

s = "['3306', '3014', '3359', '3792', '3508', '3546', '3201']"
# As simple strip + split
the_list_stripped = s.strip('][').split(', ')

# double strip
the_list_double_stripped = [item.strip('\'') for item in the_list_stripped]

# use ast.literal_eval()
the_list_from_eval = ast.literal_eval(s)

print(f'Initial string: {type(s)} {s}\n')
print(f'the_list_stripped {type(the_list_stripped)}: {the_list_stripped}\n')
print(f'the_list_double_stripped: {type(the_list_double_stripped)}: {the_list_double_stripped}\n')
print(f'the_list_double_stripped[0]: {type(the_list_double_stripped[0])}: {the_list_double_stripped[0]}\n')
print(f'the_list_from_eval: {type(the_list_from_eval)}: {the_list_from_eval}\n')
print(f'the_list_from_eval[0]: {type(the_list_from_eval[0])}: {the_list_from_eval[0]}\n')
