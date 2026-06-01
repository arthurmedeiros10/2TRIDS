import tkinter
from conta import Conta
import json
def cadastrar():
    agencia = input_agencia.get()
    titular = input_titular.get()
    cpf = input_cpf.get()
    nova_conta = Conta(agencia, titular, cpf)
    with open("clientes.json", "r") as clientes_leitura:
        clientes = json.load(clientes_leitura)
    # adicionar o novo cliente
    clientes.append({
        "titular": nova_conta.titular,
        "agencia": nova_conta.agencia,
        "numero": nova_conta.numero,
        "cpf": nova_conta.cpf,
        "saldo": nova_conta.saldo,
        "senha": nova_conta.senha,
        "chavepix": nova_conta.chavepix
    })
    # salvar no arquivo
    with open("clientes.json", "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)
    # resposta de sucesso na tela
    label_resposta.configure(
        text=f"Conta: {nova_conta.numero} Titular: {nova_conta.titular} cadastrado com sucesso!",
        fg="green")