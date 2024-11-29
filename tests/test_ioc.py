import unittest
from unittest.mock import MagicMock

from core.command import ICommand
from core.ioc import IoC, IoCRegister, Scope, IIoC


class TestIoCContainer(unittest.TestCase):

    def setUp(self):
        IoC.scopes = Scope()

    def test_register_and_resolve(self):
        mock_command = MagicMock(spec=ICommand)

        register_command = IoCRegister('test_key', mock_command)
        register_command.execute()

        resolved_command = IoC.resolve('test_key')
        self.assertIsInstance(resolved_command, MagicMock)

    def test_resolve_non_existent_key(self):
        with self.assertRaises(ValueError):
            IoC.resolve('non_existent_key')

    def test_register_default_command(self):
        resolved_command = IoC.resolve('IoC.Register', 'test_key', MagicMock(spec=ICommand))
        self.assertIsInstance(resolved_command, IoCRegister)
