#!/usr/bin/env python3

import gi
import os
import locale
import requests
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gio
from locale import gettext as tr

# Tərcümə məlumatları
APPNAME = "turan-session-logout"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Tərcümə funksiyaları
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)

# GTK Builder
builder = Gtk.Builder()
builder.set_translation_domain(APPNAME)
builder.add_from_file("/usr/share/turan/proqramlar/turan-session-logout/turan-session-logout.glade")

window = builder.get_object("window")
window.show_all()

class Handler():

    def shutdown(self, button):
        os.system("turan-session-logout shutdown")
        Gtk.main_quit()

    def reboot(self, button):
        os.system("turan-session-logout reboot")
        Gtk.main_quit()

    def logout(self, button):
        os.system("turan-session-logout logout")
        Gtk.main_quit()

    def suspend(self, button):
        os.system("turan-session-logout suspend")
        Gtk.main_quit()

    def on_exit(self, button):
        Gtk.main_quit()

builder.connect_signals(Handler())
Gtk.main()
