import tkinter as tk
from tkinter import ttk
import random
import math
import colorsys

class ColorSortApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Sorter")
        
        self.size = 180
        self.colors = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(self.size)]
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        
        self.sort_button = ttk.Button(root, text="Sort", command=self.sort)
        self.sort_button.pack()
        
        self.shuffle_button = ttk.Button(root, text="Shuffle", command=self.shuffle)
        self.shuffle_button.pack()
        
        self.draw_colors_in_circle()
        
    def sort(self):
        self.sort_colors_by_hue()
        self.draw_colors_in_circle()
    
    def shuffle(self):
        random.shuffle(self.colors)
        self.draw_colors_in_circle()
    
    def draw_colors_in_circle(self):
        self.canvas.delete("all")
        radius = 150
        center_x = self.canvas.winfo_reqwidth() // 2
        center_y = self.canvas.winfo_reqheight() // 2
        
        for i, color in enumerate(self.colors):
            angle = i * (360 / self.size)
            x1 = center_x + radius * math.cos(math.radians(angle))
            y1 = center_y + radius * math.sin(math.radians(angle))
            x2 = center_x + radius * math.cos(math.radians(angle + 360 / self.size))
            y2 = center_y + radius * math.sin(math.radians(angle + 360 / self.size))
            self.canvas.create_polygon(center_x, center_y, x1, y1, x2, y2, fill=color)
    
    def sort_colors_by_hue(self):
        # Convert colors to HSV and sort by hue
        hsv_colors = [colorsys.rgb_to_hsv(int(color[1:3], 16) / 255.0, int(color[3:5], 16) / 255.0, int(color[5:], 16) / 255.0) for color in self.colors]
        self.colors = [color for _, color in sorted(zip([color[0] for color in hsv_colors], self.colors))]
    
def main():
    root = tk.Tk()
    app = ColorSortApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
