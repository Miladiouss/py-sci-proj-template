# Scripts vs Modules

This directory contains Python scripts that may or may not rely on the packages being developed under `py_src` directory. The trivial difference between Python packages and Python scripts is that the latter is intended to be imported while the former is only intended to be executed. Python packages should be developed from the perspective of a developer constantly keeping in mind how the user of the package might interact with it. On the other hand, a script is written from the perspective of a user of the developed packages.

Some examples of scripts are:

1. Scripts running computational experiments
2. Scripts for visualization data
3. Scripts used for auto-generating documents (e.g. Markdown to PDF)
4. Scripts responsible for running integration tests
