# MyUI Framework 🚀

> **⚠️ Status: Em Desenvolvimento Ativo**  
> Este é um projeto em constante evolução. Novas funcionalidades e melhorias estão sendo implementadas regularmente.

## 📋 Visão Geral

**MyUI** é um framework Python minimalista e intuitivo para criação rápida de interfaces gráficas desktop, construído sobre o PySide6. Desenvolvido com foco na simplicidade e produtividade, oferece uma API fluente e componentes pré-estilizados para acelerar o desenvolvimento de aplicações desktop.

## ✨ Principais Características

### 🎯 **Simplicidade Extrema**
- API intuitiva e fluente
- Configuração mínima necessária
- Curva de aprendizado baixa
- Sintaxe limpa e expressiva

### 🎨 **Design System Integrado**
- Sistema de cores consistente e personalizável
- Componentes pré-estilizados com variantes
- Tipografia padronizada
- Layouts responsivos e flexíveis

### ⚡ **Produtividade Elevada**
- Criação de interfaces em poucas linhas de código
- Componentes reutilizáveis
- Sistema de notificações integrado
- Gerenciamento automático de layouts

### 🔧 **Flexibilidade Total**
- Personalização completa de estilos
- Suporte a temas customizados
- Integração nativa com PySide6
- Extensibilidade para novos componentes

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+** - Linguagem base
- **PySide6** - Framework Qt para Python
- **Poetry** - Gerenciamento de dependências
- **Type Hints** - Tipagem estática para melhor DX

## 📦 Instalação

### Pré-requisitos
- Python 3.11 ou superior
- Poetry (recomendado) ou pip

### Via Poetry (Recomendado)
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/pymyui.git
cd pymyui

# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell
```

### Via pip
```bash
pip install pyside6
```

## 🚀 Primeiros Passos

### Exemplo Básico
```python
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
```

### Exemplo Completo - Formulário de Usuário
```python
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
            
            input_widget = layout.add_widget(
                self.app.add_input(placeholder, width=300), 
                alignment="left"
            )
            self.inputs[key] = input_widget

    def _build_submit_button(self):
        submit_layout = self.app.add_layout("horizontal")
        submit_btn = self.app.add_button(
            "Enviar", 
            variant="success", 
            font_size=12, 
            width=300
        )
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
```

## 🧩 Componentes Disponíveis

### 📝 **MyLabel**
Labels estilizados com suporte a alinhamento, cores e tipografia personalizada.

```python
label = app.add_label(
    "Texto do Label",
    size_text=14,
    color_text="#ffffff",
    alignment="center",
    font_weight="bold"
)
```

### 🔘 **MyButton**
Botões com variantes pré-definidas e efeitos visuais.

```python
# Variantes disponíveis: "success", "error", "natural"
button = app.add_button(
    "Clique Aqui",
    variant="success",
    font_size=12,
    width=200,
    height=50
)
button.onClick(callback_function)
```

### 📝 **MyInput**
Campos de entrada com placeholder e estilização personalizada.

```python
input_field = app.add_input(
    "Digite aqui...",
    size_text=12,
    width=300,
    height=40,
    border_radius=8
)
```

### 📋 **MyLayout**
Sistema de layouts flexível para organizar componentes.

```python
# Layout horizontal
horizontal_layout = app.add_layout("horizontal")

# Layout vertical  
vertical_layout = app.add_layout("vertical")

# Adicionar widgets aos layouts
layout.add_widget(component, alignment="center")
layout.add_stretch()  # Espaçamento flexível
```

### 🔔 **MyNotify**
Sistema de notificações toast integrado.

```python
app.window.notify(
    "Operação realizada com sucesso!",
    background_color="#4CAF50",
    corner="top-right",
    duration=3000
)
```

## 🎨 Personalização

### Cores e Temas
```python
app = MyApp(
    background_color="#1a1a1a",      # Cor de fundo
    primary_color="#007acc",         # Cor primária
    secondary_color="#ffffff",       # Cor secundária
    font_family="Roboto"             # Fonte personalizada
)
```

### Estilos de Componentes
```python
# Botão personalizado
button = app.add_button(
    "Ação",
    variant="success",
    border_radius=12,
    padding=15,
    font_size=14
)

# Input personalizado
input_field = app.add_input(
    "Placeholder",
    border_radius=8,
    padding=12,
    margin=8
)
```

## 📁 Estrutura do Projeto

```
myui/
├── main.py                 # Exemplo de uso
├── pyproject.toml         # Configuração do projeto
├── myui/
│   ├── __init__.py
│   ├── controllers/
│   │   └── app.py         # Classe principal MyApp
│   └── components/
│       ├── __init__.py
│       ├── my_button.py   # Componente de botão
│       ├── my_input.py    # Componente de entrada
│       ├── my_label.py    # Componente de label
│       ├── my_layout.py   # Sistema de layouts
│       └── my_notify.py   # Sistema de notificações
└── tests/                 # Testes automatizados
```

## 🔮 Roadmap

### ✅ **Implementado**
- [x] Sistema de layouts horizontal e vertical
- [x] Componentes básicos (Label, Button, Input)
- [x] Sistema de notificações toast
- [x] Personalização de cores e temas
- [x] API fluente e intuitiva
- [x] Suporte a callbacks e eventos

### 🚧 **Em Desenvolvimento**
- [ ] Componente de tabela (MyTable)
- [ ] Componente de menu (MyMenu)
- [ ] Sistema de modais/dialogs
- [ ] Componente de progress bar
- [ ] Suporte a ícones
- [ ] Temas predefinidos (Dark/Light)

### 📋 **Planejado**
- [ ] Componente de gráficos
- [ ] Sistema de validação de formulários
- [ ] Componente de upload de arquivos
- [ ] Suporte a animações avançadas
- [ ] Documentação interativa
- [ ] Exemplos e templates

## 🤝 Contribuindo

Este projeto está em desenvolvimento ativo e aceita contribuições! 

### Como Contribuir
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes de Contribuição
- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Siga as convenções de nomenclatura existentes
- Atualize a documentação quando necessário

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Emerson Silva**
- GitHub: [@ASCII000](https://github.com/ASCII000)
- LinkedIn: [Emerson Silva](https://www.linkedin.com/in/emerson-silva-361048266)

## 🙏 Agradecimentos

- **PySide6** - Framework Qt para Python
- **Qt Company** - Framework Qt
- **Comunidade Python** - Suporte e inspiração

---

## 💡 Por que MyUI?

### 🎯 **Problema Resolvido**
Criação de interfaces desktop em Python frequentemente envolve código verboso e configurações complexas. MyUI simplifica esse processo oferecendo uma API intuitiva e componentes pré-estilizados.

### 🚀 **Vantagens Competitivas**
- **Simplicidade**: API mais limpa que PySide6 puro
- **Produtividade**: Desenvolvimento 3x mais rápido
- **Consistência**: Design system integrado
- **Flexibilidade**: Personalização total mantendo simplicidade
- **Performance**: Baseado em PySide6, performance nativa

### 🎨 **Diferencial de Design**
- Sistema de cores consistente
- Componentes com variantes pré-definidas
- Tipografia padronizada
- Layouts responsivos
- Notificações integradas

---

**⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!** 