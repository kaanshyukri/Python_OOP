from unittest import TestCase, main
from examp_prep.apr import Student


class StudentTest(TestCase):

    def test_init(self):
        student = Student("Ivan")
        self.assertEqual("Ivan", student.name)
        self.assertEqual({}, student.courses)
        new_student = Student("Gosho", {"English": ["yes", "no"]})
        self.assertEqual("Gosho", new_student.name)
        self.assertEqual({"English": ["yes", "no"]}, new_student.courses)

    def test_enroll_course_added(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        result = new_student.enroll("English", ["okay", "not okay"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)
        self.assertEqual({"English": ["yes", "no", "okay", "not okay"], "Turkish": ["tamam"]}, new_student.courses)

    def test_enroll_course_and_notes_added(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        result = new_student.enroll("German", ["ya", "ich bin"], "Y")
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)
        self.assertEqual({"English": ["yes", "no"], "Turkish": ["tamam"], "German": ["ya", "ich bin"]}, new_student.courses)

        result = new_student.enroll("Python", ["str", "int"])
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)

        result = new_student.courses
        expected = {"English": ["yes", "no"], "Turkish": ["tamam"], "German": ["ya", "ich bin"], "Python":["str", "int"]}
        self.assertEqual(expected, result)

    def test_enroll_added_course(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        result = new_student.enroll("Python", ["int", "str"], "K")
        expected = "Course has been added."
        self.assertEqual(expected, result)
        self.assertEqual({"English": ["yes", "no"], "Turkish": ["tamam"], "Python": []}, new_student.courses)

    def test_add_notes_raises_exception(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        with self.assertRaises(Exception) as er:
            new_student.add_notes("Python", "okay")
        self.assertEqual("Cannot add notes. Course not found.", str(er.exception))

    def test_add_notes_update_notes(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        result = new_student.add_notes("English", "okay")
        expected = "Notes have been updated"
        self.assertEqual(expected, result)
        self.assertEqual({"English": ["yes", "no", "okay"], "Turkish": ["tamam"]}, new_student.courses)

    def test_leave_course_raises_exception(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        with self.assertRaises(Exception) as er:
            new_student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(er.exception))

    def test_leave_course_remove_course(self):
        new_student = Student("Gosho", {"English": ["yes", "no"], "Turkish": ["tamam"]})
        result = new_student.leave_course("Turkish")
        expected = "Course has been removed"
        self.assertEqual(expected, result)
        self.assertEqual({"English": ["yes", "no"]}, new_student.courses)


if __name__ == "__main__":
    main()