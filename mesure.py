
class Mesure :

    def __init__(self, str_Sensor, str_Type_mesure, str_Unite, f_Threshold_min, f_Threshold_max):
        self.str_Sensor = str_Sensor
        self.str_Type_mesure = str_Type_mesure
        self.f_Value = None
        self.str_Unite = str_Unite
        self.f_Threshold_min = f_Threshold_min
        self.f_Threshold_max = f_Threshold_max



    def threshold_check(self) :
        if self.f_Value > self.f_Threshold_max or self.f_Value < self.f_Threshold_min :
                print(f'Alerte : {self.str_Type_mesure} hors limites !    |    Mesure : {self.f_Value}, Min : {self.f_Threshold_min}, Max : {self.f_Threshold_max}')

