# Unit tests

This directory contains unit tests and should be parallel to `py_src`. For every module, there should be a corresponding test that must pass before merging a branch. The minimum requirement for a unit test is to make a call to all functions and classes that are intended for the user and ensure that they behave as expected. This is a much smaller subset of all the functionality that has been developed and is only paying attention to what is visible from outside. A minimal unit test doesn't necessarily validate the functionalities. It is mainly responsible for ensuring that changes to the code do not have unintended effects by breaking components that were not changed themselves. Having said that, validating the functionality of the products is important. It may be done as unit tests or as scripts.

Since tests are regularly run by GitHub actions, it is important to keep them light. To this end, light datasets are stored (and version controlled) under [`data`](data/). Alternatively, the data can be simulated for each test.

To run the tests, simply execute the following command at the repository level:

```sh
pytest .
```
