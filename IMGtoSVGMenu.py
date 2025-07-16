import tkinter as tk
from tkinter import filedialog, messagebox
import os
import vtracer  # Make sure vtracer is installed

class VTracerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VTracer Image to SVG Converter")
        self.image_path = None

        self.settings = {
            "colormode": tk.StringVar(value="color"),
            "hierarchical": tk.StringVar(value="stacked"),
            "mode": tk.StringVar(value="spline"),
            "filter_speckle": tk.IntVar(value=20),
            "color_precision": tk.IntVar(value=8),
            "layer_difference": tk.IntVar(value=30),
            "corner_threshold": tk.IntVar(value=130),
            "length_threshold": tk.DoubleVar(value=10),
            "splice_threshold": tk.IntVar(value=50)
        }

        self.build_gui()

    def build_gui(self):
        tk.Button(self.root, text="Import Image", command=self.import_image).pack(pady=5)

        tk.Label(self.root, text="Clustering", font=("Arial", 12, "bold")).pack()
        self.create_radio_buttons("Color Mode", "colormode", [("B/W", "binary"), ("COLOR", "color")])
        self.create_radio_buttons("Layering", "hierarchical", [("CUTOUT", "cutout"), ("STACKED", "stacked")])
        self.create_slider("Filter Speckle (Cleaner)", "filter_speckle", 0, 128)
        self.create_slider("Color Precision (More accurate)", "color_precision", 1, 8)
        self.create_slider("Gradient Step (Less layers)", "layer_difference", 0, 128)

        tk.Label(self.root, text="Curve Fitting", font=("Arial", 12, "bold")).pack()
        self.create_radio_buttons("Curve Mode", "mode", [("PIXEL", "pixel"), ("POLYGON", "polygon"), ("SPLINE", "spline")])
        self.create_slider("Corner Threshold (Smoother)", "corner_threshold", 0, 180)
        self.create_slider("Segment Length (More coarse)", "length_threshold", 3.5, 10, resolution=0.1)
        self.create_slider("Splice Threshold (Less accurate)", "splice_threshold", 0, 180)

        tk.Button(self.root, text="Convert to SVG", command=self.convert_to_svg).pack(pady=10)

    def create_radio_buttons(self, label, var_name, options):
        frame = tk.Frame(self.root)
        tk.Label(frame, text=label).pack(side=tk.LEFT)
        for text, value in options:
            tk.Radiobutton(frame, text=text, variable=self.settings[var_name], value=value).pack(side=tk.LEFT)
        frame.pack(pady=2)

    def create_slider(self, label, var_name, min_val, max_val, resolution=1):
        frame = tk.Frame(self.root)
        tk.Label(frame, text=label).pack()
        tk.Scale(frame, from_=min_val, to=max_val, orient=tk.HORIZONTAL, variable=self.settings[var_name], resolution=resolution).pack()
        frame.pack(pady=2)

    def import_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )
        if file_path:
            self.image_path = file_path
            messagebox.showinfo("Image Selected", f"Selected:\n{file_path}")

    def convert_to_svg(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please import an image first.")
            return

        output_path = os.path.splitext(self.image_path)[0] + ".svg"

        try:
            vtracer.convert_image_to_svg_py(
                self.image_path,
                output_path,
                colormode=self.settings["colormode"].get(),
                hierarchical=self.settings["hierarchical"].get(),
                mode=self.settings["mode"].get(),
                filter_speckle=self.settings["filter_speckle"].get(),
                color_precision=self.settings["color_precision"].get(),
                layer_difference=self.settings["layer_difference"].get(),
                corner_threshold=self.settings["corner_threshold"].get(),
                length_threshold=self.settings["length_threshold"].get(),
                splice_threshold=self.settings["splice_threshold"].get()
            )
            messagebox.showinfo("Success", f"SVG saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VTracerGUI(root)
    root.mainloop()
