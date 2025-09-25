#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            # store in title case
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

    # job property
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        elif value == "Unemployed":  # default fallback, no print
            self._job = "Unemployed"
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"
