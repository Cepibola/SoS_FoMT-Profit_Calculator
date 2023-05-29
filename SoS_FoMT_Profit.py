def calculate(name, seeds):
    '''(str, int) -> int, str

    This code takes the name of a vegetable from SoS: FoMT and the quantity of seeds you'll use,
    searches for that vegetable in a data base and retiurns it's total profit at the end of
    the season, the season on which it grows and if it regrows or not.

    >>> calculate('Tomato', 1)
    3760 Summer Regrow
    >>> calc('Potato', 1)
    2280 Spring No regrow
    '''
    

    grow_time = 0
    regrow_time = 0
    seed_price = 0
    selling_price = 0
    seed_name = ''
    regrow = 'No regrow'
    season = ''
    test = 0
    p = ''


    lists = open('data.txt', 'r')

    for line in lists:
        veggie = line[0:21].strip()
        if veggie == name:
            p = line

    if p != '':
        seed_name = p[0:21].strip()
        grow_time  = int(p[22:24])
        regrow_time = int(p[25:26])
        seed_price = int(p[27:31])
        selling_price = int(p[32:35])
    else:
        return 'Wrong vegetable'
    
    if regrow_time > 0:
        regrow = 'Regrow'
        production = ((30 - grow_time) // regrow_time) + 1
        profit = (((seeds * 9) * production)* selling_price) - (seed_price * seeds)
    else:
        production = 30 // grow_time
        profit = (((seeds * 9) * production)* selling_price) - ((seed_price * seeds) * production)
        
    if p[36] == '1':
        season = 'Spring'
    elif p[36] == '2':
        season = 'Summer'
    else:
        season = 'Fall'
       
        
    

    return print(profit, season, regrow)
