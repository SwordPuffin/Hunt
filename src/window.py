# window.py
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

import random, time
from gi.repository import Adw, Gtk, Gdk, Gio, GLib
from .resources import *

@Gtk.Template(resource_path='/io/github/swordpuffin/hunt/window.ui')
class HuntWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'HuntWindow'

    #All relevant items from window.ui that are used here
    grid = Gtk.Template.Child()
    frame = Gtk.Template.Child()
    frame_light = Gtk.Template.Child()
    custom_box = Gtk.Template.Child()
    clock = Gtk.Template.Child()
    small_game = Gtk.Template.Child()
    medium_game = Gtk.Template.Child()
    large_game = Gtk.Template.Child()
    custom_start_button = Gtk.Template.Child()
    words_value = Gtk.Template.Child()
    height_value = Gtk.Template.Child()
    length_value = Gtk.Template.Child()
    time_value = Gtk.Template.Child()
    category_list = Gtk.Template.Child()
    search_entry = Gtk.Template.Child()
    active_category = Gtk.Template.Child()
    main_window_content = Gtk.Template.Child()
    sidebar_view = Gtk.Template.Child()
    theme_selector = Gtk.Template.Child()
    jumble_category = Gtk.Template.Child()
    game_selector = Gtk.Template.Child()
    custom_settings = Gtk.Template.Child()
    recommended_settings = Gtk.Template.Child()
    gamemode = Gtk.Template.Child()
    gamemode_timed = Gtk.Template.Child()
    gamemode_blitz = Gtk.Template.Child()
    gamemode_ar = Gtk.Template.Child()
    gamemode_timed_ar = Gtk.Template.Child()
    gamemode_blitz_ar = Gtk.Template.Child()
    timer_progBar = Gtk.Template.Child()
    game_title = Gtk.Template.Child()
    theme_mobile = Gtk.Template.Child()
    gamemode_mobile = Gtk.Template.Child()
    ingame_bottomSheet = Gtk.Template.Child()

    found_words = []
    words_left = []
    used_letters = []
    words = []
    word_buttons = []
    word_list = []
    copy_colors = []
    checkbuttons = []
    colors = ["red1", "red2", "red3", "orange3", "purple2", "blue1", "blue2", "blue3", "blue4", "blue5", "yellow1", "yellow2", "yellow3", "yellow4", "green1"]

    length = 10
    height = 10
    word_count = 3
    timer = 10
    saved_time = 10

    timed_game = False
    game_over = False
    blitz_game = False

    grid_data = None
    current_word = None
    timer_id = None
    key = None
    dialog = None
    divided_timer = None
    reference_time = None
    selected_categories = {"RANDOM"}

    def update_gamemode(self, checkbox, clock, timed_game, blitz_game, actionrow):
        if checkbox.get_active():
            self.game_mode(clock, timed_game, blitz_game)
            self.gamemode_mobile.set_subtitle(actionrow.get_title())
            self.gamemode_mobile.set_icon_name(actionrow.get_icon_name())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css.encode('utf-8')) #fetches the css from resources.py.
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

        self.small_game.set_title(_("\n<span size='x-large' weight='ultrabold'>8 × 8 grid</span>\n<b>5 words\n(30 seconds)</b>\n"))
        self.medium_game.set_title(_("\n<span size='x-large' weight='ultrabold'>12 × 12 grid</span>\n<b>8 words\n(60 seconds)</b>\n"))
        self.large_game.set_title(_("\n<span size='x-large' weight='ultrabold'>16 × 16 grid</span>\n<b>10 words\n(80 seconds)</b>\n"))
        self.custom_start_button.set_title(_("\n<span size='large' weight='ultrabold'>Custom</span>\n"))
        from .main import HuntApplication

        #Connect each button to its designated function
        HuntApplication.create_action(self, 'reload', self.reload)
        HuntApplication.create_action(self, 'custom', self.custom)
        HuntApplication.create_action(self, 'back', self.back)
        HuntApplication.create_action(self, 'custom_start', self.custom_start)
        HuntApplication.create_action(self, 'restart', self.back_to_main_menu)
        HuntApplication.create_action(self, 'hint', self.hint)
        self.small_game.connect("activated", self.start_game, _, 5, 8, 8, 30, 400, 400)
        self.medium_game.connect("activated", self.start_game, _, 8, 12, 12, 60, 600, 600)
        self.large_game.connect("activated", self.start_game, _, 10, 16, 16, 80, 800, 800)
        self.theme_selector.connect("toggled", lambda cb, cat="RANDOM": self.on_row_activated(cb, cat))
        self.jumble_category.connect("toggled", lambda cb, cat="JUMBLE": self.on_row_activated(cb, cat))
        self.gamemode.connect("toggled",  self.update_gamemode, False, False, False, self.gamemode_ar)
        self.gamemode_timed.connect("toggled", self.update_gamemode, True, True, False, self.gamemode_timed_ar)
        self.gamemode_blitz.connect("toggled",self.update_gamemode, True, False, True, self.gamemode_blitz_ar)
        self.main_window_content.connect("popped", lambda _, page: self.back_to_main_menu(None, None) if page.get_tag() == 'game' else None)

        for item in sorted(list(related_words.keys())):
            actionEntry = Adw.ActionRow(title=item.capitalize())
            listEntry = Gtk.ListBoxRow(selectable=False, child=actionEntry)

            checkbox = Gtk.CheckButton()
            # if(actionEntry.get_title().upper() in self.selected_categories):
            #     checkbox.set_active(True)
            # else:
            #     checkbox.set_active(False)
            self.checkbuttons.append(checkbox)
            actionEntry.add_suffix(checkbox)
            actionEntry.set_activatable_widget(checkbox)
            checkbox.connect("toggled", lambda cb, cat=item.upper(): self.on_row_activated(cb, cat))

            self.category_list.append(listEntry)
        self.category_list.connect("row-selected", lambda _, row: row.get_child().activate() if row else None)
        self.search_entry.connect("search-changed", self.list_changed)

    def list_changed(self, search_entry):
        query = search_entry.get_text().lower()

        # Filter the categories based on the query
        filtered_categories = filter(lambda c: query in c.lower(), related_words.keys())

        self.checkbuttons.clear()
        while(self.category_list.get_first_child() is not None):
            self.category_list.remove(self.category_list.get_first_child())

        for category in sorted(filtered_categories):
            actionEntry = Adw.ActionRow(title=category.capitalize())
            listEntry = Gtk.ListBoxRow(selectable=False, child=actionEntry)

            checkbox = Gtk.CheckButton()
            self.checkbuttons.append(checkbox)
            if(actionEntry.get_title().upper() in self.selected_categories):
                checkbox.set_active(True)
            else:
                checkbox.set_active(False)
            actionEntry.add_suffix(checkbox)
            actionEntry.set_activatable_widget(checkbox)
            checkbox.connect("toggled", lambda cb, cat=category.upper(): self.on_row_activated(cb, cat))

            self.category_list.append(listEntry)

    #Changes the active category depending on what row in self.category_list is selected
    def on_row_activated(self, cb, actionName):
        if(cb.get_active()):
            self.selected_categories.add(actionName.upper())
            if(actionName != "RANDOM" and actionName != "JUMBLE"):
                self.theme_selector.set_active(False); self.jumble_category.set_active(False)
        else:
            self.selected_categories.remove(actionName.upper())
        if(actionName == "RANDOM" and cb.get_active() or actionName == "JUMBLE" and cb.get_active()):
            for child in self.checkbuttons:
                child.set_active(False)
            self.selected_categories.clear()
            self.selected_categories.add(actionName)
        self.active_category.set_title(", ".join(item.capitalize() for item in self.selected_categories))

        # Display the number of selected categories if more than one in mobile mode
        self.theme_mobile.set_subtitle([item.capitalize() for item in self.selected_categories][0] if len(self.selected_categories) == 1 else f"{len(self.selected_categories)} selected")

    #restarts the game
    def reload(self, action, _):
        if(self.timed_game or self.blitz_game):
            GLib.Source.remove(self.timer_id)
            self.timer = self.saved_time
        self.found_words.clear(); self.used_letters.clear();
        self.make_grid("clicked", _)

    def game_mode(self, clock, timed_game, blitz_game):
        self.clock.set_visible(clock)
        self.timed_game = timed_game
        self.blitz_game = blitz_game

    #Small, medium, or large game grids
    def start_game(self, action, _, word_count, length, height, timer, grid_length, grid_width):
        self.word_count = word_count
        self.length = length
        self.height = height
        self.timer = self.saved_time = self.reference_time = timer
        self.timer_id = None
        self.make_grid("activate", _)
        self.grid.set_size_request(grid_length, grid_width)

    #Player wants a custom game, display the options menu
    def custom(self, action, _):
        self.game_selector.scroll_to(self.custom_settings, True)

    #Pull back from the custom game options menu to the main menu
    def back(self, action, _):
        self.game_selector.scroll_to(self.recommended_settings, True)

    #Start the game with the custom values set by the player in self.custom_box
    def custom_start(self, action, _):
        self.word_count = int(self.words_value.get_value())
        self.height = int(self.height_value.get_value())
        self.length = int(self.length_value.get_value())
        self.timer = self.saved_time  = self.reference_time = int(self.time_value.get_value())
        self.make_grid("activate", _)
        self.grid.set_size_request(400 + (self.length - 8) / 2 * 100, 400 + (self.height - 8) / 2 * 100)

    #Back from a running game to the main menu
    def back_to_main_menu(self, action, _):
        print("backtomainmenu")
        if(self.clock.is_visible()):
            GLib.Source.remove(self.timer_id)
        self.found_words.clear(); self.used_letters.clear()
        self.main_window_content.pop_to_tag("preferences")

    def hint(self, action, _):
        self.ingame_bottomSheet.set_open(False)
        used_button = random.choice(self.used_letters)
        used_button.add_css_class("shake")
        def remove_shake():
            used_button.remove_css_class("shake")
            return False
        GLib.timeout_add(350, remove_shake)

    #Function that is the timer of the game. Return false/return true ends or continues the function
    def update(self):
        if(self.timer_progBar.get_fraction() < 0.25):
            self.timer_progBar.remove_css_class("warning")
            self.timer_progBar.add_css_class("error")
        elif(self.timer_progBar.get_fraction() < 0.5):
            self.timer_progBar.add_css_class("warning")
        else:
            self.timer_progBar.remove_css_class("warning")
            self.timer_progBar.remove_css_class("error")

        if(self.timer <= 0.1 and self.grid.is_visible):
            self.clock.set_description("Timer ended!")
            self.end_dialogue(hasWon=False)
            return False
        else:
            self.timer -= 0.1
            self.clock.set_description(time.strftime("%H:%M:%S", time.gmtime(self.timer)) + f".{int((self.timer % 1) * 10)}")
            self.timer_progBar.set_fraction(self.timer / self.reference_time)
            return True

    #Main function that is the start of the game. As the name suggests, makes the grid for all the letters
    def make_grid(self, action, _):
        if(len(self.selected_categories) == 0):
            dialog = Adw.AlertDialog(
            heading='Warning',
            body='Please select at least one theme before playing!',
            close_response="ok"
            )
            dialog.add_response("ok", "_OK")
            dialog.set_response_enabled("ok", True)
            dialog.set_default_response("ok")
            dialog.present(self)
            dialog.get_child().add_css_class("warning")
            return
        self.game_over = False
        self.copy_colors = self.colors.copy()
        if(len(self.found_words) == 0): #Only run at game start, this is here because the blitz mode will call this function to rebuild the grid every time a player finds a new word
            if(not self.make_word_list()): return
            while(self.frame.get_first_child() is not None): #Clear the GTKListBox that is to the left of the grid, only on start of game (not when blitz refreshes grid)
                self.frame.remove(self.frame.get_first_child())
            if self.main_window_content.get_visible_page().get_tag() != "game":
                self.main_window_content.push_by_tag("game")

        if(self.timed_game and len(self.found_words) == 0 or self.blitz_game and len(self.found_words) == 0): #Create a timer only on first execution of timed or blitz games
            if(self.timer_id is not None): #Remove the active timer, as if the grid failed to generate, it would create multiple timers at once
                GLib.Source.remove(self.timer_id)
            self.timer_id = GLib.timeout_add(100, self.update)
            self.clock.set_visible(True)
            self.timer = self.saved_time
            if(self.blitz_game):
                self.divided_timer = self.timer / self.word_count
                self.timer = 0 #Reset timer so it will be equal to self.divided_timer on first execution

        self.grid.set_visible(True)
        if(len(self.key) > 1):
            self.game_title.set_subtitle(", ".join(item.capitalize() for item in self.key))
        else:
            self.game_title.set_subtitle(self.key[0].capitalize())
        while(self.grid.get_child_at(0,0) is not None): #Clear the entire main grid where all the letters are
            self.grid.remove_row(0)

        row = 0
        col = 0
        self.buttons = []

        import os
        locale = os.environ.get("LANG", "C") #Grabs the system language

        #Use the correct alphabet for the user's language
        if(locale not in letters.keys()):
            if(locale in ["fr_BE.UTF-8", "fr_CA.UTF-8", "fr_CH.UTF-8", "fr_LU.UTF-8"]): #Change other types of French to standard French
                locale = "fr_FR.UTF-8"
            else:
                locale = "en_US.UTF-8" #defaults to English if not defined in resources.py
        for i in range(1, self.length * self.height + 1): #Generate the grid with all the buttons in it
            button = Gtk.Button(hexpand=True, vexpand=True, width_request=12, height_request=12, label=random.choice(letters[locale]))
            self.grid.attach(button, col, row, 1, 1)
            self.buttons.append(button)
            self.grid.add_css_class("frame")
            button.add_css_class("flat")
            button.connect("clicked", self.letter_selected, _, button)

            motion_controller = Gtk.EventControllerMotion() #Uses an event controller for when is hovering over buttons on the grid when they have selected their first letter
            motion_controller.connect("enter", self.on_button_hovered)
            button.add_controller(motion_controller)

            col += 1
            if(i % self.length == 0):
                col = 0
                row += 1

        self.refresh_lightlist()

        if(not self.blitz_game):
            #Add each word the the GTKListBox, and place each word in the grid. Does not run in blitz mode because only one word needs to be in the grid and in the GTKListBox at a time
            used_words = set()
            for word in self.words:
                label = Gtk.Label(label=word, margin_bottom=14, margin_top=14)
                used_words.add(label.get_label())
                #This is needed because sometimes words would be added to self.frame that are not in self.words, or words that are in self.frame are placed in multiple times
                #Occurs with words that fail to be placed
                if(label.get_label().lower() in self.word_list and all(child.get_first_child().get_title().upper() != label.get_label() for child in self.frame)):
                    self.place_word_in_grid(word)
        else: #Add self.divided_timer to however much it was before, and place the one new word into the grid as well as onto the GTKListBox.
            self.timer += self.divided_timer
            self.reference_time = self.timer
            self.clock.set_description(str(round(self.timer, 1)) + " seconds")
            self.place_word_in_grid(self.words[len(self.found_words)])

    def add_item_to_sidebar(self, word):
        checkbutton = Gtk.CheckButton(visible=False)
        actionRow = Adw.ActionRow(title=word.capitalize())
        listbox = Gtk.ListBoxRow(selectable=False, activatable=False, child=actionRow)
        actionRow.add_suffix(checkbutton)
        self.frame.append(listbox)

    def make_word_list(self): #Creates the list of words for the player to search for.
        self.words.clear()
        self.words_left.clear()
        if("RANDOM" in self.selected_categories):
            self.key = [random.choice(list(related_words.keys()))]
            self.word_list = related_words[self.key[0]]
        elif("JUMBLE" in self.selected_categories):
            self.key = [(_("Jumble"))]
            for i in range(10):
                self.word_list.append(random.choice(related_words[random.choice(list(related_words.keys()))]))
        else:
            self.word_list = []
            for item in self.selected_categories:
                if related_words[item] not in self.word_list:
                    self.word_list += related_words[item]
            self.key = list(self.selected_categories) #For the end dialog when stating the category
        self.grid_data = [[' ' for _ in range(self.length)] for _ in range(self.height)]
        self.word_list = list(set(self.word_list)) #Kind of stupid, but removes all the duplicate words if there are two or more active themes and they have a few in common
        random.shuffle(self.word_list)
        for i in range(len(self.word_list)):
            if(len(self.word_list[i]) > self.length or len(self.word_list[i]) > self.height):
                print(self.word_list[i])
                continue
            newWord = self.word_list[i].upper()
            self.words.append(newWord)
            self.words_left.append(newWord)
        del self.words[self.word_count:]; del self.words_left[self.word_count:]
        if(len(self.words) < self.word_count):
            if("RANDOM" in self.selected_categories or "Jumble" in self.selected_categories):
                print("error placing word: " + str(self.key))
                self.make_grid("activate", _)
                return False
            else:
                self.back_to_main_menu("activate", _)
            dialog = Adw.AlertDialog(
            heading=_('Error :('),
            body=_('\nUnable to place all the words in the selected theme!\n\n   Try selecting a larger grid or a different category.   \n\nSorry for the inconvenience\n'),
            close_response="ok"
            )
            dialog.add_response("ok", "_OK")
            dialog.set_response_enabled("ok", True)  # Ensure OK button is enabled
            dialog.set_default_response("ok")
            dialog.present(self)
            dialog.get_child().add_css_class("error")
            return False
        return True

    # Places the words in self.words into the grid in random places and in random directions
    def place_word_in_grid(self, word):
        placed = False
        attempts = 0
        max_attempts = 200  # Maximum attempts to prevent infinite loop

        while(not placed and attempts < max_attempts):
            attempts += 1
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            backward = random.choice([False, False, False, True])  # Randomly decide if word should be placed backwards. Only 1/3rd chance since half of all words being backwards is too much

            if(direction == 'diagonal'):
                diagonal_up = random.choice([True, False])  # Randomly decide if diagonal should go upwards

            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.length - 1)
            word_to_place = word[::-1] if backward else word  # Reverse word if placing backwards
            # Check horizontal placement
            if(direction == 'horizontal'):
                if(backward):
                    col -= len(word) - 1  # Adjust start position for backward placement
                if(0 <= col and col + len(word) <= self.length):
                    if all(self.grid_data[row][col + i] in [' ', word_to_place[i].upper()] for i in range(len(word))):
                        for i in range(len(word)):
                            self.grid_data[row][col + i] = word_to_place[i].upper()
                            self.buttons[row * self.length + col + i].set_label(word_to_place[i].upper())
                            self.used_letters.append(self.buttons[row * self.length + col + i])
                        placed = True; self.add_item_to_sidebar(word)
            # Check vertical placement
            elif(direction == 'vertical'):
                if(backward):
                    row -= len(word) - 1
                if(0 <= row and row + len(word) <= self.height):
                    if(all(self.grid_data[row + i][col] in [' ', word_to_place[i].upper()] for i in range(len(word)))):
                        for i in range(len(word)):
                            self.grid_data[row + i][col] = word_to_place[i].upper()
                            self.buttons[(row + i) * self.length + col].set_label(word_to_place[i].upper())
                            self.used_letters.append(self.buttons[(row + i) * self.length + col])
                        placed = True; self.add_item_to_sidebar(word)
            # Check diagonal placement
            elif(direction == 'diagonal'):
                if(diagonal_up):
                    if(row - (len(word) - 1) >= 0 and col + len(word) <= self.length):  # Ensure row stays within bounds
                        if(all(self.grid_data[row - i][col + i] in [' ', word_to_place[i].upper()] for i in range(len(word)))):
                            for i in range(len(word)):
                                self.grid_data[row - i][col + i] = word_to_place[i].upper()
                                self.buttons[(row - i) * self.length + (col + i)].set_label(word_to_place[i].upper())
                                self.used_letters.append(self.buttons[(row - i) * self.length + (col + i)])
                            placed = True; self.add_item_to_sidebar(word)
                else:
                    if(0 <= row and row + len(word) <= self.height and col + len(word) <= self.length):
                        if(all(self.grid_data[row + i][col + i] in [' ', word_to_place[i].upper()] for i in range(len(word)))):
                            for i in range(len(word)):
                                self.grid_data[row + i][col + i] = word_to_place[i].upper()
                                self.buttons[(row + i) * self.length + (col + i)].set_label(word_to_place[i].upper())
                                self.used_letters.append(self.buttons[(row + i) * self.length + (col + i)])
                            placed = True; self.add_item_to_sidebar(word)
        if(not placed):
            print(f"Failed to place word '{word}' after {max_attempts} attempts.")
            self.make_grid("activate", _)

    def refresh_lightlist(self):
        self.frame_light.remove_row(0)

        def generate_new_entry(word, empty=False):
            label = Gtk.Label(label=word, css_classes=(["dim-label"] if empty else None), use_markup=empty)
            box = Gtk.Box(css_classes=(['tag'] if not empty else None))
            box.append(label)
            return box

        if len(self.words_left) > 0:
            max_words = len(self.words_left)

            if self.blitz_game:
                max_words = 1
                if self.frame_light.get_halign() != Gtk.Align.CENTER: self.frame_light.set_halign(Gtk.Align.CENTER)
            else:
                if self.frame_light.get_halign() != Gtk.Align.START: self.frame_light.set_halign(Gtk.Align.START)

            for i in range(0, max_words):
                self.frame_light.attach(generate_new_entry(self.words_left[i].capitalize()),i, 0, 1, 1)
        else:
            self.frame_light.attach(generate_new_entry("<i>No words left</i>", True), 0, 0, 1, 1)
            if self.frame_light.get_halign() != Gtk.Align.CENTER: self.frame_light.set_halign(Gtk.Align.CENTER)

    #Fetches the word in between the two selected buttons. Also checks if the word that is made is one of words the player is supposed to find
    def letter_selected(self, action, _, button):
        if(not self.current_word and self.game_over == False):
            self.ingame_bottomSheet.set_open(False) # Close BottomSheet when letter pressed
            self.current_word = button
            button.add_css_class("green_button")
        elif(self.current_word and self.game_over == False):
            first_pos = self.grid.query_child(self.current_word) #Grab the position of the first selected button
            second_pos = self.grid.query_child(button) #Grab the position of the second selected button
            word = self.get_selected_word(first_pos, second_pos) #Find the word between the two
            if(word[::-1] in self.words and word[::-1] not in self.found_words):
                word = word[::-1]
            if(word in self.words and word not in self.found_words):
                for child in self.frame:
                    if(child.get_first_child().get_title().upper() == word):
                        child.get_first_child().add_css_class("success")
                        child.get_first_child().set_sensitive(False)
                        child.get_first_child().set_title(f"<s>{child.get_first_child().get_title()}</s>")

                        checkIcon = Gtk.CheckButton(active=True)
                        checkIcon.add_css_class("selection-mode")
                        child.get_first_child().add_suffix(checkIcon)
                color = random.choice(self.copy_colors)
                self.words_left.remove(word)
                self.refresh_lightlist()
                self.copy_colors.remove(color)
                for child in self.word_buttons:
                    if(child in self.used_letters):
                        self.used_letters.remove(child)
                    child.remove_css_class("green_button")
                    child.add_css_class(f"{color}")
                    for css_classes in child.get_css_classes():
                        # Remove the color class if it is at an intersection point to that it always uses the most recently added color, sometimes it ignores the newer color.
                        if(css_classes in self.colors and css_classes != color):
                            child.add_css_class("outline-" + css_classes); child.remove_css_class(f"{css_classes}")
                self.found_words.append(word)
                if(len(self.found_words) == self.word_count): #End the game if the player has found all the words
                    self.end_dialogue(hasWon=True)
                    return
                if(self.blitz_game):
                    self.make_grid("activate", _)
            else:
                self.current_word.remove_css_class("green_button")
                for child in self.word_buttons:
                    child.remove_css_class("green_button")
            self.current_word = None

    #This function runs when the player selects two letters, and then creates the word from their location
    def get_selected_word(self, first_pos, second_pos):
        row1, col1 = first_pos[1], first_pos[0]
        row2, col2 = second_pos[1], second_pos[0]
        row_min, row_max = sorted([row1, row2])
        col_min, col_max = sorted([col1, col2])
        self.word_buttons.clear()
        word = ""

        #If the selected buttons are in the same row
        if(row1 == row2):
            for col in range(col_min, col_max + 1):
                child = self.grid.get_child_at(col, row1)
                if(child):
                    child.add_css_class("green_button")
                    self.word_buttons.append(child)
                    word += child.get_label()
        #If the two selected buttons are in the same column
        elif(col1 == col2):
            for row in range(row_min, row_max + 1):
                child = self.grid.get_child_at(col1, row)
                if(child):
                    child.add_css_class("green_button")
                    self.word_buttons.append(child)
                    word += child.get_label()
        #If the two selected buttons are diagonal to eachother
        elif(abs(row1 - row2) == abs(col1 - col2)):
            row_step = 1 if row2 > row1 else -1
            col_step = 1 if col2 > col1 else -1
            for step in range(abs(row2 - row1) + 1):
                child = self.grid.get_child_at(col1 + step * col_step, row1 + step * row_step)
                if(child):
                    child.add_css_class("green_button")
                    self.word_buttons.append(child)
                    word += child.get_label()
        return word


    def on_button_hovered(self, controller, event, _):
        if(not self.current_word):
            return

        hovered_button = controller.get_widget()
        first_pos = self.grid.query_child(self.current_word)
        second_pos = self.grid.query_child(hovered_button)

        if(not first_pos or not second_pos):
            return

        for button in self.word_buttons:
            if(button is not self.current_word):
                button.remove_css_class("green_button")

        path_buttons = self.get_path_buttons(first_pos, second_pos)

        # Highlight the path
        for button in path_buttons:
            button.add_css_class("green_button")
            self.word_buttons.append(button)

    #Grab all the buttons between the two selected ones
    def get_path_buttons(self, first_pos, second_pos):
        row1, col1 = first_pos[1], first_pos[0]
        row2, col2 = second_pos[1], second_pos[0]
        row_min, row_max = sorted([row1, row2])
        col_min, col_max = sorted([col1, col2])
        path_buttons = []

        # Horizontal path
        if(row1 == row2):
            for col in range(col_min, col_max + 1):
                button = self.grid.get_child_at(col, row1)
                if(button):
                    path_buttons.append(button)
        # Vertical path
        elif(col1 == col2):
            for row in range(row_min, row_max + 1):
                button = self.grid.get_child_at(col1, row)
                if(button):
                    path_buttons.append(button)
        # Diagonal path
        elif(abs(row1 - row2) == abs(col1 - col2)):
            row_step = 1 if row2 > row1 else - 1 #Either moves upwards or downwards depending on the difference in location
            col_step = 1 if col2 > col1 else - 1
            for step in range(abs(row2 - row1) + 1):
                button = self.grid.get_child_at(col1 + step * col_step, row1 + step * row_step) #I don't understand how this works, but it does
                if(button):
                    path_buttons.append(button)

        return path_buttons

    #Dialog that runs when the player has found all the words or run out of time.
    def end_dialogue(self, hasWon=False):
        self.game_over = True
        #If the player back_to_main_menus the game, self.current_word gets set to the first button and returns errors. Don't know why it happens, so this is the fix ¯\_(ツ)_/¯
        self.current_word = None
        if(self.clock.is_visible()):
            GLib.Source.remove(self.timer_id)
            self.divided_timer = None

        endDialog_obj = EndDialog(self.key, f"{self.length} ⨯ {self.height}", len(self.found_words), self.word_count, hasWon)
        endDialog_obj.set_actions(self.close_end_dialogue, self.back_to_main_menu_game)
        endDialog_obj.present(self)

        self.found_words.clear(); self.used_letters.clear()

    #back_to_main_menu the game when it ends
    def back_to_main_menu_game(self):
        self.make_grid("activate", _)

    #Destroy the dialogue so that the player can see the grid
    def close_end_dialogue(self):
        self.main_window_content.pop()

