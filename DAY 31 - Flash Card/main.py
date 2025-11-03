import pandas 
from tkinter import *

selected_word = None
is_active = False
skip = False
known_words = []


def random_words(state):
    global selected_word, known_words
    data = pandas.read_csv('100 Days Of Learning Python/DAY 31 - Flash Card/french_words.csv')

    for _ in range(100):  # Prevent infinite loop
        random_row = data.sample(n=1)
        selected_word = random_row.iloc[0].tolist()

        if selected_word[0] not in known_words and state == True:
            known_words.append(selected_word[0])
            print(known_words)
            return selected_word
        elif selected_word[0] not in known_words and state == False:
            print(known_words)
            return selected_word

    print("All words exhausted!")
    return None


def flash_card(state):
    global is_active, skip
    t = time.get() 

    if not is_active:
        is_active = True
        temp = random_words(state)
        canvas.create_image(380, 300, image=card_front)
        canvas.create_text(390, 200, text="FRENCH", font=("arial", 30, "bold"), fill="white")
        canvas.create_text(390, 350, text=temp[0], font=("arial", 30, "bold"), fill="white")
        window.after(1000 * t, lambda: img_change(temp[1]))


def img_change(word):
    global is_active
    canvas.create_image(380, 300, image=card_back)
    canvas.create_text(390, 200, text="ENGLISH", font=("arial", 30, "bold"), fill="white")
    canvas.create_text(390, 350, text=word, font=("arial", 30, "bold"), fill="white")
    is_active = False


# UI SETTING
window = Tk()
window.title("Flash Card")
window.resizable(False, False)
time = IntVar()

canvas = Canvas(width=900, height=700)
card_front = PhotoImage(file="100 Days Of Learning Python\DAY 31 - Flash Card\card front.png")
card_back = PhotoImage(file="100 Days Of Learning Python\DAY 31 - Flash Card\card back.png")
side_Card = PhotoImage(file="100 Days Of Learning Python\DAY 31 - Flash Card\side_card.png")
yes_img = PhotoImage(file="100 Days Of Learning Python\DAY 31 - Flash Card\yes.png")
no_img = PhotoImage(file="100 Days Of Learning Python/DAY 31 - Flash Card/no.png")

s1 = Scale(variable = time, from_ = 1, to = 100, width=50,) 
s1.set(5)
s1.place(x=710, y=260)

canvas.create_image(750, 300, image=side_Card)
flash_card(False)

yes_button = Button( image = yes_img, bg="#1E222D", activebackground="#1E222D", relief="flat", command = lambda: flash_card(True))
yes_button.place(x=230, y=520)
no_button = Button( image = no_img, bg="#1E222D", activebackground="#1E222D", relief="flat", command = lambda: flash_card(False))
no_button.place(x=430, y=520)

# skip_button = Button(text = "Time Skip", fg="white", bg="#313746", font=("Arial", 18, "bold"), activebackground="#1E222D", relief="flat", command = lambda: flash_card(False))
# skip_button.place(x=682, y=420)


canvas.config(bg="#1E222D")
canvas.grid()


window.mainloop()