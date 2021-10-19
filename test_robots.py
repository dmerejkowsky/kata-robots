import re
from robots import Robot

def test_name_is_not_set_at_first():
    robot = Robot()
    assert robot.name() is None


def test_started_robots_have_a_name():
    robot = Robot()
    robot.start()
    actual_name = robot.name()
    assert actual_name, "name should not be empty"
    # Note: this checks that the name of the robot is properly formatted
    # (2 uppercase letters followed by 2 digits)
    assert re.match(r"^[A-Z]{2}\d{3}$", actual_name)


def test_name_does_not_change_when_rebooted():
    robot = Robot()
    robot.start()
    name1 = robot.name()

    robot.stop()
    robot.start()
    name2 = robot.name()
    assert name1 == name2


def test_name_changes_after_reset():
    robot = Robot()
    robot.start()
    name1 = robot.name()

    robot.reset()
    robot.start()
    name2 = robot.name()
    assert name1 != name2
