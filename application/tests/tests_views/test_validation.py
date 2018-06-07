from django.test import TestCase
from application.services.validation import *
from ...views.base import build_paths
from .resources import *
import copy


class ValidationTests(TestCase):

    elements = test_elements

    def test_can_build_message(self):
        """
        Test that a validation message can be built
        """
        code = "1"
        id = "us98f9kc7"
        label = "Error message"
        response = "Test response"

        message = build_message(code, id, label, response)

        self.assertEqual(message['id'], id)
        self.assertEqual(message['code'], code)
        self.assertEqual(message['href'], '#' +id)
        self.assertEqual(message['label'], label)
        self.assertEqual(message['response'], response)

    def test_can_identify_visible_question(self):
        """
        Test that we can determine that a question is visible
        """
        elements = self.elements
        dependent_question = get_question('fif8f99di', self.elements)

        # Setting a response to the target question that should make the dependent question visible
        set_property('response', 'true', elements, '8rf88f89f8d')

        # Evaluate whether the question is visible
        dependent_visible = question_visible(dependent_question, elements)

        self.assertEqual(dependent_visible, True)

    def test_can_identify_invisible_question(self):
        """
        Test that we can determine that a question is not visible
        """
        elements = self.elements
        dependent_question = get_question('fif8f99di', self.elements)

        # Setting a response to the target question that should make the dependent question invisible
        set_property('response', 'false', elements, '8rf88f89f8d')

        # Evaluate whether the question is visible
        dependent_visible = question_visible(dependent_question, elements)

        self.assertEqual(dependent_visible, False)

    def test_can_strip_response(self):
        """
        Test that we can remove the response from a question
        """
        question = get_question('8rf88f89f8d', self.elements)
        response = 'true'

        # Set a response property on the element
        set_property('response', response, self.elements, '8rf88f89f8d')

        # Verify that the response is set
        self.assertEqual(question['response'], response)

        # Remove the response
        strip_response(question)

        # Verify that the response is no longer set
        self.assertEqual(question['response'], None)

    def test_can_assess_condition_radio_inline_valid(self):
        """
        Test that we can validate the valid response to a question
        """
        # Set a valid response to the question
        set_property('response', 'true', self.elements, '8rf88f89f8d')
        question = get_question('8rf88f89f8d', self.elements)
        validation = assess_condition(question, self.elements)

        self.assertEqual(validation, True)

    def test_can_assess_condition_radio_inline_invalid(self):
        """
        Test that we can validate the invalid response to a question
        """
        # Set an invalid response to the question
        set_property('response', '', self.elements, '8rf88f89f8d')
        question = get_question('8rf88f89f8d', self.elements)
        validation = assess_condition(question, self.elements)

        # An error message is expected as the validation result
        message = build_message("1", question['id'], "This question is required", question['response'])

        self.assertEqual(validation, message)

    def test_can_assess_condition_text_valid(self):
        """
        Test that we can validate the valid response to a question
        """
        # Set a valid response to the question
        set_property('response', 'test answer', self.elements, '98r8jd8rrdy')
        question = get_question('98r8jd8rrdy', self.elements)
        validation = assess_condition(question, self.elements)

        self.assertEqual(validation, True)

    def test_can_assess_condition_text_invalid(self):
        """
        Test that we can validate the invalid response to a question
        """
        # Set an invalid response to the question
        set_property('response', '', self.elements, '98r8jd8rrdy')
        question = get_question('98r8jd8rrdy', self.elements)
        validation = assess_condition(question, self.elements)

        # An error message is expected as the validation result
        message = build_message("1", question['id'], "This question is required", question['response'])

        self.assertEqual(validation, message)

    def test_can_assess_condition_date_valid(self):
        """
        Test that we can validate the valid date
        """
        # Set a valid response to the question
        set_property('response', '19-11-2016', self.elements, '487478jjjfju')
        set_property('response_list', {"day": "19", "month": "11", "year": "2016"}, self.elements, '487478jjjfju')

        # Set a response to the trigger question to make the question visible
        set_property('response', 'true', self.elements, 'uuuui4848')

        question = get_question('487478jjjfju', self.elements)
        validation = assess_condition(question, self.elements)

        self.assertEqual(validation, True)

    def test_can_assess_condition_date_invalid(self):
        """
        Test that we can validate the invalid date
        """
        # Set an invalid response to the question
        set_property('response', '--', self.elements, '487478jjjfju')
        set_property('response_list', {"day": "", "month": "", "year": ""}, self.elements, '487478jjjfju')

        # Set a response to the trigger question to make the question visible
        set_property('response', 'true', self.elements, 'uuuui4848')

        question = get_question('487478jjjfju', self.elements)
        validation = assess_condition(question, self.elements)

        # An error message is expected as the validation result
        message = build_message("1", question['id'], "This question is required", question['response'])

        self.assertEqual(validation, message)

    def test_can_assess_condition_date_incomplete(self):
        """
        Test that we can validate the incomplete date
        """
        # Set an invalid response to the question
        set_property('response', '-5-', self.elements, '487478jjjfju')
        set_property('response_list', {"day": "", "month": "5", "year": ""}, self.elements, '487478jjjfju')

        # Set a response to the trigger question to make the question visible
        set_property('response', 'true', self.elements, 'uuuui4848')

        question = get_question('487478jjjfju', self.elements)
        validation = assess_condition(question, self.elements)

        # An error message is expected as the validation result
        message = build_message("3", question['id'], "Please supply a complete date", question['response'])

        self.assertEqual(validation, message)

    def test_can_assess_condition_checkbox_valid(self):
        """
        Test that we can validate the valid response to a checkbox question
        """
        # Set a valid response to the question
        set_property('response', [
            {"choice_id": "98r8jd8rrde-1", "choice": None},
            {"choice_id": "98r8jd8rrde-2", "choice": "Coffee beans"},
            {"choice_id": "98r8jd8rrde-3", "choice": "Mexican Jumping beans"},
            {"choice_id": "98r8jd8rrde-4", "choice": None}
        ], self.elements, '98r8jd8rrde')

        # Mark the chosen answers as checked
        set_property('options', [
            {
                "id": 1,
                "label": "Baked beans",
                "ticked": False
            },
            {
                "id": 2,
                "label": "Coffee beans",
                "ticked": True
            },
            {
                "id": 3,
                "label": "Mexican Jumping beans",
                "ticked": True
            },
            {
                "id": 4,
                "label": "Jelly beans",
                "ticked": False
            }
        ], self.elements, '98r8jd8rrde')

        question = get_question('98r8jd8rrde', self.elements)
        validation = assess_condition(question, self.elements)

        self.assertEqual(validation, True)

    def test_can_assess_condition_checkbox_invalid(self):
        """
        Test that we can validate the invalid response to a question
        """
        # Set an invalid response to the question
        set_property('response', [
            {"choice_id": "98r8jd8rrde-1", "choice": None},
            {"choice_id": "98r8jd8rrde-2", "choice": None},
            {"choice_id": "98r8jd8rrde-3", "choice": None},
            {"choice_id": "98r8jd8rrde-4", "choice": None}
        ], self.elements, '98r8jd8rrde')

        # Mark the chosen answers as checked
        set_property('options', [
            {
                "id": 1,
                "label": "Baked beans",
                "ticked": False
            },
            {
                "id": 2,
                "label": "Coffee beans",
                "ticked": False
            },
            {
                "id": 3,
                "label": "Mexican Jumping beans",
                "ticked": False
            },
            {
                "id": 4,
                "label": "Jelly beans",
                "ticked": False
            }
        ], self.elements, '98r8jd8rrde')

        question = get_question('98r8jd8rrde', self.elements)
        validation = assess_condition(question, self.elements)

        # An error message is expected as the validation result
        message = build_message("2", question['id'], "Choose an option", question['response'])

        self.assertEqual(validation, message)

    def test_can_validate_form_valid(self):
        """
        Test that a form containing all valid responses can be validated
        """

        # Set valid responses
        set_property('response', 'test answer', self.elements, '98r8jd8rrdy')
        set_property('response', 'true', self.elements, '8rf88f89f8d')

        question1 = get_question('98r8jd8rrdy', self.elements)
        question2 = get_question('8rf88f89f8d', self.elements)

        # Validate a form comprised of these questions
        messages = validate_form([question1, question2])

        self.assertEqual(messages, [])

    def test_can_validate_form_invalid(self):
        """
        Test that a form containing invalid responses can be validated
        """

        # Set valid responses
        set_property('response', '', self.elements, '98r8jd8rrdy')
        set_property('response', 'true', self.elements, '8rf88f89f8d')

        question1 = get_question('98r8jd8rrdy', self.elements)
        question2 = get_question('8rf88f89f8d', self.elements)

        # Validate a form comprised of these questions
        messages = validate_form([question1, question2])

        message = build_message("1", question1['id'], "This question is required", question1['response'])

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], message)


    def test_can_build_partial_paths(self):
        """
        Test that a set of elements can be iterated over and updated to have correct template paths
        """

        # Deep copy is needed so that sub-objects of elements are not implicitly referenced in the copy
        # This is necessary because changing the paths in this test will break other tests if they use the same object
        questions = copy.deepcopy(self.elements)
        question1 = get_question('98r8jd8rrdy', questions)
        question2 = get_question('uisdiudiu', questions)

        self.assertEqual(question1['type'], 'text')
        self.assertEqual(question2['type'], 'radio-inline')

        # Run the function to build out relative paths to template files
        build_paths(questions)

        self.assertEqual(question1['type'], './form-elements/text.html')
        self.assertEqual(question2['type'], './form-elements/radio-inline.html')