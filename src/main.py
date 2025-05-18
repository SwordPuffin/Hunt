# main.py
#
# Copyright 2025 Nathan Perlman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys, gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import HuntWindow

class HuntApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='io.github.swordpuffin.hunt',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('help', self.help_action, ['<primary>h'])

    def do_activate(self):
        win = self.props.active_window
        if(not win):
            win = HuntWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        about = Adw.AboutDialog(application_name='Hunt',
                                application_icon='io.github.swordpuffin.hunt',
                                developer_name='Nathan Perlman',
                                version='1.1.4',
                                issue_url='https://github.com/SwordPuffin/Hunt/issues',
                                developers=['Nathan Perlman', 'DodoLeDev'],
                                copyright='© 2025 Nathan Perlman')
        about.present(self.props.active_window)

    def help_action(self, *args):
        builder = Gtk.Builder().new_from_resource('/io/github/swordpuffin/hunt/help_dialog.ui')
        help_dialog = builder.get_object("HelpDialog")
        help_dialog.present(parent=self.props.active_window)

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if(shortcuts):
            self.set_accels_for_action(f"app.{name}", shortcuts)

def main(version):
    app = HuntApplication()
    return app.run(sys.argv)
