class Urls:
    computers_table = '/computers'
    create_new_computer_url = '/computers/new'

    @staticmethod
    def computer_url_by_id(id: int):
        return f"/computers/{id}"
