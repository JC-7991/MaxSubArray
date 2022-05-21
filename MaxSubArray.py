def max_sequence(arr):

    curr = 0
    max = 0
    
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max:
            max = curr
            
    return max