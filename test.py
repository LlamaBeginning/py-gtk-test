#!/usr/bin/env python
# based on http://python-gtk-3-tutorial.readthedocs.org/en/latest/introduction.html
# and other pages from that site

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LlamaBeginning test")
        self.set_border_width(12)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.button1 = Gtk.Button(label="This is a button")
        self.button1.connect("clicked", self.on_button1_clicked)
        vbox.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="This is also a button")
        self.button2.connect("clicked", self.on_button2_clicked)
        vbox.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Hello from button 2")

def main():
    window = MyWindow()
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
