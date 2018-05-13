"""
@brief      test log(time=170s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


class TestNotebookRunner2a_1 (unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencies", OutputPrint=__name__ == "__main__")
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "jyquickhelper"], __file__)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from src.ensae_teaching_cs.automation.notebook_test_helper import clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_1_tiny")
        keepnote = ls_notebooks("td2a_eco")
        for k in keepnote:
            if "_1" in k:
                fLOG("*********", k)
        execute_notebooks(temp, keepnote, (lambda i, n: "_1" in n and "td2_eco_rappels_1a" in n),
                          clean_function=clean_function_1a, fLOG=fLOG, dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
