import tkinter as tk
from tkinter import filedialog, messagebox
import os
import vtracer


def convert_to_svg():
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
    )

    if not file_path:
        messagebox.showwarning("No Selection", "No image file was selected.")
        return

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(os.path.dirname(file_path), f"{base_name}.svg")

    try:
        vtracer.convert_image_to_svg_py(file_path, output_path)
        messagebox.showinfo("Conversion Successful", f"SVG saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Conversion Failed", f"An error occurred:\n{str(e)}")


root = tk.Tk()
root.title("Image to SVG Converter")
root.geometry("300x150")

convert_button = tk.Button(root, text="Import and Convert Image", command=convert_to_svg, width=25, height=2)
convert_button.pack(pady=40)

root.mainloop()
