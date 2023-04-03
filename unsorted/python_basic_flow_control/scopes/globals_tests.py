global_var = 100


def do_assign_local():
    global_var = 200
    print(f"do_assign_local() scope: {global_var}")

def do_assign_global():
    global global_var
    global_var = 300
    print(f"do_assign_global() scope: {global_var}")

def do_update():
    global global_var
    global_var = global_var + 400

    print(f"do_update() scope: {global_var}")


print(f"Global scope: {global_var}")
do_assign_local()
print(f"Global scope: {global_var}")
do_assign_global()
print(f"Global scope: {global_var}")
do_update()
print(f"Global scope: {global_var}")
