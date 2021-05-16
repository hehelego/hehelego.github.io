#!/usr/bin/python
import subprocess

if __name__=='__main__':
    subprocess.run(['rm','-rf','WhyNotMarkdown/'])
    subprocess.run(['rm','-rf','converted/'])
    subprocess.run(['git','clone','https://github.com/hehelego/WhyNotMarkdown','--depth','1'])
    subprocess.run(['python','WhyNotMarkdown/backup/scripts/blog_builder.py'])
    subprocess.run(['rm','-rf','WhyNotMarkdown/'])
