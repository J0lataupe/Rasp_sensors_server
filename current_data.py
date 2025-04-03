import Adafruit_DHT

from database_ctrl import ajouter_mesure
from mesure import Mesure

class CurrentData :

    def __init__(self):
        self.obj_Humidity = Mesure("DHT11", "Humidité", "%", 0, 75)
        self.obj_Temperature = Mesure("DHT11", "Température", "°C", 0, 25)
        self.list_Mesures = [self.obj_Humidity, self.obj_Temperature]




    def acquisition_data(self) :

        # Declaration Capteur
        obj_Sensor_T_H = Adafruit_DHT.DHT11


        # Declaration pin
        i_Pin_T_H = 4


        # Mappage
        self.obj_Humidity.f_Value, self.obj_Temperature.f_Value = Adafruit_DHT.read_retry(obj_Sensor_T_H, i_Pin_T_H)

        # Actualisation Database
        for obj_Mesure in self.list_Mesures :
            if obj_Mesure is not None :
                ajouter_mesure(obj_Mesure.str_Sensor, obj_Mesure.str_Type_mesure, obj_Mesure.f_Value, obj_Mesure.str_Unite)
            else :
                print ('Echec de lecture de {str}%`').format(obj_Mesure.str_Type_mesure)


