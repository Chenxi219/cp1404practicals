from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from data and add them to the GUI."""
        for name in names:
            name_label = Label(text=name)
            self.root.add_widget(name_label)


DynamicLabelsApp().run()