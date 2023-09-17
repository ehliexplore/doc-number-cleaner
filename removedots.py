from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

def clean_number(number):
    return ''.join(char for char in number if char.isdigit())


class CleanNumberApp(App):
    def build(self):
        self.b = BoxLayout(orientation='vertical')

        self.label1 = Label(text='Enter the document number: ')
        self.b.add_widget(self.label1)

        self.textinput = TextInput(multiline=False)
        self.b.add_widget(self.textinput)

        self.label2 = Label(text='Cleaned Number: ')
        self.b.add_widget(self.label2)

        self.result = Label(text='', font_size=32)
        self.b.add_widget(self.result)

        self.button = Button(text='Clean Number')
        self.button.bind(on_press=self.clean)
        self.b.add_widget(self.button)

        return self.b
    
    def clean(self, instance):
        raw_number = self.textinput.text
        cleaned_number = clean_number(raw_number)
        self.result.text = cleaned_number

if __name__ == '__main__':
    CleanNumberApp().run()
