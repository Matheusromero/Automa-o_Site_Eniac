import customtkinter as ctk 
from tkinter import messagebox
import time
ctk.set_appearance_mode("Dark")


class login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")

        largura=420
        altura=255
        self.update_idletasks()
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = int((largura_tela / 2) - (largura / 2))
        y = int((altura_tela / 2) - (altura / 2))

        self.geometry(f"{largura}x{altura}+{x}+{y}")
        self.construir_login()
   
    def executar(self):
        login = self.campo_login.get()
        senha = self.campo_senha.get()

        self.destroy()
        import automacao
        automacao.rodar(login, senha)
        

    def construir_login(self):
        texto_aviso2 = ctk.CTkLabel(self, text="Fique Tranquilo!")
        texto_aviso2.pack(pady=(0, 0))
        texto_aviso = ctk.CTkLabel(self, text="Esse codigo não armazenará nenhuma das seguintes informações:")
        texto_aviso.pack(pady=(0, 15))
        

        textoBasico = ctk.CTkLabel(self, text="Digite abaixo o seu login do Eniac:")
        textoBasico.pack()
        self.campo_login = ctk.CTkEntry(self, placeholder_text="Digite aqui o login", justify="center")
        self.campo_login.pack(pady=(0,15))

        textoBasico2 = ctk.CTkLabel(self, text="Digite abaixo a sua senha do Eniac:")
        textoBasico2.pack()
        self.campo_senha = ctk.CTkEntry(self, placeholder_text="Digite aqui a senha", justify="center")
        self.campo_senha.pack(pady=(0,20))

        botao = ctk.CTkButton(self, text="Clique aqui para continuar", command=self.executar)
        botao.pack()

    


    
    
        


janela = login()
janela.mainloop()
#messagebox.showinfo('Sucesso', "A automação foi finalizada com sucesso")