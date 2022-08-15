from august_exam.table.table import Table


class OutsideTable(Table):
    start_number = 51
    end_number = 100

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

