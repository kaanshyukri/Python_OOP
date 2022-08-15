from august_retake import Team
from unittest import TestCase, main


class TeamTest(TestCase):

    def test_init(self):
        cska = Team("cska")
        self.assertEqual("cska", cska.name)
        self.assertEqual({}, cska.members)

    def test_name_raises_error_number(self):
        cska = Team("Cska")
        with self.assertRaises(ValueError) as ex:
            cska.name = "Cska5"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        result = cska.add_member(**kwargs)
        expected = "Successfully added: Ivan, Stoyan, Gosho"
        self.assertEqual(expected, result)
        cska.add_member(**kwargs)
        new_kwargs = {"Ivan": 10}
        self.assertEqual("Successfully added: ", cska.add_member(**new_kwargs))

    def test_remove_member_not_in_team(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        result = cska.remove_member("Kaan")
        expected = "Member with name Kaan does not exist"
        self.assertEqual(expected, result)

    def test_remove_member_in_team(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        result = cska.remove_member("Ivan")
        expected = "Member Ivan removed"
        self.assertEqual(expected, result)
        expected = {"Stoyan": 11, "Gosho": 9}
        result = cska.members
        self.assertEqual(expected, result)

    def test_gt(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        levski = Team("levski")
        self.assertEqual(True, cska > levski)
        levski.add_member(**kwargs)
        self.assertFalse(cska.__gt__(levski))

    def test_len(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        self.assertEqual(3, cska.__len__())

    def test_add(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        levski = Team("levski")
        new_kwargs = {"Djaner": 20, "Kaan": 18}
        levski.add_member(**new_kwargs)
        result = str(cska.__add__(levski))
        expected = "Team name: cskalevski\n" \
                   "Member: Djaner - 20-years old\n" \
                   "Member: Kaan - 18-years old\n" \
                   "Member: Stoyan - 11-years old\n" \
                   "Member: Ivan - 10-years old\n" \
                   "Member: Gosho - 9-years old"
        self.assertEqual(expected, result)

    def test_str(self):
        cska = Team("cska")
        kwargs = {"Ivan": 10, "Stoyan": 11, "Gosho": 9}
        cska.add_member(**kwargs)
        new_kwargs = {"Djaner": 20, "Kaan": 18}
        cska.add_member(**new_kwargs)
        result = cska.__str__()
        expected = "Team name: cska\n" \
                   "Member: Djaner - 20-years old\n" \
                   "Member: Kaan - 18-years old\n" \
                   "Member: Stoyan - 11-years old\n" \
                   "Member: Ivan - 10-years old\n" \
                   "Member: Gosho - 9-years old"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()