import time
import threading

from current_data import CurrentData


obj_Current_data = CurrentData()


def main_loop(x_Stop_event):
    while not x_Stop_event.is_set() :
        obj_Current_data.acquisition_data()

        for obj_Mesure in obj_Current_data.list_Mesures :
            obj_Mesure.threshold_check()

        time.sleep(2)



def listen_for_input(x_Stop_event):
    while True:
        command = input("Entrez une commande (q pour quitter) : ")
        if command == "q":
            print("Arrêt du script...")
            x_Stop_event.set()
            break


if __name__ == "__main__":
    x_Stop_event = threading.Event()


    thread1 = threading.Thread(target=main_loop, args=(x_Stop_event,))
    thread2 = threading.Thread(target=listen_for_input, args=(x_Stop_event,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

