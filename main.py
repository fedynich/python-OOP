import Employee.employee as employee


def init_employees():
    qa_skills = ['manual testing', 'test cases developing', 'test cases execution']
    dev_skills = ['programming', 'programming languages', 'databases']

    maria = employee.QA_Engineer('Maria', 'maria@portnov.com', 2020, qa_skills)
    katya = employee.QA_Engineer('Maria', 'kate@portnov.com', 2020, qa_skills)
    denis = employee.SofwareDeveloper('Denis', 'denis@portnov.com', 2019, dev_skills)

    print(isinstance(maria, employee.Employee))
    print(isinstance(denis, employee.QA_Engineer))
    print('')

    print(denis.move_story())
    print(katya.is_demo_accepted(False))

    print(denis.move_story())
    print(maria.is_demo_accepted(True))

    print(maria.move_story())




if __name__ == '__main__':
    init_employees()