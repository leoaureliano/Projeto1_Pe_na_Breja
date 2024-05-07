import tkinter as tk
from tkinter import messagebox
from database import Database

db = Database()

def login(username, password):
    user = db.get_user_by_username(username)
    if user:
        stored_password = user[2]  # O índice 2 corresponde à coluna 'password' na tabela 'users'
        if password == stored_password:
            login_successful(username)
        else:
            messagebox.showerror("Erro de Login", "Senha incorreta. Por favor, tente novamente.")
    else:
        messagebox.showerror("Erro de Login", "Usuário não encontrado.")

def register():
    register_window()

def register_user():
    username = new_username_entry.get()
    password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()
    is_over_18 = over_18_var.get()

    if password != confirm_password:
        messagebox.showerror("Erro de Senha", "As senhas fornecidas não coincidem. Por favor, tente novamente.")
    elif not is_over_18:
        messagebox.showerror("Erro de Registro", "Proibido para menores de 18 anos.")
    else:
        if db.get_user_by_username(username):
            messagebox.showerror("Erro de Registro", "O nome de usuário já está em uso. Por favor, escolha outro.")
        else:
            db.insert_user(username, password)
            messagebox.showinfo("Registro Bem-sucedido", "OK, você foi registrado. Beba com moderação!")

def register_window():
    # Criar nova janela para registro
    register_window = tk.Toplevel()
    register_window.title("Registrar")

    # Campos de entrada para registro
    new_username_label = tk.Label(register_window, text="Novo Usuário:", font=("Arial", 12))
    new_username_label.grid(row=0, column=0, padx=10, pady=5)

    global new_username_entry
    new_username_entry = tk.Entry(register_window, font=("Arial", 12))
    new_username_entry.grid(row=0, column=1, padx=10, pady=5)

    new_password_label = tk.Label(register_window, text="Nova Senha:", font=("Arial", 12))
    new_password_label.grid(row=1, column=0, padx=10, pady=5)

    global new_password_entry
    new_password_entry = tk.Entry(register_window, show="*", font=("Arial", 12))
    new_password_entry.grid(row=1, column=1, padx=10, pady=5)

    confirm_password_label = tk.Label(register_window, text="Confirmar Senha:", font=("Arial", 12))
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5)

    global confirm_password_entry
    confirm_password_entry = tk.Entry(register_window, show="*", font=("Arial", 12))
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

    global over_18_var
    over_18_var = tk.BooleanVar()
    over_18_checkbox = tk.Checkbutton(register_window, text="Sou maior de 18 anos.", variable=over_18_var, font=("Arial", 12))
    over_18_checkbox.grid(row=3, columnspan=2, padx=10, pady=5)

    register_button = tk.Button(register_window, text="Registrar", width=15, font=("Arial", 12), command=register_user)
    register_button.grid(row=4, columnspan=2, pady=10)

def open_user_settings():
    user_settings_window = tk.Toplevel()
    user_settings_window.title("Configurações do Usuário")

    # Obtém as informações do usuário do banco de dados (isso pode variar dependendo de como você implementou o banco de dados)
    user_info = db.get_user_info()  # Isso deve retornar as informações do usuário (nome, data de nascimento, etc.)

    # Rótulos e entradas para nome completo e data de nascimento
    full_name_label = tk.Label(user_settings_window, text="Nome Completo:", font=("Arial", 12))
    full_name_label.grid(row=0, column=0, padx=10, pady=5)
    full_name_entry = tk.Entry(user_settings_window, font=("Arial", 12), width=30)
    full_name_entry.grid(row=0, column=1, padx=10, pady=5)

    dob_label = tk.Label(user_settings_window, text="Data de Nascimento:", font=("Arial", 12))
    dob_label.grid(row=1, column=0, padx=10, pady=5)
    dob_entry = tk.Entry(user_settings_window, font=("Arial", 12), width=30)
    dob_entry.grid(row=1, column=1, padx=10, pady=5)

    # Botão para trocar a senha
    change_password_button = tk.Button(user_settings_window, text="Trocar Senha", width=15, font=("Arial", 12))
    change_password_button.grid(row=2, columnspan=2, pady=10)

    # Botão de voltar
    back_button = tk.Button(user_settings_window, text="Voltar", width=10, font=("Arial", 12), command=user_settings_window.destroy)
    back_button.grid(row=3, columnspan=2, pady=10)

def login_successful(username):
    # Exibir segundo menu após o login bem-sucedido
    root.withdraw()  # Esconde a janela de login

    # Cria uma nova janela para o segundo menu
    global second_menu
    second_menu = tk.Toplevel()
    second_menu.title("Opções de Cerveja e Locais")

    # Botão para abrir as configurações do usuário
    settings_button = tk.Button(second_menu, text="Usuário", width=10, font=("Arial", 12), command=open_user_settings)
    settings_button.grid(row=0, column=1, pady=10, padx=10, sticky="e")

    # Rótulo de boas-vindas
    welcome_label = tk.Label(second_menu, text=f"Bem-vindo, {username}!", font=("Arial", 14))
    welcome_label.grid(row=0, column=0, pady=20)

    # Botões para adicionar cerveja e local
    add_beer_button = tk.Button(second_menu, text="Adicione Cerveja", width=15, font=("Arial", 12))
    add_beer_button.grid(row=1, column=0, padx=10, pady=10)

    add_location_button = tk.Button(second_menu, text="Adicione Local", width=15, font=("Arial", 12))
    add_location_button.grid(row=1, column=1, padx=10, pady=10)

    # Botões para procurar locais e cervejas
    search_locations_button = tk.Button(second_menu, text="Procurar Locais", width=15, font=("Arial", 12))
    search_locations_button.grid(row=2, column=0, padx=10, pady=10)

    search_beers_button = tk.Button(second_menu, text="Procurar Cervejas", width=15, font=("Arial", 12))
    search_beers_button.grid(row=2, column=1, padx=10, pady=10)

    # Botão de sair
    logout_button = tk.Button(second_menu, text="Sair", width=10, font=("Arial", 12), command=close_second_menu)
    logout_button.grid(row=3, column=0, columnspan=2, pady=20)

def close_second_menu():
    # Fecha a janela do segundo menu e mostra a janela de login novamente
    second_menu.destroy()
    root.deiconify()

# Função principal para iniciar o aplicativo
def main():
    # Criar janela principal
    global root
    root = tk.Tk()
    root.title("App de Cervejas e Locais de Visita")

    # Rótulo de boas-vindas
    welcome_label = tk.Label(root, text="Pe na Breja", font=("Arial", 18))
    welcome_label.pack(pady=20)

    # Campos de entrada para usuário e senha (login)
    username_label = tk.Label(root, text="Usuário:", font=("Arial", 12))
    username_label.pack()

    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack()

    password_label = tk.Label(root, text="Senha:", font=("Arial", 12))
    password_label.pack()

    password_entry = tk.Entry(root, show="*", font=("Arial", 12))
    password_entry.pack()

    login_button = tk.Button(root, text="Login", width=15, font=("Arial", 12), command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.pack(pady=10)

    # Botão de registro
    register_button = tk.Button(root, text="Registrar", width=15, font=("Arial", 12), command=register)
    register_button.pack(pady=10)

    # Executar o loop principal da interface gráfica
    root.mainloop()

# Verificar se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
