import customtkinter
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkCheckBox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")

texto = CTkLabel(janela, text="FazerLogin")
texto.pack(padx=10, pady=10)

email = CTkEntry(janela, placeholder_text="Gmail")
email.pack(padx=10, pady=10)

senha = CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

numero = CTkEntry(janela, placeholder_text="Numero")
numero.pack(padx=10, pady=10)

checkbox = CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
