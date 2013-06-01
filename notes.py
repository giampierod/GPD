"""
Copyright (c) 2013 Giampiero De Ciantis <gdeciantis@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import datetime
import time
import threading
import sublime
import sublime_plugin
import re
from todos import is_header


# Create a new note section with boilerplate text in the view supplied
def create_note(view, note_time, todo_str):
    edit = view.begin_edit()
    note_header = "//{0}//\n".format(note_time)
    note_footer = "//End//\n\n"
    note_boiler_str = ("%s    %s\n\n    \n%s" %
                      (note_header, todo_str, note_footer))
    boiler_length = view.insert(edit, 0, note_boiler_str)
    boiler_region = sublime.Region(boiler_length - len(note_footer) - 1,
                                   boiler_length - len(note_footer) - 1)
    highlight_note(view, sublime.Region(0, boiler_length - 1), boiler_region)
    view.end_edit(edit)


# The pattern for a note header
def note_header_pattern():
    return '`\((.*)\)'


# Fold the other notes, and unfold the selected not so the user can focus
# on the note they are working on.
def highlight_note(view, note_region, end_of_note):
    view.sel().clear()
    view.sel().add(end_of_note)
    view.show(end_of_note)
    view.fold(sublime.Region(0, note_region.a))
    view.unfold(note_region)
    view.fold(sublime.Region(note_region.b, view.size() - 1))
    

# Find a note with the given header_text in the view
def find_note_header(view, header_text):
    search = view.find("//{0}//".format(header_text), 0)
    if search is not None:
        note_header = view.full_line(search)
        note_footer = view.full_line(view.find("//End//", note_header.b))
        end_of_note = note_footer.a - 1
        note_region = note_header.cover(note_footer)
        highlight_note(view, note_region, end_of_note)        
        return True
    else:
        return False


def note_exists(view, cur_line):
    first_note = view.find(note_header_pattern(), cur_line.a,
                           sublime.IGNORECASE)
    if first_note is not None:
        return cur_line.contains(first_note)
    else:
        return False


def open_note_file(view):
    return view.window().open_file(view.file_name() + "_Note")


class OpenTodoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()[:-len("_Note")]
        self.view.window().open_file(filename)


class OpenNoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        NoteLoadListener._clear()
        note_time = datetime.now().strftime("%Y.%m.%d.%H.%M")
        cur_line = self.view.full_line(self.view.sel()[0].begin())
        todo_str = self.view.substr(cur_line).strip()

        if is_header(todo_str):
            return
        elif note_exists(self.view, cur_line):
            first_note = self.view.find(note_header_pattern(), cur_line.a,
                                        sublime.IGNORECASE)
            m = re.search(note_header_pattern(), self.view.substr(first_note))
            inner_note = m.group(1)
            todo_str_min = todo_str.replace(m.group(0), "").strip()
            note_view = open_note_file(self.view)
            # This should be while note_view.is_loading() with a sleep
            # Sublime 3 should fix the issue with multi-threading
            if note_view.is_loading():
                NoteLoadListener._set_attr(note_view.file_name(),
                                  inner_note,
                                  todo_str_min,
                                  True)
            elif not find_note_header(note_view, inner_note):
                create_note(note_view, inner_note, todo_str_min)
        else:
            self.view.insert(edit, cur_line.end() - 1,
                             " `({0})".format(note_time))
            note_view = open_note_file(self.view)
            if note_view.is_loading():
                NoteLoadListener._set_attr(note_view.file_name(), note_time,
                                  todo_str, False)
            else:
                create_note(note_view, note_time, todo_str)

# This workaround will be gone in Sublime 3
class NoteLoadListener(sublime_plugin.EventListener):
    target_filename = ""
    header_str = ""
    todo_str = ""
    note_exists = False

    @staticmethod
    def _set_attr(filename, section, todo, exists):
        NoteLoadListener.target_filename = filename
        NoteLoadListener.header_str = section
        NoteLoadListener.todo_str = todo
        NoteLoadListener.note_exists = exists

    @staticmethod
    def _clear():
        NoteLoadListener._set_attr("", "", "", False)

    def on_load(self, view):
        if note_exists and find_note_header(view, NoteLoadListener.header_str):
            pass
        elif view.file_name() == NoteLoadListener.target_filename:
            create_note(view, NoteLoadListener.header_str, NoteLoadListener.todo_str)
            NoteLoadListener.target_filename = ""
            NoteLoadListener.header_str = ""
            NoteLoadListener.todo_str = ""
