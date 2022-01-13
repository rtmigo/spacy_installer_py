import unittest

from spacy import Language

import spacy_installer


# self.assertEqual(spacy_installer.can_load(model_name), False)
# m = spacy_installer.load_model(model_name)
# self.assertIsInstance(m, Language)


class TestInstallUninstall(unittest.TestCase):
    model_name = 'en_core_web_sm'

    def setUp(self) -> None:
        if spacy_installer.can_load(self.model_name):
            spacy_installer.uninstall_model(self.model_name)

    def tearDown(self) -> None:
        spacy_installer.uninstall_model(self.model_name)

    def test_install_uninstall(self):
        self.assertEqual(spacy_installer.can_load(self.model_name), False)

        # install and check
        spacy_installer.install_model(self.model_name)
        self.assertEqual(spacy_installer.can_load(self.model_name), True)

        # uninstall and check
        spacy_installer.uninstall_model(self.model_name)
        self.assertEqual(spacy_installer.can_load(self.model_name), False)


class TestLoad(unittest.TestCase):
    model_name = 'en_core_web_sm'

    def setUp(self) -> None:
        if spacy_installer.can_load(self.model_name):
            spacy_installer.uninstall_model(self.model_name)

    def tearDown(self) -> None:
        spacy_installer.uninstall_model(self.model_name)

    def test_install_uninstall(self):
        self.assertEqual(spacy_installer.can_load(self.model_name), False)
        self.assertEqual(spacy_installer.can_load(self.model_name), False)

        m = spacy_installer.load_model(self.model_name)
        self.assertIsInstance(m, Language)
        self.assertEqual(spacy_installer.can_load(self.model_name), True)
