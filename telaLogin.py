import tkinter as tkinter

def login():
    email = input_email.get()
    senha = input_senha.get()
    if(email == "admin"):
        if(senha == "1234"):

app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")

# EMAIL
label_email = tk.Label(app, text="Email:")
label_email.pack(pady=5)
input_email = tk.Entry(app)
input_email.pack()

# SENHA
label_senha = tk.Label(app, text="Senha:")
label_senha.pack(pady=5)
input_email = tk.Entry(app)
input_email.pack()

btn_enviar = tk.Button(app, text="Enviar", command=login)
btn_enviar.pack()

app.mainloop()