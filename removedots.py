from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

def clean_number(number):
    return ''.join(char for char in number if char.isdigit())


class CleanNumberApp(App):
    def build(self):
        self.b = BoxLayout(orientation='vertical')

        self.label1 = Label(text='COLE O NÚMERO DO DOCUMENTO: ', font_size=16)
        self.b.add_widget(self.label1)

        self.textinput = TextInput(multiline=False, font_size=32)
        self.textinput.bind(on_text_validate=self.clean_and_copy)
        self.b.add_widget(self.textinput)

        self.label2 = Label(text='NÚMERO LIMPO: ', font_size=16)
        self.b.add_widget(self.label2)

        self.result = Label(text='', font_size=34)
        self.b.add_widget(self.result)

        self.button = Button(text='LIMPAR E COPIAR')
        self.button.bind(on_press=self.clean_and_copy)
        self.b.add_widget(self.button)
        self.button.background_color = [1, 1, 0, 1]


        return self.b
    

    def clean_and_copy(self, instance):
        raw_number = self.textinput.text
        cleaned_number = clean_number(raw_number)
        self.result.text = cleaned_number
        Clipboard.copy(self.result.text)

        # Change the button text and color
        self.button.text = "O NÚMERO LIMPO FOI COPIADO"
        self.button.background_color = [0, 1, 0, 1] # RGB and alpha ([R, G, B, A])



if __name__ == '__main__':
    CleanNumberApp().run()
