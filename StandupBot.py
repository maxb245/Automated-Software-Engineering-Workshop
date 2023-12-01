from datetime import datetime, timedelta

class Meeting:
    def __init__(self, title, date_time):
        self.title = title
        self.date_time = date_time
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def display_info(self):
        print(f"\nMeeting: {self.title}")
        print(f"Date and Time: {self.date_time}")
        print("Attendees:", ", ".join(self.attendees))


class StandupBot:
    def __init__(self, team_members):
        self.team_members = team_members
        self.updates = {}
        self.meetings = []

    def run_standup(self):
        print("Welcome to the Standup Bot!")
        for member in self.team_members:
            update = input(f"{member}, please share your standup update: ")
            self.updates[member] = update

    def schedule_meeting(self, title, date_time):
        meeting = Meeting(title, date_time)
        self.meetings.append(meeting)
        print(f"\nMeeting scheduled: {title}, {date_time}")

    def list_meetings(self):
        print("\nScheduled Meetings:")
        for meeting in self.meetings:
            meeting.display_info()

    def print_standup_summary(self):
        print("\nStandup Summary:")
        for member, update in self.updates.items():
            print(f"{member}: {update}")


if __name__ == "__main__":
    team_members = ["Alice", "Bob", "Charlie"]
    standup_bot = StandupBot(team_members)

    # Run standup
    standup_bot.run_standup()

    # Schedule meetings
    standup_bot.schedule_meeting("Sprint Planning", datetime(2023, 12, 1, 10, 0))
    standup_bot.schedule_meeting("Code Review", datetime(2023, 12, 3, 14, 30))

    # List scheduled meetings
    standup_bot.list_meetings()

    # Print standup summary
    standup_bot.print_standup_summary()
