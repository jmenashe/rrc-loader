let s:rrc_command = expand('<sfile>:h:h')."/rrc-locator.py ".expand('%:p')
let s:filenames = system(s:rrc_command)
for s:filename in split(s:filenames, ";")
  "echom "Checking ".s:filename
  if filereadable(s:filename) && match(readfile(s:filename),g:rrc_loader_signature) >= 0
    "echom "Loading ".s:filename
    execute 'source '.fnameescape(s:filename)
  else
    echom "Unreadable file or invalid signature: '".fnameescape(s:filename) . "'"
  endif
endfor
