import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter

def reduce_colors(image, num_colors):
    return image.convert('P', palette=Image.ADAPTIVE, colors=num_colors).convert('RGB')

def reduce_resolution(image, scale_percent):
    width, height = image.size
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

def reduce_fidelity(image, quality):
    return image, quality

def simplify_shapes(image, level):
    for _ in range(level):
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return image

def process_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if not file_path:
        return

    try:
        image = Image.open(file_path)

        if color_var.get():
            image = reduce_colors(image, color_slider.get())
        if resolution_var.get():
            image = reduce_resolution(image, resolution_slider.get())
        if fidelity_var.get():
            image, quality = reduce_fidelity(image, fidelity_slider.get())
        else:
            quality = 95
        if shape_var.get():
            image = simplify_shapes(image, shape_slider.get())

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
        if save_path:
            image.save(save_path, quality=quality)
            messagebox.showinfo("Success", f"Image saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Image Minimizer with Sliders")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open and Process Image", command=process_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

options_frame = tk.Frame(root)
options_frame.pack(padx=10, pady=10)

color_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Reduce Colors", variable=color_var).grid(row=0, column=0, sticky='w')
color_slider = tk.Scale(options_frame, from_=2, to=256, orient='horizontal')
color_slider.set(64)
color_slider.grid(row=0, column=1)

resolution_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Reduce Resolution (%)", variable=resolution_var).grid(row=1, column=0, sticky='w')
resolution_slider = tk.Scale(options_frame, from_=10, to=100, orient='horizontal')
resolution_slider.set(50)
resolution_slider.grid(row=1, column=1)

fidelity_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Reduce Fidelity (Quality)", variable=fidelity_var).grid(row=2, column=0, sticky='w')
fidelity_slider = tk.Scale(options_frame, from_=10, to=95, orient='horizontal')
fidelity_slider.set(70)
fidelity_slider.grid(row=2, column=1)

shape_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Simplify Shapes (Level)", variable=shape_var).grid(row=3, column=0, sticky='w')
shape_slider = tk.Scale(options_frame, from_=0, to=5, orient='horizontal')
shape_slider.set(1)
shape_slider.grid(row=3, column=1)

root.mainloop()
