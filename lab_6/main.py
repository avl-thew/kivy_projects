from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


class CalculatorApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')
        
        self.result = TextInput(multiline=False, readonly=True, 
                                halign="right", font_size=50)
        self.main_layout.add_widget(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.main_layout.add_widget(h_layout)

        equal_btn = Button(text="=", font_size=40)
        equal_btn.bind(on_press=self.on_equal_press)
        self.main_layout.add_widget(equal_btn)

        return self.main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text
        
        if button_text == "C":
            self.result.text = ""
        else:
            self.result.text = current + button_text

    def on_equal_press(self, instance):
        try:
            self.result.text = str(eval(self.result.text))
        except:
            self.result.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()