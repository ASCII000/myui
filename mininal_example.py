import random

from pymyui.controllers.app import MyApp

# Cria uma aplicação com configurações personalizadas
app = MyApp(
    width=800,
    height=200,
    background_color="#363333",
    primary_color="#707070",
    secondary_color="#C8C8C8",
    font_family="Segoe UI"
)

# Adiciona um layout vertical
layout = app.add_layout("vertical")

# Cria componentes
label = app.add_label("Olá, MyUI!", size_text=16, color_text="#ffffff")
button = app.add_button("Clique Aqui", variant="success")

# Acao do botao
cool_names = [
    "Alice", "Bob", "Charlie", "Diana", "Eva", "Fiona", "Grace", "Helen", "Ivy", "Judy"
]

button.onClick(lambda: label.setText(f"Olá, {random.choice(cool_names)}!"))

# Adiciona componentes ao layout
layout.setContentsMargins(20, 20, 20, 20)
layout.add_widget(label, alignment="center")
layout.add_widget(button, alignment="center")

# Executa a aplicação
app.run()