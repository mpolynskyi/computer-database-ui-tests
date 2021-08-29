class ComputersTablePage:
    add_new_computers_button = 'a#add'
    filter_by_name_button = 'input#searchsubmit'
    filter_by_computer_name_field = 'input#searchbox'
    alert_message = 'div[class*="alert-message warning"]'

    @staticmethod
    def table_row_by_computer_id(id):
        return f'//a[@href="/computers/{id}"]/../..'
