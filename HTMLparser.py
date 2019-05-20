
# REFERENCE : https://docs.python.org/3/library/html.parser.html

# It defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.
# The user should subclass HTMLParser and override its methods to implement the desired behavior.

# HTMLParser instances have the following methods:
# 1
# parser.feed(data)
# Feed some text to the parser. It is processed insofar as it consists of complete elements; 
# incomplete data is buffered until more data is fed or close() is called. data must be str.

# 2
# parser.close()
# Force processing of all buffered data as if it were followed by an end-of-file mark.

# 3
# parser.reset()
# Reset the instance. Loses all unprocessed data. This is called implicitly at instantiation time.

# 4
# parser.getpos()
# Return current line number and offset

# 5
# def handle_starttag(self, tag, attrs):
# This method is called to handle the start of a tag (e.g. <div id="main">).
# The tag argument is the name of the tag converted to lower case. 
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.

# 6
# def handle_endtag(self, tag):
# This method is called to handle the end tag of an element (e.g. </div>).
# The tag argument is the name of the tag converted to lower case.

# 7
# def handle_startendtag(self, tag, attrs):
# called when the parser encounters an XHTML-style empty tag (<img ... /> , <input ... />).

# 8
# def handle_data(self, data):
# This method is called to process arbitrary data

# 9
# def handle_comment(self, data):
# This method is called when a comment is encountered (e.g. <!--comment-->).

# 10
# def handle_decl(self, decl):
# This method is called to handle an HTML doctype declaration (e.g. <!DOCTYPE html>).

# 11
# def unknown_decl(self, data):
# This method is called when an unrecognized declaration is read by the parser.



# EXAMPLE 1
# detect and print all the HTML tags, attributes and attribute values.
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("-> " + i[0] + " > " + i[1])

parser = MyHTMLParser()

n = int(input())
while n:
    a = input()
    parser.feed(a)
    n-=1



# EXAMPLE 2
# check start tags, end tags and empty tags with their attributes and values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("-> " + str(i[0]) + " > " + str(i[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("-> " + str(i[0]) + " > " + str(i[1]))

parser = MyHTMLParser()

n = int(input())
while n:
    a = input()
    parser.feed(a)
    n-=1



# EXAMPLE 3
# check for single-line comments, multi-line comments and the data
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data!="\n":
            print(">>> Data")
            print(data)
        
    def handle_comment(self, data):
        lst = data.split("\n")
        if len(lst)>1:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    
parser = MyHTMLParser()

parser.feed(html)
parser.close()


