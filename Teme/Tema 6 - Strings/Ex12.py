# Print a justified word count for py_text variable.

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

count_words = py_text.replace(".","").replace(",","").split(" ")

print("{} Words".format(len(count_words)))