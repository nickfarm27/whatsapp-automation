import pyautogui as pg
import webbrowser
import time
import pandas as pd

def main():
    # pg.FAILSAFE = False

    # your own csv file with Names, Phone Numbers, and the message
    # NOTE: You can customize the csv file however you like but make sure you update the code accordingly
    df = pd.read_csv("something.csv")

    for index, row in df.iterrows():
        print("")
        print(row["Name"])
        print(row["Phone Number"])
        print(row["Message"])

        message = f"Hi {row['Name']}! Your message is {row['Message']}"

        url = f"https://web.whatsapp.com/send?phone=+{row['Phone Number']}&text={message}"
        print(url)

        webbrowser.open(url)
        time.sleep(10)
        
        # update the values based on the location of the text field
        pg.click(1650, 960)
        time.sleep(1)
        
        pg.press("enter")
        time.sleep(2)
        
        with pg.hold("ctrl"):
            pg.press("w")
        time.sleep(2)

if __name__ == "__main__":
    main()