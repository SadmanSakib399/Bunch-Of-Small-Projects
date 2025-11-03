from tkinter import *
import requests

quote = None


def button_change(yes_button):
    yes_button.config(image=green)

def get_quote(yes_button):
    global quote
    yes_button.config(image=red)
    canvas.delete(quote)
    responce = requests.get("https://api.kanye.rest")
    data = responce.json()
    data = data["quote"]
    quote = canvas.create_text(350, 350, text= data, font=("arial", 16, "bold"), fill="black", width= 400,)
    window.after(500 , lambda: button_change(yes_button))

window = Tk()
window.title("Kanye Quotes")
window.resizable(False, False)
canvas = Canvas(width=700, height=700)

background = PhotoImage(file="100 Days Of Learning Python/DAY 33 - Kanye Quotes/Kanye Quotes/background.png")
green = PhotoImage(file="100 Days Of Learning Python/DAY 33 - Kanye Quotes/Kanye Quotes/green.png")
red = PhotoImage(file="100 Days Of Learning Python/DAY 33 - Kanye Quotes/Kanye Quotes/red.png")

canvas.create_image(350, 350, image=background)


yes_button = Button(image= green, bg="#000000", activebackground="#212121", relief="flat", command= lambda: get_quote(yes_button))
yes_button.place(x=65, y=135)

get_quote(yes_button)

canvas.config(bg="#1E222D")
canvas.grid()


window.mainloop()