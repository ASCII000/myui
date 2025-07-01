from myui.controllers.app import MyApp

# Inicializa a aplicação
app = MyApp(
    width=400,
    height=200,
    background_color="#363333",
    font_family="Segoe UI",
    primary_color="#707070",
    secondary_color="#C8C8C8",
)

# Layout horizontal para agrupar label e input
layout = app.add_layout("horizontal")

# Adiciona label
layout.add_widget(app.add_label("Nome:"), alignment="left")

# Adiciona input com placeholder
input_nome = layout.add_widget(app.add_input("Digite seu nome", width=200), alignment="left")

# Função de clique do botão
def on_click():
    nome = input_nome.text()
    if nome == "":
        app.window.notify(
            "Digite seu nome antes de enviar!",
            background_color="#866E6E",
            corner="top-left",
        )
    else:
        print(f"Nome digitado: {nome}")

# Layout para o botão
button_layout = app.add_layout("horizontal")

# Adiciona botão
btn = app.add_button("Enviar", variant="success", font_size=12, width=200)
btn.onClick(on_click)
button_layout.add_widget(btn, alignment="center")

# Executa a aplicação
app.run()
