import datetime, getpass
import sublime, sublime_plugin
import re

def is_header(text):
    return re.match("//(.*)//", text)

def move_todo_to_section(section, self, edit, prefix=""):
    cur_line = self.view.full_line(self.view.sel()[0].begin())
    if not is_header(self.view.substr(cur_line).strip()):
        header_string = "//" + section + "//"
        header_top = self.view.find(header_string, 0)
        todo = "    " + prefix + self.view.substr(cur_line).strip()
        if header_top.b < cur_line.a:
            self.view.erase(edit, cur_line)
            self.view.insert(edit, header_top.b, "\n" + todo)        
        else:
            self.view.insert(edit, header_top.b, "\n" + todo)
            self.view.erase(edit, cur_line)
    else:
        sublime.status_message("Can't move section marker.")

def add_to_todo(self, edit):
    cur_line = self.view.full_line(self.view.sel()[0].begin())
    if not is_header(self.view.substr(cur_line).strip()):
        todo_header_string = "//Todo//"
        todo_footer_string = "//End//"
        todo_top = self.view.find(todo_header_string, 0)
        todo_bottom = self.view.find(todo_footer_string, todo_top.b)
        todo = re.sub("\$\([a-zA-Z0-9_ ]*\)[ ]?", '', self.view.substr(cur_line).rstrip())
        self.view.insert(edit, todo_bottom.a - 1, "\n" + todo)
    else:
        sublime.status_message("Can't move section marker.")

def close_todo(self, edit):
    closed_time = "~(" + datetime.datetime.now().strftime("%d/%m/%y %H:%M") + ") "
    move_todo_to_section("Closed", self, edit, closed_time)

class SelectTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		move_todo_to_section("Today", self, edit)

class DoneTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit): close_todo(self, edit)

class DoneTodoRepeatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        add_to_todo(self, edit)
        close_todo(self, edit)
        

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


