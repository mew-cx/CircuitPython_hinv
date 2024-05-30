# Makefile

TGT = GITREPO.txt

all: $(TGT)

$(TGT): .git Makefile
	> $@
	echo "gitdir: `git root`/.git" >> $@
	echo "HEAD `git desc`" >> $@
	echo "remotes {" >> $@
	git remote -v >> $@
	echo "}" >> $@
	echo "branches {" >> $@
	git branch -vv >> $@
	echo "}" >> $@

clean clobber nuke:
	-rm -f $(TGT)

# vim: set sw=4 ts=8 noet ic ai:
