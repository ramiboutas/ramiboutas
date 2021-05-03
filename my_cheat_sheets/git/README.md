
## Using Git & GitHub

Git: [https://git-scm.com/](https://git-scm.com/)

### Concepts
* Repo: repository
* Remote repo: a repo on the internet (on GitHub for instance)

### Clone a repository (let's called repo) from GitHub

* Clone a remote repo to a local PC: `git clone <ressoure>`

### Adding & commiting changes

* Adding
  - One file: `git add <file>`
  - All files in the current folder: `git add . `
* Commit Changes: `git commit -m "{description of changes}"`
* Adding & Commiting: `git commit -am "{description of changes}"`

### Updating the remote repo and getting updates from it

* Updating the repo: `git push`
* Getting the updates (other contributors did some changes and you need the last update): `git pull`

<img align="center" src="images/pushpull.png">
