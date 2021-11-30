# Git Rutines

This article will help you configure git and shows you how to properly use git branches.

## Initial Setup

Make vscode the default git editor:
`git config --global core.editor "code --wait"`

Make git remember credentials:

1. `git config --global credential.helper cache`
2. `git config --global credential.helper "cache --timeout=2500000"`

Initialize git and specify branch name:
`git init -b main`

## Most commonly used git commands

VS Code can provide a visual way to interact with git. But ensure you are familiar with the following git commands:

- git fetch
- git add -A
- git commit -m "implement feature-1"

## Properly using git branches

### Create a branch

Create a new branch and switch to it: `git checkout -b ticket-123_feature`

If needed, delete a local branch: `git branch -d <obsolete-branch>`

### Rebasing and Squashing (with VS Code)

Note: Use system terminal to execute the following commands. The interactive feature doesn't function properly in VS Code integrated terminal.

1. Ensure all changes are committed.
2. Ensure that the local and remote repose are in sync.
3. Rebase onto `origin/main` to keep up to date with `origin/main`: `git rebase -i origin/main`
4. Resolve conflicts if any and be sure all tests pass. You may have to repeat the previous steps if new changes need to be made.
5. Rebase the branch to clean up its history: `git rebase -i HEAD~<n>`
    1. Pick the earliest commit and mark the rest as fixup.
6. Force push the current branch: `git push --force-with-lease origin <feature-branch>`

### Pull Request

1. Create a pull request (PR) on branch page on GitHub.
2. Assign someone to review it.
3. Once reviewed and all concerns have been answered, click on merge.
    1. Use a template for the merge message:
4. Delete the branch (assuming all tests pass on the main branch too).
5. Update you local main with the remote one.
