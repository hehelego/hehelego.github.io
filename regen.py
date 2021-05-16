#!/usr/bin/python
import subprocess
import sys

def fullyRegen():
    subprocess.run(['rm','-rf','WhyNotMarkdown/'])
    subprocess.run(['rm','-rf','converted/'])
    subprocess.run(['git','clone','https://github.com/hehelego/WhyNotMarkdown','--depth','1'])
    subprocess.run(['python','WhyNotMarkdown/backup/scripts/blog_builder.py'])
    subprocess.run(['rm','-rf','WhyNotMarkdown/'])
def partiallyRegen():
    subprocess.run(['rm','-rf','converted/'])
    subprocess.run(['python','WhyNotMarkdown/backup/scripts/blog_builder.py'])

def main():
    if len(sys.argv)<2:
        print('usage: ./regen.py (f|p)')
        return

    opt = sys.argv[1]
    if opt=='f':
        fullyRegen()
    elif opt=='p':
        partiallyRegen()
    else:
        print('usage: ./regen.py (f|p)')




if __name__=='__main__':
    main()
