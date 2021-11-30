# Visual Code Studio setup

While you can always run tools from command line, setting up your Integrated Development Environment (IDE) will make it much easier to develop projects, test, debug, follow formatting rules, and version control. There are many IDE out there, but here, we provide basic VS Code configuration. Learn more at <https://code.visualstudio.com/docs/>.

## Extensions

### Coding

- Python: The official Python extension, from Microsoft.
- Better Comments
- Trailing Spaces: Highlights and/or deletes trailing spaces, which Flake8 will otherwise complain about.
- Python Indent: Correct python indentation in Visual Studio Code.
- Python Docstring Generator

### Documentation

- Markdown All in One
- markdownlint
- Markdown Header Coloring
- Graphviz Markdown Preview
- Latex Workshop: Useful for writing Latex docs.
- restructuredText: Useful for writing Sphinx docs.
- Code Spell Checker

### Others

- Remote Development, Remote - SSH: Provides support for editing, browsing, and debugging code on a remote server from a local editor, over SSH.

## User settings

Follow Rubin/LSST recommendations for VSCode with the addition of "python.linting.flake8Args" settings.

To open User settings.json file, use Command Palette (⇧⌘P) with Preferences: Open Settings (JSON).

```json
{
    "editor.rulers": [
        80,
       110
    ],
    "files.exclude": {
       "**/__pycache__": true,
       "**/.coverage.*": true,
       "**/.pytest_cache": true,
       "**/.sconf_temp": true,
       "**/.sconsign.dblite": true,
       "**/.tests": true,
       "**/*.o": true,
       "**/*.os": true
    },
   "files.watcherExclude": {
       "**/__pycache__": true
    },
    "trailing-spaces.trimOnSave": true,
    "restructuredtext.linter.extraArgs": [
       "--ignore D001"
    ],
    "[restructuredtext]": {
        "editor.wordWrap": "wordWrapColumn",
    },
    "python.linting.flake8Args": [
        "--max-line-length=110",
        "--ignore=E133,E226,E228,N802,N803,N806,N812,N813,N815,N816,W503",
    ],
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "search.useGlobalIgnoreFiles": true,
    "python.dataScience.enabled": false,
    "latex-workshop.latex.external.build.command": "make",
    "[cpp]": {
       "editor.defaultFormatter": "ms-vscode.cpptools"
    },
    "terminal.integrated.inheritEnv": false,
    "window.zoomLevel": 1
}
```
