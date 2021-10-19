# The robots kata

# Specifications

Your are a developer inside a robot factory. Your task is to manage robot settings.

Here are the rules:

* When robots come off the factory floor, they have no name.
* The first time you boot them up, a random name is generated in the format
  of two uppercase letters followed by three digits, such as RX837 or BC811.
* Every once in a while we need to reset a robot to its factory settings,
  which means that their name gets wiped. The next time you ask, it will
  respond with a new random name.


# Instructions

Clone this repo

Create a virtualenv

Install pytest in the virtualenv

Activate the virtualenv

Check that pytest is set up properly

```
$ pytest test_robots.py
```

This should print something like:

```
======= test session starts =======

collected 4 items

test_robots.py .FFF

...

FAILED test_started_robots_have_a_name
    AssertionError: name should not be empty

FAILED test_name_does_not_change_when_rebooted
    AttributeError: 'Robot' object has no attribute...

FAILED test_name_changes_after_reset
    AttributeError: 'Robot' object has no attribute 'reset'
```

Your goal is to change the code in `robots.py` to make all the tests pass.
