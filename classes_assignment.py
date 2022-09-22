class Sports: #Class Sports created with 4 attributes
    name = 'American Football'
    country = 'USA'
    type_of_ball = 'sphere'
    violence_level ='high'

class Players(Sports): #Class Players inherists from sports and adds Players to the class with its own attributes
    base_pay = '$900,000'
    competiteveness = 'high'


class Coaches(Sports): #Class Coaches inherists from sports and adds Players to the class with its own attributes
    Firing_Frequency = 'high'
    Diversity = 'very low'


