import tkinter as tk
from tkinter import messagebox, filedialog

def parse_coords(text):
    coords = []
    parts = text.strip().split()
    for p in parts:
        lon, lat, *_ = p.split(',')
        coords.append((float(lon), float(lat)))
    return coords

def convert():
    text = input_box.get("1.0", "end").strip()
    if not text:
        messagebox.showerror("Error", "Paste Line GPS first!")
        return

    try:
        pts = parse_coords(text)
    except:
        messagebox.showerror("Error", "Invalid GPS format!")
        return

    placemarks = ""

    for i, (lon, lat) in enumerate(pts, start=1):
        placemarks += f"""
<Placemark>
    <name>Point {i}</name>
    <Point>
        <coordinates>{lon},{lat},0</coordinates>
    </Point>
</Placemark>
""".strip() + "\n\n"

    output_box.delete("1.0", "end")
    output_box.insert("end", placemarks)


def save_kml():
    content = output_box.get("1.0", "end").strip()
    if not content:
        messagebox.showerror("Error", "Nothing to save!")
        return

    kml_full = f"""
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
{content}
</Document>
</kml>
""".strip()

    path = filedialog.asksaveasfilename(
        defaultextension=".kml",
        filetypes=[("KML files", "*.kml")]
    )

    if path:
        with open(path, "w") as f:
            f.write(kml_full)
        messagebox.showinfo("Saved", "All placemarks saved successfully!")

# GUI
root = tk.Tk()
root.title("Line Points → Multiple Placemarks")
root.geometry("750x550")

tk.Label(root, text="Paste GPS Line Points (lon,lat,0 ...):", font=("Arial", 12)).pack()

input_box = tk.Text(root, height=10, width=80, font=("Courier", 10))
input_box.pack(pady=5)

tk.Button(root, text="Generate ALL Placemarks", font=("Arial", 12), command=convert).pack(pady=10)

tk.Label(root, text="Generated Placemarks:", font=("Arial", 12)).pack()

output_box = tk.Text(root, height=12, width=80, font=("Courier", 10))
output_box.pack(pady=5)

tk.Button(root, text="Save as KML", font=("Arial", 12), command=save_kml).pack(pady=10)

root.mainloop()
