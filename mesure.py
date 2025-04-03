class Mesure :
    # Liste statique d'alarmes
    current_alarms = []

    def __init__(self, str_Sensor, str_Type_mesure, str_Unite, f_Threshold_min, f_Threshold_max):
        self.str_Sensor = str_Sensor
        self.str_Type_mesure = str_Type_mesure
        self.f_Value = None
        self.str_Unite = str_Unite
        self.f_Threshold_min = f_Threshold_min
        self.f_Threshold_max = f_Threshold_max

    def threshold_check(self, led_alarme=None) :
        if self.f_Value > self.f_Threshold_max or self.f_Value < self.f_Threshold_min :
            if led_alarme :
                led_alarme.Led_On()
            alarm_message = f'⚠ Alerte : {self.str_Type_mesure} hors limites ! | Min : {self.f_Threshold_min}, Max : {self.f_Threshold_max}'
            print(alarm_message)
            if alarm_message not in Mesure.current_alarms:
                Mesure.current_alarms.append(alarm_message)
        else:
            if led_alarme :
                led_alarme.Led_Off()
            # Supression de l'alarme si la valeur est dans les limites
            Mesure.current_alarms = [alarm for alarm in Mesure.current_alarms 
                                   if self.str_Type_mesure not in alarm]

