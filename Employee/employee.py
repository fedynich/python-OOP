class Employee:
    def __init__(self, name, email, year, skills):
        self.name = name
        self.email = email
        self.year = year
        self.skills = skills

    corporation = 'Portnov Computer School'

    def get_slack_profile(self, channel, workspace):
        return f"Name: {self.name} \nChannel: {channel} \nWorkplace: {workspace}"

    def move_story(self, status):
        return f"{self.name} moved Feature to status: {status}"


class SofwareDeveloper(Employee):
    def give_demo(self):
        return f"{self.name}: finished Demo"

    def move_story(self, status="Implemented"):
        return super().move_story(status)


class QA_Engineer(Employee):
    def is_demo_accepted(self, status):
        return f"Is {self.name} approved the Demo: {status}"

    def move_story(self, status='Tested'):
        return super().move_story(status)
