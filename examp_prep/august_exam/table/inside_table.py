from august_exam.table.table import Table


class InsideTable(Table):
    start_number = 1
    end_number = 50

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)
