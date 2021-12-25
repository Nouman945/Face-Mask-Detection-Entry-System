from tkinter import *
import subprocess
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.title("Login System")
root.geometry("1199x600+100+100")
bg = Image.open('pic/mask1.jpg')
width, height = bg.size
bg = ImageTk.PhotoImage(bg)

# Function to resize the window


def resize_image(e):
   global image, resized, image2
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(280, 280, image=image2, anchor='nw')


# Bind the function to configure the parent window
root.bind("<Configure>", resize_image)


def run_program():
    subprocess.call(["python", "detection.py"])


canvas = Canvas(root, width=700, height=700, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
label = Label(root, text="Face Mask Detection Based Entry System",
              font=("Forte 25 bold"), bg='black', fg='white')
canvas.create_window(520, 20, anchor="nw", window=label)
label1 = Label(root, text=" Home Page", font=(
    "Ariel 30 bold"), bg='black', fg='white')
canvas.create_window(153, 110, anchor="nw", window=label1)


login1 = Button(root, text="Start Detection", font=("Ariel 21 bold"),
                width=11, padx=10, pady=2, bg="white", fg='black', relief=RAISED, activeforeground="white",
                activebackground="gray", command=run_program)
canvas.create_window(165, 220, anchor="nw", window=login1)

exit = Button(root, text="Exit", font=("Ariel 22 bold"),
              width=10, padx=10, pady=2, bg="white", fg='black', relief=RAISED, activeforeground="white",
              activebackground="gray", command=root.destroy)
canvas.create_window(165, 380, anchor="nw", window=exit)


root.mainloop()
