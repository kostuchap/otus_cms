import unittest
from unittest.mock import MagicMock

from core.command import ICommand, MacroCommand, LambdaCommand


class TestCommands(unittest.TestCase):

    def test_macro_command_execute(self):
        mock_command1 = MagicMock(spec=ICommand)
        mock_command2 = MagicMock(spec=ICommand)

        macro_command = MacroCommand([mock_command1, mock_command2])

        macro_command.execute()

        mock_command1.execute.assert_called_once()
        mock_command2.execute.assert_called_once()

    def test_lambda_command_execute(self):
        mock_lambda = MagicMock()

        lambda_command = LambdaCommand(mock_lambda)

        lambda_command.execute()

        mock_lambda.assert_called_once()

    def test_lambda_command_with_real_lambda(self):
        counter = 0

        def increment():
            nonlocal counter
            counter += 1

        lambda_command = LambdaCommand(increment)

        lambda_command.execute()

        self.assertEqual(counter, 1)

    def test_macro_command_with_mixed_commands(self):
        mock_command = MagicMock(spec=ICommand)
        counter = 0

        def increment():
            nonlocal counter
            counter += 1

        macro_command = MacroCommand([mock_command, LambdaCommand(increment)])

        macro_command.execute()

        mock_command.execute.assert_called_once()

        self.assertEqual(counter, 1)
