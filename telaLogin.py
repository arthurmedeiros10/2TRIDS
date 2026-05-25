import tkinter as tk

def login():
    print("login realizado!")

app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")

label_email = tk.Label(app, text="Email:")
label_email.pack(pady=5)

input_email = tk.Entry(app)
input_email.pack()

btn_enviar = tk.Button(app, text="Enviar", command=login)
btn_enviar.pack()

app.mainloop()