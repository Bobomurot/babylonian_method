S = int(input())
d = int(input())

def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    a = (S - (d**2))/(2*d)
    b = a +d
    x = b - (a**2)/(2*b)
    return x

result = main(S, d)
print(result)