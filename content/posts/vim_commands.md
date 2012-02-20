Title: Favorite vim commands
Author: Tony S. Yu
Tags: vim
Status: draft


Normal mode
-----------

`.`: repeat command

- I use this frequently to replace the more cumbersome multiplier
  convention. For example, instead of `d3w` to delete 3 words in front
  of the cursor, I would most likely use `dw..` to delete next word and
  repeat twice. I find this to be much easier than counting letters,
  words, lines, etc.

`;`: repeat last line-search movement

- By line-search movment, I mean `f`, `F`, `t`, `T` commands. If I want
  to 

`g;`: go to previous edit

- With other text editors, I find myself using undo to find a place in
  a file. If you just want to go back to the last edited position,
  that's not a bad solution. But, if you want to go to the edit before
  that, then it gets difficult (because you have to redo (or undo?) the
  previous "undo"s). With vim, you can just do `g;g;`---repeat as
  necessary.
