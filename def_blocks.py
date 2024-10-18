global_var = 1

def my_var():
        print('Global variable:', global_var)

        local_var=2
        print('Local var', local_var)


        global inner_var
        inner_var=3
my_var()
print("Second Global:", inner_var)

