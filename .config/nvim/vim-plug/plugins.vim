" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
	silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
	 \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	"autocmd VimEnter * PlugInstall
	"  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

	" Better Syntax Support
	Plug 'sheerun/vim-polyglot'
	" File Explorer
	"Plug 'scrooloose/NERDTree'
	" Auto pairs for '(' '[' '{'
	Plug 'jiangmiao/auto-pairs'
	" Theme
	Plug 'joshdick/onedark.vim'
	" Stable version of coc
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	" Airline and Themes
	Plug 'vim-airline/vim-airline'
	Plug 'vim-airline/vim-airline-themes'
	" Ranger
	Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
	" FZF
	Plug 'junegunn/fzf', {'do': { -> fzf#install() }}
	Plug 'junegunn/fzf.vim'
	Plug 'airblade/vim-rooter'
	
	Plug 'norcalli/nvim-colorizer.lua'
	Plug 'junegunn/rainbow_parentheses.vim'
	
	Plug 'liuchengxu/vim-which-key'

	" Floaterm
	Plug 'voldikss/vim-floaterm'

	" Codi
	Plug 'ChristianChiarulli/codi.vim'

	" Snippets
	Plug 'honza/vim-snippets'

call plug#end()
