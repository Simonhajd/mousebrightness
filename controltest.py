import tkinter as tk
from screeninfo import get_monitors

def create_highlighted_edge(window, x, y, width, height):

    window.canvas.create_rectangle(x, y, x + width, y + height, fill="red", stipple="gray50")

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

   
    edge_width = 10  
    create_highlighted_edge(root, 0, 0, screen_width, edge_width) 
    create_highlighted_edge(root, 0, screen_height - edge_width, screen_width, edge_width)  
    create_highlighted_edge(root, 0, 0, edge_width, screen_height) 
    create_highlighted_edge(root, screen_width - edge_width, 0, edge_width, screen_height) 

    root.mainloop()

if __name__ == "__main__":
    main()