import tkinter as tk

def login():
    if input_agencia.get() == "admin":
        if input_agencia.get() == "1234":
            label_resposta.configure(text="Cadastro realizado com sucesso!", fg="green")
        else:
            label_resposta.configure(text="Falha no cadastro", fg="red")
    else:
        label_resposta.configure(text="Falha no cadastro", fg="red")

app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")             

# AGÊNCIA
label_agencia = tk.Label(app, text="Agência:")
label_agencia.pack(pady=5)
input_agencia = tk.Entry(app)
input_agencia.pack()

# TITULAR
label_titular = tk.Label(app, text="Titular:")
label_titular.pack(pady=5)
input_titular = tk.Entry(app)
input_titular.pack()

# CPF
label_cpf = tk.Label(app, text="CPF:")
label_cpf.pack(pady=5)
input_cpf = tk.Entry(app)
input_cpf.pack()

# CADASTRAR
botao = tk.Button(app, text="Cadastrar Cliente", command=login)
botao.pack(pady=10)

# RESPOSTA
label_resposta = tk.Label(app, text="")
label_resposta.pack(pady=5)

app.mainloop() # -> executar a tela em laço infinito