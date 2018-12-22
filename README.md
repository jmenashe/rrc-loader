# Recursive VimRC Loader

1. Set the first line to the load signature and use ! to override functions.
   Example:

```lua
let g:rrc_loader_signature = 'jMsnlSkK3wFc8wzROPG2vaWSclFXXbV76reHrl6wKAtLt'
function! SetLaTeX()
  set noautoindent
  set nocindent
endfunction
```
