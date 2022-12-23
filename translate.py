import webbrowser
import sys
import pyperclip

print("\n\tThe word you entered or the clipboard should have been translated to italian, german, and french")

if len(sys.argv) > 1:
    myword = ''.join(sys.argv[1:])
else:
    myword = pyperclip.paste()

webbrowser.open(
    'https://translate.google.com/#view=home&op=translate&sl=en&tl=it&text='+myword)

webbrowser.open(
    'https://translate.google.com/#view=home&op=translate&sl=en&tl=fr&text='+myword)

webbrowser.open(
    'https://translate.google.com/#view=home&op=translate&sl=en&tl=de&text='+myword)

print("\n\tTo translate a full sentence or phrase use quotes\n")
