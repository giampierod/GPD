""" 
Copyright (c) 2013 Giampiero De Ciantis <gdeciantis@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in the 
Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
"""

from datetime import datetime
import time
import threading
import sublime, sublime_plugin

targetView = None

def prepare_view(view, note_time, todo_str):
    edit = view.begin_edit()
    note_header = "//{0}//".format(note_time)
    note_footer = "//End//"
    note_boiler_str = "{0}\n    {1}\n    \n{2}\n".format(note_header, todo_str,note_footer)
    boiler_length = view.insert(edit, 0, note_boiler_str)
    boiler_region = sublime.Region(boiler_length - (len(note_footer) + 2), boiler_length - (len(note_footer) + 2))
    view.sel().clear()
    view.sel().add(boiler_region)
    view.show(boiler_region)
    view.end_edit(edit)

class OpenNoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        note_time = datetime.now().strftime("%Y.%m.%d.%H.%M")
        cur_line = self.view.full_line(self.view.sel()[0].begin())
        self.view.insert(edit, cur_line.end() - 1, " `({0})".format(note_time))
        todo_str = self.view.substr(cur_line).strip()
        LoadListener.target_filename = note_view.file_name()
        LoadListener.note_time = note_time
        LoadListener.todo_str = todo_str
        note_view = self.view.window().open_file(self.view.file_name() + "_Note")
        
class LoadListener(sublime_plugin.EventListener):
    target_filename = ""
    note_time = ""
    todo_str = ""

    def on_load(self, view):
        if view.file_name() == LoadListener.target_filename:
            prepare_view(view, LoadListener.note_time, LoadListener.todo_str)
            LoadListener.target_filename = ""
            LoadListener.note_time = ""
            LoadListener.todo_str = ""