class LogisticsSystem:

    def __init__(self):
        self._dict = {'Morning' : 0 ,'Noon' : 0, 'Afternoon' : 0}
    
    def post_or_courier(self , city_code : int):

        if city_code == 1 :
            return 'courier'
        else : 
            return 'post'
    
    def address_check(self , city_code : int , town_code : int , postal_code : str):

        if city_code not in [1,2,3]:
            return False
            
        if town_code not in [1,2]:
            return False 
        
        if len(postal_code) != 10:
            return False
        
        if len(postal_code) == 10:
            return postal_code.isdigit()

        return True
    
    def delivery_time_allocation(self):

        if self._dict['Noon'] < 3 and self._dict['Afternoon'] < 3 :
            print('1.Morning\n2.Noon\n3.Afternoon')
        
        elif self._dict['Noon'] > 2 and self._dict['Afternoon'] < 3 :
            print('1.Morning\n\n3.Afternoon')
        
        elif self._dict['Noon'] < 3 and self._dict['Afternoon'] > 2 :
            print('1.Morning\n2.Noon\n')
        
        elif self._dict['Noon'] > 2 and self._dict['Afternoon'] > 2 :
            print('1.Morning\n\n')

    def update_dict(self , no : int):

        if no == 1:
            self._dict['Morning'] += 1
        
        elif no == 2:
            self._dict['Noon'] += 1    

        elif no == 3:        
            self._dict['Afternoon'] += 1
    
    def _time(self , no:int):
        
        if no == 1:
            return 'Morning'
        
        elif no == 2:
            return 'Noon'
        
        elif no == 3:
            return 'Afternoon'