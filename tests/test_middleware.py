import unittest
from fastapi import Request, Response
from unittest.mock import Mock, patch
from core.middleware import component_middleware


class TestComponentMiddleware(unittest.TestCase):
    def test_middleware(self):
        mock_request = Mock(spec=Request)
        mock_request.method = "GET"
        mock_request.url = "http://example.com"

        mock_response = Mock(spec=Response)
        mock_response.status_code = 200

        mock_call_next = Mock(return_value=mock_response)
        result = component_middleware(mock_request, mock_call_next)
        mock_call_next.assert_called_once_with(mock_request)
        self.assertEqual(result, mock_response)
