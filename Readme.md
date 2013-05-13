About the GPD System
====================

The GPD system is meant for people who spend a great deal of time text editing. It is a Todo app with the power of GTD and Mark Forster's Final Version, but the simplicity of writing a final. Except for Section headers every line is a todo item. Special symbols allow you to understand different aspects of the todo item. Using combinations of regular and symbolized everything is free form, with the ability to understand general organization. I doubt this tool is for everyone, but I find it quite useful.

Special Text
============
There are 5 symbols that can be used to encapsulate text which gives the text special meaning.

\#(Project) = Represents a project or collection of work that is larger than an indvidual todo
!(Target) = Represents some measurable aspect of a project or a todo. For example, a target weight for a weight loss project or the due date of a project.
@(Context) = Represents People, Places, or Times that the todo is related to. For example, a meeting room or the time of the meeting. 
$(Cost) = Represents the time it took to complete the task. This is totally free form, so you could put the actual time in hours, minutes, seconds or some other metric like pomodoros.
~(Date/Time) = The time and date that this todo was done.

Sections
========
Todos are divided into different sections. Today, Goals, Todo, and Closed. These sections are noted by //Section Name// followed by an //End//. The Today, Todo, and Closed sections are mandatory for this Sublime Text package. You can create any other sections you want.

Usage
=====
Step 1. Create a new file. Type //-tab and select Boilerplate from the selection box. It will instantly give you the section layouts
Steo 2. Create some Goals and Todos. All the symbols listed above (#, !, @, $, ~) are all tab triggered. I usually start with goals and specify #(Project) !(Target) for each goal and try to avoid any free form text. That's just a suggestion, this thing is free form.
Step 3. Start working on todos. There are some shortcuts to help you:
- ctrl+shift+. will put the current todo at the top of the //Today// section
- ctrl+shift+end will put the current todo at the top of //Closed// section and put a ~(datetime.now) at the front of the todo
- ctrl+shift+insert will do the same as ctrl+shift+end except it will also put the same todo at the bottom of the //Todo// section
- ctrl+shift+- will start a time to track the time it takes to do the todo
- ctrl+shift+= will stop the timer and put a $(total_time) at the end of the todo
