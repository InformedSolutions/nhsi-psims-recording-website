from django.test import TestCase
from ...validation import build_message


class ValidationTests(TestCase):

    def test_can_build_message(self):
        """
        Test that a validation message can be built
        """
        code = "1"
        id = "us98f9kc7"
        label = "Error message"
        response = "Test respose"

        message = build_message(code, id, label, response)

        self.assertEqual(message['id'], id)
