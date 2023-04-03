test = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'

i_idx = 0
while (i_idx := test.find('i', i_idx+1)) > 0:
    print(i_idx)

