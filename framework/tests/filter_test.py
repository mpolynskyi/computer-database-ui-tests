from framework.actions.computer_table_actions import TableActions
from framework.urls import Urls
from parameterized import parameterized


class FilterTest(TableActions):
    autouse_fixture_names = ["request"]
    # fixture injection

    @parameterized.expand([
        ('asci_white_filter_computer'),
        ('spectrum_2a_filter_computer')
    ])
    def test_filter_computer(self, fixture_name):
        item_for_filter = self.request.getfixturevalue(fixture_name)
        self.open(Urls.computers_table)
        self.filter_computer_by_name(item_for_filter.computer_name)
        self.can_see_computer_in_table(item_for_filter.id,
                                       item_for_filter.computer_name,
                                       item_for_filter.introduced,
                                       item_for_filter.discontinued,
                                       item_for_filter.company)
