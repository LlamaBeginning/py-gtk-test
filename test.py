#!/usr/bin/env python
# based on http://python-gtk-3-tutorial.readthedocs.org/en/latest/introduction.html

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LlamaBeginning test")

        self.button = Gtk.Button(label="This is a button")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello")

def main():
    window = MyWindow()
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
