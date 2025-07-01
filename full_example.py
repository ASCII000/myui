"""
Arquivo para testes da aplicação
"""

from pymyui.controllers.app import MyApp


class UserForm:
    def __init__(self):
        self.app = MyApp(
            width=800,
            height=700,
            background_color="#363333",
            font_family="Segoe UI",
            primary_color="#707070",
            secondary_color="#C8C8C8",
        )

        self.fields = {
            "name": ("Nome completo:", "Digite seu nome completo"),
            "email": ("Email:", "Digite seu email"),
            "phone": ("Telefone:", "Digite seu telefone"),
            "cpf": ("CPF:", "Digite seu CPF"),
            "street": ("Rua:", "Digite sua rua"),
            "number": ("Número:", "Número da casa/apto"),
            "neighborhood": ("Bairro:", "Digite seu bairro"),
            "city": ("Cidade:", "Digite sua cidade"),
            "uf": ("UF:", "UF"),
        }

        self.inputs = {}
        self._build_form()
        self._build_submit_button()

    def _build_form(self):
        for key, (label_text, placeholder) in self.fields.items():
            layout = self.app.add_layout("horizontal")
            layout.add_widget(self.app.add_label(label_text), alignment="left")
            layout.setContentsMargins(20, 0, 300, 0)
            layout.add_stretch()

            input_widget = layout.add_widget(self.app.add_input(placeholder, width=300), alignment="left")
            self.inputs[key] = input_widget

    def _build_submit_button(self):
        submit_layout = self.app.add_layout("horizontal")
        submit_btn = self.app.add_button("Enviar", variant="success", font_size=12, width=300)
        submit_btn.onClick(self.submit_form)
        submit_layout.add_widget(submit_btn, alignment="right")

    def submit_form(self):
        if any(input_widget.text() == "" for input_widget in self.inputs.values()):
            self.app.window.notify(
                "Preencha todos os campos antes de enviar!",
                background_color="#866E6E",
                corner="top-left",
            )
            return

        print("=== Dados do formulário ===")
        for key, input_widget in self.inputs.items():
            print(f"{key.capitalize()}: {input_widget.text()}")
        print("===========================")

    def run(self):
        self.app.run()


if __name__ == "__main__":
    form = UserForm()
    form.run()