@Gtk.Template(resource_path='/io/github/swordpuffin/hunt/end_dialog.ui')
class EndDialog(Adw.AlertDialog):
    __gtype_name__ = 'EndGame'

    #All relevant items from window.ui that are used here
    category = Gtk.Template.Child()
    grid_size = Gtk.Template.Child()
    progress = Gtk.Template.Child()
    words_found = Gtk.Template.Child()

    def __init__(self, categoryName: str, gridSize: str, wordsFound: int, wordsTotal: int, hasWon: bool = False, **kwargs):
        super().__init__(**kwargs)
        if(hasWon):
            self.set_body(_("Congratulations!"))
            self.set_heading(_("You won the game!"))
            self.add_css_class('success')
        else:
            self.set_body(_("Time's out!"))
            self.set_heading(_("You ran out of time!"))
            self.add_css_class('warning')

        self.category.set_subtitle(", ".join(item.capitalize() for item in categoryName))
        self.grid_size.set_subtitle(gridSize)
        self.words_found.set_subtitle(f"{wordsFound} out of {wordsTotal}")
        self.progress.set_fraction(wordsFound/wordsTotal)
        self.connect("response", self.end_dialog_callback)

    def set_actions(self, closeAction: callable, newGameAction: callable):
        self.newGameAction = newGameAction
        self.closeAction = closeAction

    def end_dialog_callback(self, EndGameDialog: Adw.AlertDialog, responseID: str):
        if responseID == 'newgame':
            self.newGameAction()
        else:
            self.closeAction()
