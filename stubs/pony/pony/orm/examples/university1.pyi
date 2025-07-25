from _typeshed import Incomplete
from decimal import Decimal as Decimal

from pony.orm.core import Database, Entity

db: Database

class Department(Entity):
    number: Incomplete
    name: Incomplete
    groups: Incomplete
    courses: Incomplete

class Group(Entity):
    number: Incomplete
    major: Incomplete
    dept: Incomplete
    students: Incomplete

class Course(Entity):
    name: Incomplete
    semester: Incomplete
    lect_hours: Incomplete
    lab_hours: Incomplete
    credits: Incomplete
    dept: Incomplete
    students: Incomplete

class Student(Entity):
    id: Incomplete
    name: Incomplete
    dob: Incomplete
    tel: Incomplete
    picture: Incomplete
    gpa: Incomplete
    group: Incomplete
    courses: Incomplete

params: dict[str, dict[str, str | bool] | dict[str, str | int]]

def populate_database() -> None: ...
def print_students(students) -> None: ...
def test_queries() -> None: ...
