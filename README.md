chrome-bookmark-sort-out
=========================

Sort out your Bookmarks by the keywords/regular expressions for Chrome/Chromium.

What can it do?
---------------

I used bookmarks/favorite of every web browser a long time. If I saw something useful web page, I will put it into my bookmark. But sort out the bookmarks is really hard work. Now I have more than a thousand of bookmark, sort out it manually is impossible.

This program can check the name of the bookmark by your regular expressions, and put them into right folder automatically.

How to use it?
--------------
Software Requested:
1. A Python3 interpreter.

First, make sure you have Python 3 interpreter, if not, download and (make) install to your system.

Second, checkout the code.

Third, create a empty folder. Bookmarks of Chrome are save in JSON format, so your must copy it to the same folder of this program. If your platform is Linux, copy ~/.config/chrome (or chromium)/Default/Bookmarks out.

Forth, write the config file. The config file called 'keywords.conf'. Syntax and document of the config files are in it self.

Fifth, run the script with no parameter. Your new Bookmark will write to standard output, you should use data stream redirection to redirect them to a file.

Sixth, copy this file back to the chrome config folder, and rename it back to "Bookmarks", restart Chrome, them you can see your new Bookmarks!

I got an error, it not works:
------------------------------

This program is untested, still in development, some code need fully rewrite.
Please report a bug if it not works.

So, please make sure your have create a backup for your bookmarks, just copy the JSON file and keep safe.
