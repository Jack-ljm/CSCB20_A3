# CSCB20_A3

## How to run the code
### Windows
```bash
cd src
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
### MacOS
```bash
cd src
env FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### How to browse data
I downloaded a sqlite database browser from [here](https://sqlitebrowser.org/dl/).

## Github features
### Issues
We can create new issues for our tasks and assign issues to ourself.

### Pull requests
If you don't want to mess up the main branch, the following process is a nice way to follow.

1. Branch out from the main branch
```bash
git checkout -b branch_name
```

2. Implement features on the new branch and push your code
```bash
git add file_name
git commit -m "your message"
git push origin branch_name
```

4. Make a pull request
- Remember to write down `Resolves #issue_number` in the description section of the pull request so that Github will automatically close that issue for you.
- Github will also check whether there is a merge conflit.

6. Merge
There are three ways to merge your code to the main branch. I usually use `squash and merge` option so that the main branch is clean.

7. Delete the branch
- Delete branch locally
```bash
git branch -d local_branch_name
```
- Delete branch remotely
```bash
git push origin --delete remote_branch_name
```

### .gitignore
I ignore the MacOS system file `.DS_Store` since it is not necessary.\
I also ignore `A3.db` since it is automatically generated in init_db().
