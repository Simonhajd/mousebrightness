import tkinter as tk
from screeninfo import get_monitors
import pyautogui
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
def create_highlighted_edge(window, x, y, width, height):
    window.canvas.create_rectangle(x, y, x + width, y + height, fill="red", stipple="gray50")

def update_progress_bar(progressbar, screen_width, screen_height):
    x, y = pyautogui.position()
    progress = 100 - (y / (screen_height / 100))
    progressbar['value'] = progress
    progressbar.after(1, update_progress_bar, progressbar, screen_width, screen_height)


def main():
    root = tk.Tk()
    root.attributes('-alpha', 0.5)
    root.attributes('-topmost', True)
    root.overrideredirect(True)

    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    canvas = tk.Canvas(root, bg='blue', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    root.canvas = canvas


    PIL.Image.open("mono.png")
    image = PIL.Image.open("mono.png")
    image = image.resize((100, 100))  # adjust the size as needed
    photo = PIL.ImageTk.PhotoImage(image)
    canvas.create_image(50, 50, anchor=tk.NW, image=photo)

    progressbar = ttk.Progressbar(root, orient=tk.VERTICAL, length=160, style="green.Horizontal.TProgressbar") 
    progressbar.place(x=(screen_width / 2), y=(screen_height / 6))


    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", background='#FFFF00')

    update_progress_bar(progressbar, screen_width, screen_height) 

    edge_width = 20
    create_highlighted_edge(root, 0, 0, screen_width, edge_width)
    create_highlighted_edge(root, 0, screen_height - edge_width, screen_width, edge_width)
    create_highlighted_edge(root, 0, 0, edge_width, screen_height)
    create_highlighted_edge(root, screen_width - edge_width, 0, edge_width, screen_height)

    root.mainloop()

if __name__ == "__main__":
    main()