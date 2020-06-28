
loops = 10

def hypotenuse(x):
    return round(round(x[0]**2 + x[1]**2, 2)**(1/2), 2)

def heavy_computation(x):
    for i in range(loops):
        output = hypotenuse(x)
        
    return output