"""
CP1404/CP5632 Practical - Dynamic Labels example
Creating labels dynamically from a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app with list of names."""
        super().__init__(**kwargs)
        # List of names to display as labels
        self.names = ["AAA", "BBB", "CCC", "DDD"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from name list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.font_size = '24sp'
            temp_label.color = (1, 1, 1, 1)
            # Add the label to the main layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()