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

        self.button_clean_copy = Button(text='LIMPAR E COPIAR')
        self.button_clean_copy.bind(on_press=self.clean_and_copy)
        self.b.add_widget(self.button_clean_copy)
        self.button_clean_copy.background_color = [1, 1, 1, 1]

        self.button_reset = Button(text='RESET', background_color=[1, 0, 0, 1])
        self.button_reset.bind(on_press=self.reset)
        self.b.add_widget(self.button_reset)


        return self.b
    

    def clean_and_copy(self, instance):
        raw_number = self.textinput.text
        cleaned_number = clean_number(raw_number)
        self.result.text = cleaned_number
        Clipboard.copy(self.result.text)

        # Change the button text and color
        self.button_clean_copy.text = "O NÚMERO LIMPO FOI COPIADO"
        self.button_clean_copy.background_color = [0, 1, 0, 1] # RGB and alpha ([R, G, B, A])


    def reset(self, instance):
        self.textinput.text = ''
        self.result.text = ''
        self.button_clean_copy.text = 'LIMPAR E COPIAR'
        self.button_clean_copy.background_color = [1, 1, 1, 1]


if __name__ == '__main__':
    CleanNumberApp().run()
