git fetch REMOTE




Git branch newbranch
Git checkout newbranch

Git checkout master(or main)
Git merge newbranch

Git branch -d newbranch



git push -u origin master (sets git push to default branch)
git checkout -b feature-1
git checkout main
git diff (shows what changes have been made)
git merge
git pull (from main branch)
git branch -d feature-1

git commit -am "new message"

git reset file.py (unstage commits)
git reset HEAD~1 (undo 1 commit)
git log (all commits shown)

git reset 914398298613892 (commit hash, get back to that commit)
git reset --hard 3294093492 (delete all commits up to this one)

git remote add origin git@githubkkwdowjod.git (when you first done git init, commit, then need to link to a repo on github)

git remote add upstream https://github.com/fetchai/uAgents.git     (connects local repo with main repo, to fetch updates)
