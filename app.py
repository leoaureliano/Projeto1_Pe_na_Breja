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
            messagebox.showinfo("Registro Bem-sucedido", "Beba com moderação!")
            register_window.destroy()  # Fechar a janela de registro após o registro bem-sucedido

def register_window():
    # Criar nova janela para registro
    global register_window
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

    # Rótulo de boas-vindas
    welcome_label = tk.Label(user_settings_window, text="Configurações do Usuário", font=("Arial", 14))
    welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Botão de voltar
    back_button = tk.Button(user_settings_window, text="Voltar", width=10, font=("Arial", 12), command=user_settings_window.destroy)
    back_button.grid(row=4, columnspan=2, pady=10)

def add_beer():
    def send_beer():
        beer_name = beer_name_entry.get()
        beer_rating = beer_rating_entry.get()

        # Aqui você enviará os dados para o banco de dados
        db.insert_beer(beer_name, beer_rating)
        messagebox.showinfo("Cerveja adicionada com sucesso!")
        add_beer_window.withdraw()  # Esconder a janela de adicionar cerveja após o envio
        second_menu.deiconify() 

    second_menu.withdraw()  # Esconder o segundo menu

    # Criar nova janela para adicionar cerveja
    add_beer_window = tk.Toplevel()
    add_beer_window.title("Adicionar Cerveja")

    beer_name_label = tk.Label(add_beer_window, text="Nome da Cerveja:", font=("Arial", 12))
    beer_name_label.grid(row=0, column=0, padx=10, pady=5)

    global beer_name_entry
    beer_name_entry = tk.Entry(add_beer_window, font=("Arial", 12))
    beer_name_entry.grid(row=0, column=1, padx=10, pady=5)

    rating_label = tk.Label(add_beer_window, text="Classificação (1-5):", font=("Arial", 12))
    rating_label.grid(row=1, column=0, padx=10, pady=5)

    global beer_rating_entry
    beer_rating_entry = tk.Entry(add_beer_window, font=("Arial", 12))
    beer_rating_entry.grid(row=1, column=1, padx=10, pady=5)

    send_button = tk.Button(add_beer_window, text="Enviar", width=10, font=("Arial", 12), command=send_beer)
    send_button.grid(row=2, columnspan=2, pady=10)

    back_button = tk.Button(add_beer_window, text="Voltar", width=10, font=("Arial", 12), command=lambda: back_to_second_menu(add_beer_window))
    back_button.grid(row=3, columnspan=2, pady=10)

def add_location():
    def send_location():
        location_name = location_name_entry.get()
        location_rating = location_rating_entry.get()

        # Aqui você enviará os dados para o banco de dados
        db.insert_location(location_name, location_rating)
        messagebox.showinfo("Sucesso", "Local adicionado com sucesso!")
        add_location_window.withdraw()  # Esconder a janela de adicionar local após o envio
        second_menu.deiconify()
        
    second_menu.withdraw()  # Esconder o segundo menu

    # Criar nova janela para adicionar local
    add_location_window = tk.Toplevel()
    add_location_window.title("Adicionar Local")

    location_name_label = tk.Label(add_location_window, text="Nome do Local:", font=("Arial", 12))
    location_name_label.grid(row=0, column=0, padx=10, pady=5)

    global location_name_entry
    location_name_entry = tk.Entry(add_location_window, font=("Arial", 12))
    location_name_entry.grid(row=0, column=1, padx=10, pady=5)

    rating_label = tk.Label(add_location_window, text="Classificação (1-5):", font=("Arial", 12))
    rating_label.grid(row=1, column=0, padx=10, pady=5)

    global location_rating_entry
    location_rating_entry = tk.Entry(add_location_window, font=("Arial", 12))
    location_rating_entry.grid(row=1, column=1, padx=10, pady=5)

    send_button = tk.Button(add_location_window, text="Enviar", width=10, font=("Arial", 12), command=send_location)
    send_button.grid(row=2, columnspan=2, pady=10)

    back_button = tk.Button(add_location_window, text="Voltar", width=10, font=("Arial", 12), command=lambda: back_to_second_menu(add_location_window))
    back_button.grid(row=3, columnspan=2, pady=10)

def back_to_second_menu(window):
    window.destroy()  # Fechar a janela atual
    second_menu.deiconify()  # Mostrar o segundo menu


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
    add_beer_button = tk.Button(second_menu, text="Adicionar Cerveja", width=15, font=("Arial", 12), command=add_beer)
    add_beer_button.grid(row=1, column=0, padx=10, pady=10)

    add_location_button = tk.Button(second_menu, text="Adicionar Local", width=15, font=("Arial", 12), command=add_location)
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

def close_window(window):
    window.destroy()

# Função principal para iniciar o aplicativo
def main():
    # Criar janela principal
    global root
    root = tk.Tk()
    root.title("App de Cervejas e Tour cervejeiros")

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
