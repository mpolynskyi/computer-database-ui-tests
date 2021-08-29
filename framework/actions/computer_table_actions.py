from .base_actions import BaseAction
from framework.pages.computers_table_page import ComputersTablePage


class TableActions(BaseAction):
    def filter_computer_by_name(self, name: str):
        self.wait_for_element_visible(ComputersTablePage.filter_by_computer_name_field)
        self.type(ComputersTablePage.filter_by_computer_name_field, name)
        self.click(ComputersTablePage.filter_by_name_button)

    def can_see_computer_in_table(self,
                                  id,
                                  computer_name: str,
                                  introduced: str = None,
                                  discontinued: str = None,
                                  company: str = None):
        row_selector = ComputersTablePage.table_row_by_computer_id(id)
        self.wait_for_element_visible(row_selector)
        self.wait_for_text(computer_name, row_selector)
        if introduced:
            self.wait_for_text(introduced, row_selector)
        if discontinued:
            self.wait_for_text(discontinued, row_selector)
        if company:
            self.wait_for_text(company, row_selector)