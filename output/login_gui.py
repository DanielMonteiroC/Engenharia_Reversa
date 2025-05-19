# uncompyle6 version 3.9.2
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: login_gui.py
import tkinter as tk
from tkinter import messagebox
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        mostrar_segredo()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")


def mostrar_segredo():
    janela.withdraw()
    segredo = tk.Toplevel()
    segredo.title("Segredo Misterioso")
    segredo.geometry("300x150")
    tk.Label(segredo, text="🕵️ O segredo misterioso é:\nPython domina o mundo!", font=('Helvetica',
                                                                                       12),
      pady=20).pack()
    tk.Button(segredo, text="Fechar", command=(lambda: (segredo.destroy(), janela.deiconify()))).pack(pady=10)


janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x180")
tk.Label(janela, text="Usuário:").pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()
tk.Label(janela, text="Senha:").pack(pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()
tk.Button(janela, text="Entrar", command=verificar_login).pack(pady=15)
janela.mainloop()
