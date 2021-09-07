i = 0

def move(place) :
    
    if i == 0 :
        
        datas1 = place
        
    else :
        
        datas2 = place
        ram[(datas1)] = ram[(datas2)]
