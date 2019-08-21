from unittest import TestCase

from back_end.web_app.api_querier import map_parameters


class Test_classes_requester(TestCase):
    def test_map_parameters_invalid(self):
        mapped_params = map_parameters(class_name=None, attendance_date='')  # type: str
        self.assertEqual('', mapped_params)

    def test_map_parameters_valid(self):
        mapped_params = map_parameters(class_name='db', attendance_date='2019-01-01')  # type: str
        self.assertEqual('class_name=db&attendance_date=2019-01-01', mapped_params)

