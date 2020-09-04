def step_known(n_min, n_max, step):
    print('-'*25+'step_known():')

    n_max += 1

    for i in range(n_min, n_max, step):
    
        print('\t',i)

def step_unknown(n_min, n_max, rows):
    print('-'*25+'step_unknown():')

    n_max = 900000
    n_min = 450000
    rows = 10

    step = (n_max - n_min) // (rows - 1)
    
    # Loop 'rows' times to print the rows in the table:
    for i in range(rows):
        n = n_min + i * step  # calculate the value of 'n' for row 'i'
        print('\t',n)

step_known(450000, 900000, 50000)
step_unknown(450000, 900000, 10)