#
# /etc/bash.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ $DISPLAY ]] && shopt -s checkwinsize

PS1='[\u@\h \W]\$ '

case ${TERM} in
Eterm* | alacritty* | aterm* | foot* | gnome* | konsole* | kterm* | putty* | rxvt* | tmux* | xterm*)
	PROMPT_COMMAND+=('printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"')

	;;
screen*)
	PROMPT_COMMAND+=('printf "\033_%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"')
	;;
esac

if [[ -r /usr/share/bash-completion/bash_completion ]]; then
	. /usr/share/bash-completion/bash_completion
fi
PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '
alias vi="nvim"
export EDITOR=nvim
cat ~/.cache/wal/sequences &
#PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"

# Created by `pipx` on 2024-06-29 06:20:11
export PATH="$PATH:/home/user/.local/bin"

alias dns="curl -s https://raw.githubusercontent.com/macvk/dnsleaktest/master/dnsleaktest.sh | bash"

export MANPAGER='nvim +Man!'
