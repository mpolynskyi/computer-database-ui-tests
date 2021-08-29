from framework.actions.computer_item_actions import ItemActions
from parameterized import parameterized


class CreateComputerTest(ItemActions):
    """
    there is different approaches for edit and delete items:
    First one: before edit/delete - create new item via browser
    Second: having fixtures for database and reset them before each test suite run
    I prefer second one
    """
    # fixture injection
    autouse_fixture_names = ['computer_505_with_new_data', 'computer_506_to_delete', 'faker']

    def test_create_valid_computer_item(self):
        name = self.faker.uuid4()
        introduced = '2011-12-14'
        discontinued = '2012-12-14'
        company = 'Nokia'
        self.create_computer(name, introduced=introduced, discontinued=discontinued, company=company)
        self.wait_for_success_created_item_message(name)
        # no other checks because application db is readonly

    @parameterized.expand([['', '', '', ItemActions.wait_for_computer_name_alert_message, 'Failed to refine type : Predicate isEmpty() did not fail.'],
                           ['Test', '2022-12-02', '2021-12-02', ItemActions.wait_for_discontinued_alert, 'Discontinued date is before introduction date'],
                           ['Test', '2022-13-02', '2022-12-02', ItemActions.wait_for_introduced_alert, "Failed to decode date : java.time.format.DateTimeParseException: Text '2022-13-02' could not be parsed: Invalid value for MonthOfYear (valid values 1 - 12): 13"],
                           ['Test', '2022-12-02', '2022-13-02', ItemActions.wait_for_discontinued_alert, "Failed to decode date : java.time.format.DateTimeParseException: Text '2022-13-02' could not be parsed: Invalid value for MonthOfYear (valid values 1 - 12): 13"],
                           ['Test', '2022/12/02', '2022-11-02', ItemActions.wait_for_introduced_alert, "Failed to decode date : java.time.format.DateTimeParseException: Text '2022/12/02' could not be parsed at index 4"],
                           ['Test', '2022-11-02', '2022/12/02', ItemActions.wait_for_discontinued_alert, "Failed to decode date : java.time.format.DateTimeParseException: Text '2022/12/02' could not be parsed at index 4"],
                           ])
    def test_validation_on_computer_creation(self, name, introduced, discontinued, expected_alert_func, expected_alert_text):
        self.create_computer(name, introduced=introduced, discontinued=discontinued)
        expected_alert_func(self, expected_alert_text)

    def test_edit_computer(self):
        self.edit_computer_by_id(self.computer_505_with_new_data.id,
                                 self.computer_505_with_new_data.computer_name,
                                 self.computer_505_with_new_data.introduced,
                                 self.computer_505_with_new_data.discontinued,
                                 self.computer_505_with_new_data.company)

        self.wait_for_success_updated_item_message(self.computer_505_with_new_data.computer_name)
        # no other checks because application db is readonly

    def test_delete_computer(self):
        self.delete_computer_by_id(self.computer_506_to_delete.id)
        self.wait_for_success_delete_item_message(self.computer_506_to_delete.computer_name)
        # no other checks because application db is readonly
