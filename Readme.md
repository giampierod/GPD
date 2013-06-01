###About the GPD System

The GPD system is meant for people who spend a great deal of time text editing. It is a Todo app with the power of GTD and Mark Forster's Final Version, but the simplicity of writing a final. Except for Section headers every line is a todo item. Special symbols allow you to understand different aspects of the todo item. Using combinations of regular and symbolized everything is free form, with the ability to understand general organization. I doubt this tool is for everyone, but I find it quite useful.

###Pre-Requisites

To install GPD, you first need to install Sublime Text 2 (http://www.sublimetext.com/). This a great application for editing text and supports Linux, Mac, and Windows equally well. 

Once you got Sublime Text 2 up and running there two methods of installing GPD.

###Instal Method 1 - Recommended
1. Start Sublime Text 2
2. Install Package Control from will bond (http://wbond.net/sublime_packages/package_control)
Open the Sublime Text 2 console by pressing ctrl+` shortcut. Paste the text below into the console that appears.

	import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print('Please restart Sublime Text to finish installation')

3. Restart Sublime Text 2.
4. Press `ctrl+p` (Windows/Linux) or `super+p` (Mac) and type Install Package. You should see "Package Control: Install Package".
5. Type GPD and press Enter.

###Special Text

There are 5 symbols that can be used to encapsulate text which gives the text special meaning.

`#(Project)` = Represents a project or collection of work that is larger than an indvidual todo  
`!(Target)` = Represents some measurable aspect of a project or a todo. For example, a target weight for a weight loss project or the due date of a project.  
`@(Context)` = Represents People, Places, or Times that the todo is related to. For example, a meeting room or the time of the meeting.   
`$(Cost)` = Represents the time it took to complete the task. This is totally free form, so you could put the actual time in hours, minutes, seconds or some other metric like pomodoros.  
`~(Date/Time)` = The time and date that this todo was done.  

###Sections

Todos are divided into different sections. Today, Goals, Todo, and Closed. These sections are noted by `//Section Name//` followed by an `//End//`. The Today, Todo, and Closed sections are mandatory for this Sublime Text package. You can create any other sections you want.

###Usage
1. Create a new file. Type //-tab and select Boilerplate from the selection box. It will instantly give you the section layouts  
2. Create some Goals and Todos. All the symbols listed above (#, !, @, $, ~) are all tab triggered. I usually start with goals and specify #(Project) !(Target) for each goal and try to avoid any free form text. That's just a suggestion, this thing is free form.  
3. Start working on todos. There are some shortcuts to help you (for Mac OS X replace `ctrl` with `super`):
	* `ctrl+shift+n` will create a new item at the bottom of the //Todo// section
	* `ctrl+shift+.` will put the current todo at the top of the //Today// section
	* `ctrl+shift+down` will put the current todo at the top of //Closed// section and put a ~(datetime.now) at the front of the todo
	* `ctrl+shift+up` will do the same as `ctrl+shift+down` except it will also put the same todo at the bottom of the //Todo// section
	* `ctrl+shift+-` will start a time to track the time it takes to do the todo
	* `ctrl+shift+=` will stop the timer and put a $(total_time) at the end of the todo


###License
Copyright (c) 2013 Giampiero De Ciantis <gdeciantis@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
