import pyautogui
import time

def perform_click():
    #Perform the click event at the current mouse cursor postion
    pyautogui.click()
    def main():
        #Loop indefinitely
        while True:
            try:
                #Perform a click event
                perform_click()
                print("Click event Performed")

                #Wait For 1 Minute Before performing the next click event
                time.sleep(4)
            except KeyboardInterrupt:
                print("\n Program Terminated By User")
                break

            if _name_=="_main_":
                main()
