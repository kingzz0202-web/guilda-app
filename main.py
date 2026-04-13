from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime, timedelta
import os

ARQUIVO = "dados.txt"
LIMITE = 30

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.input = TextInput(hint_text="Ex: Vinicius 12d", size_hint=(1, 0.2))
        self.add_widget(self.input)

        btn_add = Button(text="Adicionar")
        btn_add.bind(on_press=self.adicionar)
        self.add_widget(btn_add)

        btn_ver = Button(text="Ver Lista")
        btn_ver.bind(on_press=self.ver)
        self.add_widget(btn_ver)

        self.output = TextInput(readonly=True)
        self.add_widget(self.output)

    def adicionar(self, instance):
        try:
            nome, dias = self.input.text.split()
            dias = int(dias.replace("d", ""))

            restante = LIMITE - dias
            data_fim = datetime.now().date() + timedelta(days=restante)

            with open(ARQUIVO, "a") as f:
                f.write(nome + ";" + str(data_fim) + "\n")

            self.output.text = "Adicionado com sucesso!"
        except:
            self.output.text = "Erro! Use formato: Nome 12d"

    def ver(self, instance):
        if not os.path.exists(ARQUIVO):
            self.output.text = "Nenhum dado ainda"
            return

        hoje = datetime.now().date()
        texto = ""

        with open(ARQUIVO, "r") as f:
            for linha in f:
                nome, data = linha.strip().split(";")
                data = datetime.strptime(data, "%Y-%m-%d").date()
                restante = (data - hoje).days

                if restante >= 0:
                    texto += f"{nome} - {restante} dias restantes\n"
                else:
                    texto += f"{nome} - expirou ha {abs(restante)} dias\n"

        self.output.text = texto

class GuildaApp(App):
    def build(self):
        return Tela()

GuildaApp().run()
