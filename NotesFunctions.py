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

import datetime
import sublime, sublime_plugin

class NewNoteCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        note_time = "`(" + datetime.datetime.now().strftime("%y.%m.%d.%H.%M") + ")"
        cur_line = self.view.full_line(self.view.sel()[0].begin())
        todo_str = self.view.substr(cur_line).strip()
        self.view.insert(edit, cur_line.end() - 1, " " + note_time)
        note_view = self.view.window().open_file(self.view.file_name() + "_Note")
        boiler_length = note_view.insert(edit, 0, note_time + " - " + todo_str + "\n" + "    \n")
        boiler_region = sublime.Region(boiler_length - 1, boiler_length - 1)
        note_view.sel().clear()
        note_view.sel().add(boiler_region)
        note_view.show(boiler_region)

        
