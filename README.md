chrome-bookmark-sort-out
=========================

Sort out your Bookmarks by the regular expressions for Chrome & Chromium.

What can it do?
---------------

I used bookmarks a long time. If I saw something useful web page, I will put it into my bookmark. But sort out the bookmarks is really hard work. Now I have more than a thousand of bookmarks, sort out them manually is impossible.

This program can check the name of the bookmark by your regular expressions, and put them into right folder automatically.

How to use it?
--------------
1. Make sure you have Python 3 interpreter, if not, download and (make) install to your system.
2. Checkout the code.
3. Create a empty folder. Copy Chrome Bookmark File to the same folder of this program. 
   If your platform is Linux, copy ~/.config/chrome (or chromium) /Default/Bookmarks.
4. Write the config file. The config file called 'keywords.conf'. Syntax and document of the config file are in it self.
5. Run the script without any parameter. Your new Bookmark will write to standard output. 
   You should use data stream redirection to redirect them to a file.
   **WARNING:** You shouldn't redirect the output with the same name (*Boorkmarks*), use **anothor** name!
6. Copy the file back to the chrome config folder, and rename it back to "Bookmarks", restart Chrome, then you can see your new Bookmarks!

I got an error, it not works:
------------------------------

This program is untested, still in development, some code need fully rewrite.
Please report a bug if it not works.

**So, please make sure your have create a backup for your bookmarks, just copy the JSON file and keep safe.**
