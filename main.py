import time
import threading
from flask import Flask, request
import requests

from output import Output
from current_data import CurrentData
from app import *


obj_Current_data = CurrentData()
LedAlarme = Output(17)


def main_loop(x_Stop_event):
    while not x_Stop_event.is_set() :
        obj_Current_data.acquisition_data()

        for obj_Mesure in obj_Current_data.list_Mesures :
            obj_Mesure.threshold_check(LedAlarme)

        time.sleep(5)



def listen_for_input(x_Stop_event):
    while True:
        command = input("Tapez q pour quitter \n")
        if command == "q":
            print("Arrêt du script...")
            x_Stop_event.set()
            stop_flask()
            break


def stop_flask():
    """ Fonction pour arreter proprement Flask """
    print("Arrêt du serveur Flask...")
    try:
        requests.get("http://0.0.0.0:5000/shutdown")
    except Exception as e:
        print(f"Erreur lors de l'arrêt de Flask: {e}")


def run_flask():
    app.run(debug=True, host='0.0.0.0', use_reloader=False)

if __name__ == "__main__":
    x_Stop_event = threading.Event()


    thread1 = threading.Thread(target=main_loop, args=(x_Stop_event,))
    thread2 = threading.Thread(target=listen_for_input, args=(x_Stop_event,))
    thread3 = threading.Thread(target=run_flask)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

