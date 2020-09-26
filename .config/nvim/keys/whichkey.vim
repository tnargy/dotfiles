" Map leader to which_key
nnoremap <silent> <leader> :silent WhichKey '<Space>'<CR>
vnoremap <silent> <leader> :silent <c-u> :silent WhichKeyVisual '<Space>'<CR>

" Create map to add keys to
let g:which_key_map =  {}
" Define a separator
let g:which_key_sep = '→'


" Not a fan of floating windows for this
let g:which_key_use_floating_win = 0

" Change the colors if you want
highlight default link WhichKey          Operator
highlight default link WhichKeySeperator DiffAdded
highlight default link WhichKeyGroup     Identifier
highlight default link WhichKeyDesc      Function

" Hide status line
autocmd! FileType which_key
autocmd  FileType which_key set laststatus=0 noshowmode noruler
  \| autocmd BufLeave <buffer> set laststatus=2 noshowmode ruler

" Single mappings
let g:which_key_map['.'] = [ ':e $MYVIMRC'                , 'edit init.vim' ]
let g:which_key_map['%'] = [ ':so %'                      , 'source %' ]
let g:which_key_map['e'] = [ ':CocCommand explorer'       , 'explorer' ]
let g:which_key_map['h'] = [ '<C-W>s'                     , 'split below']
let g:which_key_map['r'] = [ ':Ranger'                    , 'ranger' ]
let g:which_key_map['v'] = [ '<C-W>v'                     , 'split right']

let g:which_key_map['w'] = [ ':w'                         , 'write']

let g:which_key_map.q = {
      \ 'q' : [':q'            , 'quit']
      \ }

" b is for buffers
let g:which_key_map.b = {
      \ 'name' : '+buffers',
      \ 'd' : [':bd'           , 'delete'],
      \ 'l' : [':ls'           , 'list'],
      \ 'n' : [':bnext'        , 'next'],
      \ 'p' : [':bprevious'           , 'previous'],
      \ }

" s is for search
let g:which_key_map.s = {
      \ 'name' : '+search' ,
      \ '/' : [':History/'     , 'history'],
      \ ';' : [':Commands'     , 'commands'],
      \ 'a' : [':Ag'           , 'text Ag'],
      \ 'B' : [':Buffers'      , 'open buffers'],
      \ 'f' : [':Files'        , 'files'],
      \ 'h' : [':History'      , 'file history'],
      \ 'H' : [':History:'     , 'command history'],
      \ 'l' : [':Lines'        , 'lines'] ,
      \ 'm' : [':Marks'        , 'marks'] ,
      \ 'M' : [':Maps'         , 'normal maps'] ,
      \ 's' : [':Snippets'     , 'snippets'],
      \ 'S' : [':Colors'       , 'color schemes'],
      \ 't' : [':Rg'           , 'text Rg'],
      \ 'w' : [':Windows'      , 'search windows'],
      \ 'y' : [':Filetypes'    , 'file types'],
      \ 'z' : [':FZF'          , 'FZF'],
      \ }

" t is for terminal
let g:which_key_map.t = {
      \ 'name' : '+terminal' ,
      \ ';' : [':FloatermNew'                                   , 'terminal'],
      \ 'f' : [':FloatermNew fzf'                               , 'fzf'],
      \ 'n' : [':FloatermNew node'                              , 'node'],
      \ 'p' : [':FloatermNew python'                            , 'python'],
      \ 'r' : [':FloatermNew ranger'                            , 'ranger'],
      \ 't' : [':FloatermToggle'                                , 'toggle'],
      \ 'y' : [':FloatermNew ytop'                              , 'ytop'],
      \ }

" Register which key map
call which_key#register('<Space>', "g:which_key_map")
