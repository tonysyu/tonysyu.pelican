=========
Git: tips
=========

:tags: git
:status: draft
:date: 2013-12-31


There are plenty of guides for learning git and there are plenty of reference
manuals as well. The problem with git is that there are so many commands to do
so many different things (and sometimes, many commands to do the same thing).
This article just highlights a few commands that I regularly find useful.
Whether it's useful to you depends on what you want to do.


Aliased commands
================

In your `~/.gitconfig` file, you can define shell aliases (under the heading
`[alias]`) for some commonly used commands. This is really useful when you
often call the same command with an option.

   `co = checkout`
      I switch between branches frequently, so this saves a lot of typing.

   `wdiff = diff --word-diff`
      I mainly use word-diff for LaTeX: If you don't hard-wrap paragraphs and
      change a single word, normal diffs can give you a big block of green and
      red. Word-diffs will highlight the individual words that were changed.

   `sdiff = diff --staged`
      When I make multiple changes (either in multiple files, or in the same
      file) but only want to commit a subset of them, I like check the diff
      (to make sure I'm not missing any relevant changes) and the diff for
      the files staged for commit (to make sure I'm not including any
      extraneous changes).

Fixing commits
==============

   `git commit --amend`

   `git rebase or `git rebase -i`
      (where `-i` = using an image in `skimage.data`).
      This allows

Fixing code
===========

   `git bisect`
      My typical workflow is to first find a commit that passes tests, and then
      set that as a "good" commit. Next, I let `git bisect` iterate through the
      commits and each time running the tests and marking a commit as good or
      bad until `git` finds the bad commit.

Testing someone else's branch
=============================

   1. `git remote add my_name_for_repo github_path_for_repo`
   2. `git fetch my_name_for_repo`
   3. `git co -b my_name_for_branch my_name_for_repo/branch_name`

The first command adds the repo as a remote branch. You can save this under any
name you want, but it's easiest to save under the user name. For example, if
you want to track my scikits-image_ branch, you might want to write::

   git remote add tonysyu https://github.com/tonysyu/scikits-image.git

This line adds my fork of scikits-image_ to your repo. Now your repo "knows"
about my repo. But it would doesn't necessary "know" what's in my repo (i.e.
The second line . For convenience, steps 1 and 2 can be combined as::

   git remote add -f tonysyu https://github.com/tonysyu/scikits-image.git

The ``-f`` here fetches my branches. I like to separate this command into 1.
and 2. because if you ever want to play around with a new branch on my repo,
you'll have to call fetch to find new branches and update old ones. Separating
the two makes it explicit that there's more than one thing going on (plus,
you'll know what to do in the future when you need to look at a new branch. The
last line makes a copy of 


Miscellany
==========

   `git stash`
      Save

   `git log -p`
      Show changes.

Gotchas
=======

   `git add --all` vs `git commit -a`
      `git add --all` adds all files not ignored by git to the index (i.e.
      staged for commit). In contrast `git commit -a` adds all *tracked* files
      to the index and, of course, commits them.

.. _scikits-image: http://scikits-image.org/
