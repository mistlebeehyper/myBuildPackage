def top_n(items, n):
    """Returns top 10 items in an array, in desc order

    Args:
        items (Array): List or array like object
        n (int): number of items to return
        
    Eg:
        top_n([8,54,4,4,34,3], 3)
        [8.54.4]
    """
    
    for i in range(n): #sorting till we have the top n items