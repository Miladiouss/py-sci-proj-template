# Git routines

This article includes instruction to configure git and provides guidelines for proper use of git branches.

## Initial setup

If using VS Code, make it the default git editor:
`git config --global core.editor "code --wait"`

Make git remember credentials:

1. `git config --global credential.helper cache`
2. `git config --global credential.helper "cache --timeout=2500000"`

Make `main` the default branch name:
`git config --global init.defaultBranch main`

Initialize git and specify branch name:
`git init -b main`

## Most commonly used git commands

VS Code can provide a visual way to interact with git. But ensure you are familiar with the following git commands:

- git fetch
- git add -A
- git commit -m "implement feature-1"

## Recommendations on using git branches

### Create and deleting a branch

Create a new branch and switch to it: `git checkout -b <ticket-nnn_feature>`

If needed, delete a local branch: `git branch -d <obsolete-branch>`

### Rebasing and squashing (with VS Code)

Before making a pull request, consider following these steps. It ensures a clean git history and facilitates team work.

Note: You may use the VS Code integrated terminal. Howevere, if it doesn't behave properly, use the system terminal instead.

1. Ensure all changes are committed.
2. Ensure that the local and remote repose are in sync.
3. Rebase onto `origin/main` to keep up to date with `origin/main`: `git rebase -i origin/main`
4. Resolve conflicts if any and be sure all tests pass. You may have to repeat the previous steps if new changes need to be made.
5. Rebase the branch to clean up its history: `git rebase -i HEAD~<n>`
    1. Pick the earliest commit and mark the rest as fixup.
6. Force push the current branch: `git push --force-with-lease origin <feature-branch>`

### Pull Request

1. Create a pull request (PR) on a branch page on GitHub.
2. Assign someone to review it.
3. Once reviewed and all concerns have been answered, click on merge.
    1. Decide on a template and use that for the merge message.
4. If tests pass on the main branch, then delete the feature branch to keep the history linear.
5. Update the local main branch on your machine with the remote one on GitHub.
