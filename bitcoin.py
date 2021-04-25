# importing different libraries

import tkinter as tk # python GUI library
import requests # run 'pip install requests' in cmd
from datetime import datetime


# Function for tracking bitCoin price
def trackBitCoin():
  url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
  responseVar = requests.get(url).json()
  price = responseVar["USD"]
  timeVar = datetime.now().strftime("%H:%M:%S")
  
  labelPrice.config(text = str(price) + '$')
  labelTime.config(text = "Updated at: " + timeVar)
  
  canvas.after(1000, trackBitCoin)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("BitCoin Tracker")

f1 = ("algerian", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text = "BitCoin Price", font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

trackBitCoin()
canvas.mainloop()
