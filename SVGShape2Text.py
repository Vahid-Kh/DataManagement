import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET
import random
import string
import os

def generate_random_char():
    return random.choice(string.ascii_uppercase + string.digits)

def replace_shapes_with_text(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', ns['svg'])

    shape_tags = ['rect', 'circle', 'ellipse', 'line', 'polygon', 'path']

    for tag in shape_tags:
        for elem in root.findall(f'.//svg:{tag}', ns):
            # Try to get coordinates for placing text
            x = float(elem.attrib.get('x', elem.attrib.get('cx', '0')))
            y = float(elem.attrib.get('y', elem.attrib.get('cy', '0')))

            text_elem = ET.Element('text', {
                'x': str(x),
                'y': str(y),
                'font-size': '12',
                'fill': 'black'
            })
            text_elem.text = generate_random_char()

            parent = root
            parent.remove(elem)
            root.append(text_elem)

    output_path = os.path.splitext(svg_path)[0] + '_modified.svg'
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    return output_path

def select_file_and_process():
    file_path = filedialog.askopenfilename(
        title="Select SVG File",
        filetypes=[("SVG files", "*.svg")]
    )
    if file_path:
        try:
            output = replace_shapes_with_text(file_path)
            messagebox.showinfo("Success", f"Modified SVG saved as:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process SVG:\n{e}")

# GUI setup
root = tk.Tk()
root.withdraw()  # Hide the main window
select_file_and_process()
