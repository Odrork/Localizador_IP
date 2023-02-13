import geocoder
import tkinter as tk

def get_location_from_ip(ip):
    g = geocoder.ip(ip)
    country = g.country
    city = g.city
    return f"Country: {country}\nCity: {city}"

def show_location():
    ip = entry.get()
    location = get_location_from_ip(ip)
    label.config(text=location)

root = tk.Tk()
root.title("IP Geolocation")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show Location", command=show_location)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
