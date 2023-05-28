
def calculate(name, seeds):
    '''(str, int) -> int, str

    This code takes the name of a vegetable from SoS: FoMT and the quantity of seeds you'll use,
    and returns it's total profit at the end of the season, the season on which it grows and if it regrows or not.

    >>> calculate('Tomato', 1)
    3760 Summer Regrow
    >>> calc('Potato', 1)
    2280 Spring No regrow
    '''
    
    vegetables = [['Turnip', 4, 0, 120, 60], [ 'Potato', 7, 0, 150, 80], ['Cucumber', 9, 5, 200, 60], ['Strawberries', 9, 3, 15, 65], ['Cabbage', 14, 0 , 500, 250], ['Moon Drop Flower', 6, 0, 500, 10], ['Toy Flower', 12, 0, 400, 10],
             ['Tomato', 9, 3, 200, 55], ['Corn', 14, 3, 300, 85], ['Onion', 7, 0, 150, 80], ['Pumpkin', 14, 0, 500, 280], ['Pinapple', 20, 5, 1000, 500], ['Pink Cat Flower', 6, 0, 300, 10],
              ['Eggplant', 9, 3, 120, 60], ['Yam', 6, 3, 300, 55], ['Carrot', 7, 0, 300, 120], ['Spinach', 5, 0, 200, 110], ['Green Pepper', 7, 2, 150, 40], ['Adzuki Beans', 10, 4, 300, 80], ['Chili Peppers', 12, 5, 300, 100], ['Blue Magic Red Flower', 10, 0, 600, 10], ['True Magic Red Flower', 10, 0, 600, 200], ['Sunset Flowe', 10, 0, 1000, 10]]
    

    grow_time = 0
    regrow_time = 0
    seed_price = 0
    selling_price = 0
    seed_name = ''
    regrow = 'No regrow'
    season = ''
    test = 0
    p = -1


    for i in range(len(vegetables)):
        if name in vegetables[i]:
            p = i

    if p >= 0:
        seed_name = vegetables[p][0]
        grow_time  = vegetables[p][1]
        regrow_time = vegetables[p][2]
        seed_price = vegetables[p][3]
        selling_price = vegetables[p][4]
    else:
        return 'Wrong vegetable'
    
    if regrow_time > 0:
        regrow = 'Regrow'
        production = ((30 - grow_time) // regrow_time) + 1
        profit = (((seeds * 9) * production)* selling_price) - (seed_price * seeds)
    else:
        production = 30 // grow_time
        profit = (((seeds * 9) * production)* selling_price) - ((seed_price * seeds) * production)
        

    if p <= 6:
        season = 'Spring'
    elif 7 >= p < 13:
        season = 'Summer'
    else:
        season = 'Fall'
        
    
    
    

    return print(profit, season, regrow)

 

