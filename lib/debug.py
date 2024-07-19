#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee

import ipdb
import random
import faker

fake = faker.Faker()

def reset_database():
    Department.drop_table()
    Department.create_table()

    Employee.drop_table()
    Employee.create_table()

    payroll = Department.create("Payroll", "Building A, 5th Floor")
    hr = Department.create("Human Resources", "Building C, East Wing")

    departments = [payroll, hr]

    job_titles = ["Accountant", "Manager", "Benefits Coordinator", "New Hires Coordinator"]

    for _ in range(5):
        Employee.create(fake.first_name(), random.choice(job_titles), random.choice(departments).id)

reset_database()
ipdb.set_trace()
