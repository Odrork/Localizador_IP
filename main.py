import geocoder
import tkinter as tk

def LocalizacionIP(ip):
    g = geocoder.ip(ip)
    pais = g.country
    city = g.city
    return f"Country: {pais}\nCity: {city}"

def MostrarIP():
    ip = entry.get()
    location = LocalizacionIP(ip)
    label.config(text=location)

root = tk.Tk()
root.title("Localizador IP")

ip_label = tk.Label(root, text="IP:")
ip_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Mostrar", command=MostrarIP)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
