import unittest

import robotsuite
from pkg_resources import resource_listdir
from plone.testing import layered

from baobab.lims.testing import SANBI_ROBOT_TESTING

robots = [f for f in resource_listdir("baobab.lims", "tests")
          if f.endswith(".robot")]


def test_suite():
    suite = unittest.TestSuite()
    for robot in robots:
        suite.addTests([
            layered(robotsuite.RobotTestSuite(robot),
                    layer=SANBI_ROBOT_TESTING),
        ])
    return suite
