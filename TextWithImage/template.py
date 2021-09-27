import pyautogui as pg
import webbrowser
import time
import pandas as pd
import win32clipboard
from io import BytesIO
from PIL import Image

def copyImageToClipboard(path):
    image = Image.open(path)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def main():
    # pg.FAILSAFE = False

    # your own csv file with Names, Phone Numbers, the message, and the image file path
    # NOTE: You can customize the csv file however you like but make sure you update the code accordingly
    df = pd.read_csv("something.csv")

    for index, row in df.iterrows():
        print("")
        print(row["Name"])
        print(row["Phone Number"])
        print(row["Message"])

        message = f"Hello {row['Name']}! Your message is {row['Message']}"

        url = f"https://web.whatsapp.com/send?phone=+{row['Phone Number']}&text={message}"
        print(url)

        webbrowser.open(url)
        time.sleep(7)
        
        # update the values based on the location of the text field
        pg.click(1650, 960)
        time.sleep(1)

        imgPath = f"images/{row['image']}.png" # change the extension based on your images
        copyImageToClipboard(imgPath)

        # paste image
        with pg.hold("ctrl"):
            pg.press("v")
        time.sleep(2)
        
        pg.press("enter")
        time.sleep(4)

        with pg.hold("ctrl"):
            pg.press("w")
        time.sleep(1)

if __name__ == "__main__":
    main()