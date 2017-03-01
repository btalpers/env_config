from subprocess import call
import os

def setupVundle():
    
    call(["git", 
          "clone", 
          "https://github.com/VundleVim/Vundle.vim.git", 
          os.path.expanduser("~/.vim/bundle/Vundle.vim")])



setupVundle()



