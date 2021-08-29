from framework.pages.item_page import ItemDetailsPage
from framework.pages.computers_table_page import ComputersTablePage
from framework.urls import Urls
from .base_actions import BaseAction


class ItemActions(BaseAction):
    def _fill_computer_form(self,
                            computer_name: str = None,
                            introduced: str = None,
                            discontinued: str = None,
                            company: str = None):
        if computer_name:
            self.type(ItemDetailsPage.computer_name_field, computer_name)
        if introduced:
            self.type(ItemDetailsPage.introduced_field, introduced)
        if discontinued:
            self.type(ItemDetailsPage.discontinued_field, discontinued)
        if company:
            self.select_option_by_text(ItemDetailsPage.company_select, company)

    def create_computer(self,
                        computer_name: str = None,
                        introduced: str = None,
                        discontinued: str = None,
                        company: str = None,
                        click_save: bool = True):
        self.open(Urls.create_new_computer_url)
        self.wait_for_element_visible(ItemDetailsPage.computer_name_field)
        self._fill_computer_form(computer_name, introduced, discontinued, company)
        if click_save:
            self.click(ItemDetailsPage.create_this_computer_button)

    def edit_computer_by_id(self,
                            id: int = None,
                            new_computer_name: str = None,
                            new_introduced: str = None,
                            new_discontinued: str = None,
                            new_company: str = None,
                            click_save: bool = True):
        self.open(Urls.computer_url_by_id(id))
        self.wait_for_element_visible(ItemDetailsPage.computer_name_field)
        self._fill_computer_form(new_computer_name, new_introduced, new_discontinued, new_company)
        if click_save:
            self.click(ItemDetailsPage.save_this_computer_button)

    def delete_computer_by_id(self, id: int):
        self.open(Urls.computer_url_by_id(id))
        self.wait_for_element_visible(ItemDetailsPage.delete_this_computer_button)
        self.click(ItemDetailsPage.delete_this_computer_button)

    def wait_for_success_created_item_message(self, item_name: str):
        self.wait_for_text_visible(f"Done ! Computer {item_name} has been created", ComputersTablePage.alert_message)

    def wait_for_success_updated_item_message(self, item_name: str):
        self.wait_for_text_visible(f"Done ! Computer {item_name} has been updated", ComputersTablePage.alert_message)

    def wait_for_success_delete_item_message(self, item_name: str):
        self.wait_for_text_visible(f"Done ! Computer {item_name} has been deleted", ComputersTablePage.alert_message)

    def wait_for_computer_name_alert_message(self, error_message: str):
        self.wait_for_text_visible(error_message, ItemDetailsPage.computer_name_alert())

    def wait_for_introduced_alert(self, error_message: str):
        self.wait_for_text_visible(error_message, ItemDetailsPage.introduced_alert())

    def wait_for_discontinued_alert(self, error_message: str):
        self.wait_for_text_visible(error_message, ItemDetailsPage.discontinued_alert())
