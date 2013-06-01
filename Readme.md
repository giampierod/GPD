###About the GPD System

The GPD system is meant for people who spend a great deal of time text editing. It is a Todo app with the power of GTD and Mark Forster's Final Version with ninjitsu shortcuts for maximum workflow speed. Except for Section headers every line is a todo item. Special symbols allow you to understand different aspects of the todo item. Using combinations of regular and symbolic text, everything is free form text.  

###Pre-Requisites

To install GPD, you first need to install Sublime Text 2. Go to the following linke to download, http://www.sublimetext.com/. This a great application for editing text and supports Linux, Mac, and Windows equally well.

If you are using the git install method, then you are going to the need the git client. You can go to the following link to find out more, http://git-scm.com/downloads.

Once you got Sublime Text 2 up and running there two methods of installing GPD.

###Instal Method 1 - Will Bond's Package Control (Recommended)
Will Bond has made a great plugin that loads packages into Sublime Text. If you use this method you will automatically get updates of GPD when they are released. I highly recommend using this approach.

1. Start Sublime Text 2
2. Install Package Control from will bond (http://wbond.net/sublime_packages/package_control)
Open the Sublime Text 2 console by pressing ``ctrl+` `` shortcut. Paste the text below into the console that appears.
	
	import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print('Please restart Sublime Text to finish installation')
	
3. Restart Sublime Text 2.
4. Press `ctrl+p` (Windows/Linux) or `command+p` (Mac) and type Install Package. You should see "Package Control: Install Package".
5. Type GPD and press Enter.

###Instal Method 2 - Clone Repository
This method has less steps, but you will periodically have to check back to download updates. 

1. Open a terminal or command prompt and navigate to the Packages folder of your Sublime Text 2 installation:
	* Windows - cd %APPDATA%\Sublime Text 2\Packages
	* Mac - cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	* Linux - cd ~/.config/sublime-text/Packages
2. Type `git clone https://github.com/Gimped/GPD` and press `Enter`
3. Restart Sublime Text 2.

###Getting started
A few steps and you will be on your way.

1. Create new file and give it the extension `.GPD` and open it in Sublime Text 2
2. If it doesn't automatically get recognized (You will see GPD in the bottom right corner), then press `ctrl+p` (Windows\Linux) or `Command+p` (Mac) and type `GPD` and press `Enter`. You should see the bottom right of the status bar change.
3. Type `//`,`tab` and select `Boilerplate` from the selection box. It will instantly give you the section layouts and put your cursor in the `Todo` section.
4. Create some Todos. Use symbols to note various aspects of the Todo. For all the symbols available (#, !, @, $, ~, `) you can type `symbol`,`tab` to enter them. All of the symbols represent different attributes of the todo:
	* `#`,`tab` -> #(Project) - The project or group of work that this todo is part of.
	* '!`,`tab` -> !(Target) - A measurable target for the todo. For example, a date, a specific performance metric, etc.
	* `@`,`tab` -> @(Context) - People, places, or things that are related or required for the Todo. Such as a meeting room, a person who are waiting or may need to call.
	* `$`,`tab` -> $(Cost) - The amount of time or other cost metric that should be accounted for this todo.
	* `~`,`tab` -> ~(Completion Date) - The data that you finished the todo.
	* ````,`tab` -> `(Note ID) - An ID that references the Note attached to this todo
5. Once you got this under control, you will want to get familiar with the shortucts. 

###Shortcuts
Shortcuts make GPD what it is, if you don't learn them it's not really going to work that well.

	* `ctrl+shift+n` - Create a new Todo at the bottom of the //Todo// section
	* `ctrl+shift+.` - Move the currently selected Todo at the top of the //Today// section
	* `ctrl+shift+down` - Move the current todo at the top of //Closed// section and put a ~(datetime.now) at the front of the todo
	* `ctrl+shift+up` - Do the same as `ctrl+shift+down` except it will also copy the todo to the bottom of the //Todo// section
	* `ctrl+shift+,` - Get the note for this todo. It will either find or create the note for you in a companion `.GPD_Note` file. When in the GPD_Note file, you can press this again to switch back.


###Special Text

There are 5 symbols that can be used to encapsulate text which gives the text special meaning.

`#(Project)` = Represents a project or collection of work that is larger than an indvidual todo  
`!(Target)` = Represents some measurable aspect of a project or a todo. For example, a target weight for a weight loss project or the due date of a project.  
`@(Context)` = Represents People, Places, or Times that the todo is related to. For example, a meeting room or the time of the meeting.   
`$(Cost)` = Represents the time it took to complete the task. This is totally free form, so you could put the actual time in hours, minutes, seconds or some other metric like pomodoros.  
`~(Date/Time)` = The time and date that this todo was done.  

###Sections

Todos are divided into different sections. Today, Goals, Todo, and Closed. These sections are noted by `//Section Name//` followed by an `//End//`. The Today, Todo, and Closed sections are mandatory for this Sublime Text package. You can create any other sections you want.


###License
Copyright (c) 2013 Giampiero De Ciantis <gdeciantis@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
