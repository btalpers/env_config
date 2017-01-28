#!/bin/bash

if [ -e ~/.zshrc ]
then
	mv ~/.zshrc ./backup/zshrc.backup
fi
if [ -h ~/.zshrc ]
then
	unlink ~/.zshrc
fi
ln -s `pwd`/zsh/zshrc ~/.zshrc

if [ -e ~/.vimrc ]
then
	mv ~/.vimrc ./backup/vimrc.backup
fi
if [ -h ~/.vimrc ]
then
	unlink ~/.vimrc
fi
ln -s `pwd`/vim/vimrc ~/.vimrc
