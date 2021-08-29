class ItemDetailsPage:
    computer_name_field = 'input#name'
    introduced_field = 'input#introduced'
    discontinued_field = 'input#discontinued'
    company_select = 'select#company'

    create_this_computer_button = 'input[value="Create this computer"]'
    save_this_computer_button = 'input[value="Save this computer"]'
    delete_this_computer_button = 'input[value="Delete this computer"]'

    general_alert = 'span.help-inline'


    @staticmethod
    def computer_name_alert():
        return f'{ItemDetailsPage.computer_name_field} ~ {ItemDetailsPage.general_alert}'

    @staticmethod
    def introduced_alert():
        return f'{ItemDetailsPage.introduced_field} ~ {ItemDetailsPage.general_alert}'

    @staticmethod
    def discontinued_alert():
        return f'{ItemDetailsPage.discontinued_field} ~ {ItemDetailsPage.general_alert}'
