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

import datetime, getpass
import sublime, sublime_plugin
import re

def TODO_HEADER_STRING(): 
    return "//Todo//"

def CLOSED_HEADER_STRING():
    return "//Closed//"

def TODAY_HEADER_STRING():
    return "//Today//"

def FOOTER_STRING():
    return "//End//"

def is_header(text):
    return re.match("//(.*)//", text)

def move_todo_to_section(section, view, edit, prefix=""):
    cur_line = view.full_line(view.sel()[0].begin())
    if not is_header(view.substr(cur_line).strip()):
        header_string = "//" + section + "//"
        header_top = view.find(header_string, 0)
        todo = "    " + prefix + view.substr(cur_line).strip()
        if header_top.b < cur_line.a:
            view.erase(edit, cur_line)
            view.insert(edit, header_top.b, "\n" + todo)        
        else:
            view.insert(edit, header_top.b, "\n" + todo)
            view.erase(edit, cur_line)
    else:
        sublime.status_message("Can't move section marker.")

def add_to_todo(view, edit):
    cur_line = view.full_line(view.sel()[0].begin())
    if not is_header(view.substr(cur_line).strip()):        
        todo_top = view.find(TODO_HEADER_STRING(), 0)
        todo_bottom = view.find(FOOTER_STRING(), todo_top.b)
        todo = re.sub("\$\([a-zA-Z0-9_ ]*\)[ ]?", '', view.substr(cur_line).rstrip())
        view.insert(edit, todo_bottom.a - 1, "\n" + todo)
    else:
        sublime.status_message("Can't move section marker.")

def close_todo(view, edit):
    closed_time = "~(" + datetime.datetime.now().strftime("%d/%m/%y %H:%M") + ") "
    move_todo_to_section("Closed", view, edit, closed_time)

class SelectTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		move_todo_to_section("Today", self.view, edit)

class DoneTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit): close_todo(self.view, edit)

class DoneTodoRepeatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        add_to_todo(self.view, edit)
        close_todo(self.view, edit)

class NewTodoCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        todo_top = self.view.find(TODO_HEADER_STRING(),0)
        todo_bottom = self.view.find(FOOTER_STRING(), todo_top.b)
        inserted_length = self.view.insert(edit, todo_bottom.a - 1, "\n" + "    ") - 1
        cur_todo_pt = self.view.rowcol(todo_bottom.a)
        new_todo_pt = self.view.text_point(cur_todo_pt[0], cur_todo_pt[1] + inserted_length)
        self.view.sel().clear()
        self.view.sel().add(new_todo_pt)
        self.view.show(new_todo_pt)
        

def increment_seconds():
    if sublime.todo_timer_time is not None:
        td = datetime.datetime.now() - sublime.todo_timer_time
        sublime.todo_timer_seconds += (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6


def write_time(self, edit):
    has_run = hasattr(sublime, 'todo_timer_seconds')
    if has_run is False or (has_run and sublime.todo_timer_seconds == 0):
        sublime.status_message('todo timer not running')
        return

    seconds = sublime.todo_timer_seconds

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    output = []
    output.append('%ih' % hours)
    output.append('%im' % minutes)
    output.append('%is' % seconds)

    cur_line = self.view.line(self.view.sel()[0].begin())
    line_string = self.view.substr(cur_line).strip()
    self.view.replace(edit, cur_line, "	" + line_string + " " + "$(" + ' '.join(output) + ")")

class TodoTimerStartCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        if not hasattr(sublime, 'todo_timer_seconds'):
            sublime.todo_timer_seconds = 0
        sublime.todo_timer_time = datetime.datetime.now()


class TodoTimerPauseCommand(sublime_plugin.ApplicationCommand):
    """A sublime text command to pause the timer"""
    def run(self):
        try:
            increment_seconds()

            report_time()

            sublime.todo_timer_time = None

        except:
            sublime.status_message("todo timer not running")


class TodoTimerStopCommand(sublime_plugin.TextCommand):
    """A sublime text command to stop the timer"""
    def run(self, edit):
        increment_seconds()

        write_time(self, edit)

        sublime.todo_timer_seconds = 0
        sublime.todo_timer_time = None