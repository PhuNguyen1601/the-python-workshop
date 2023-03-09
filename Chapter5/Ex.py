 ## Ex 72 - creating a Pet class
 
class Pet:
    """
    A class to capture useful information regarding my pets, just in case
    I lose track of them.
    """
    def __init__(self,height):
        self.height = height
        
        
    is_human = False
    owner = 'Michael Smith'
    
    
cat1 = Pet(height=10)

print(cat1.height)
