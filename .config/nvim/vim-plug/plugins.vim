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
	
	" Auto pairs for '(' '[' '{'
	Plug 'jiangmiao/auto-pairs'

	" Theme
	Plug 'joshdick/onedark.vim'
	Plug 'vim-airline/vim-airline'
	Plug 'vim-airline/vim-airline-themes'
	
	" Ranger
	Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
	Plug 'junegunn/fzf', {'do': { -> fzf#install() }}
	Plug 'junegunn/fzf.vim'

	" Changes the working directory to the project root
	Plug 'airblade/vim-rooter'
	
	" Colors
	Plug 'norcalli/nvim-colorizer.lua'
	Plug 'junegunn/rainbow_parentheses.vim'
	
	" Other
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	Plug 'liuchengxu/vim-which-key'
	Plug 'voldikss/vim-floaterm'
	Plug 'metakirby5/codi.vim'
	Plug 'honza/vim-snippets'

call plug#end()
