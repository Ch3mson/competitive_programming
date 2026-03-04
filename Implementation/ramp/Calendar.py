

# create a nested hash map 
# key: event id 
# value: another json/dictionary 
#.  title: str
#   start_time: datetime 
# ... etc. 

"""
Add a new event to the calendar.

:param title: Name of the event.
:param start_time: Start datetime of the event.
:param end_time: End datetime of the event.
:param description: Optional description of the event.
:param location: Optional location of the event.
:param attendees: Optional list of attendee identifiers (emails/user IDs).
:return: Unique event ID for the created event.
"""

"""
Edit an existing event's details.

:param event_id: Unique identifier of the event.
:param title: New title (optional).
:param start_time: New start time (optional).
:param end_time: New end time (optional).
:param description: New description (optional).
:param location: New location (optional).
:param attendees: Updated list of attendees (optional).
:return: True if the event was successfully updated, False otherwise.
"""

"""
Delete an event from the calendar.

:param event_id: Unique identifier of the event to delete.
:return: True if the event was successfully deleted, False otherwise.
----------------------------------------------------------------
Likely Extensions in an Interview Setting
Add a search method

- Prevent invalid event times (done)
- Add getEvent method (done)
- List upcoming events for an attendee (month, week, view, etc.)
- Delete all events for a given attendee (done)
- Recurring events (basic) - repeat x days n times

Not full iCalendar rules — just “repeat every X days N times”

Lets them see loop logic and multiple inserts.
"""
import uuid
import datetime
import unittest

from collections import defaultdict
from typing import Optional
from sortedcontainers import SortedList

class CalendarApp:
    def __init__(self):
        self.calendar = {}
        self.attendee_events = defaultdict(SortedList)
    
    def addEvent(
        self,
        title: str,
        start_time: datetime,
        end_time: datetime,
        description: str = "",
        location: str = "",
        attendees: list[str] = []
    ) -> str:
        event_id = uuid.uuid4()

        if event_id in self.calendar or end_time < start_time:
            return None

        event_info = {
            "title": title,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "description": description,
            "location": location,
            "attendees": attendees
        }

        self.calendar[event_id] = event_info

        for attendee in attendees:
            self.attendee_events[attendee].add((start_time, event_id))
        
        return event_id

    def editEvent(
        self,
        event_id: Optional[str] = None,
        title: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        attendees: Optional[list[str]] = None
    ) -> bool:
        if event_id not in self.calendar:
            return False 
        
        new_event_info = self.calendar[event_id]

        if title is not None:
            new_event_info["title"] = title
        
        if start_time is not None:
            new_event_info["start_time"] = start_time.isoformat()
        
        if end_time is not None:
            new_event_info["end_time"] = end_time.isoformat()
        
        if description is not None:
            new_event_info["description"] = description 
        
        if location is not None:
            new_event_info["location"] = location 
        
        if attendees is not None:
            new_event_info["attendees"] = attendees
        
        return True
    
    def getEvent(self, event_id):
        if event_id not in self.calendar:
            return None 
    
        return self.calendar[event_id]

    def deleteEvent(
        self,
        event_id: str
    ) -> bool:
        if event_id not in self.calendar:
            return False 
        
        self.calendar.pop(event_id)
        return True

    def deleteAttendeeEvents(self, attendee) -> bool:
        if attendee not in self.attendee_events:
            return False 
    
        for _, event_id in self.attendee_events[attendee]:
            self.deleteEvent(event_id)
        
        self.attendee_events.pop(attendee)
        return True

class TestCalendarApp(unittest.TestCase):
    def setup(self):
        self.app = CalendarApp()
        self.sample_start = datetime.datetime(2025, 8, 9)
        self.sample_end = datetime.datetime(2025, 8, 20)
        self.title = "[Test] Title"
        self.description = "[Unittest] For testing"
        self.location = "Virtual"
        self.attendees = ["Me", "You", "Ramp"]
    
    def test_add_event_success_all(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert isinstance(event_id, uuid.UUID)

        assert self.app.calendar[event_id]["title"] == self.title
        assert self.app.calendar[event_id]["start_time"] == self.sample_start.isoformat()
        assert self.app.calendar[event_id]["end_time"] == self.sample_end.isoformat()
        assert self.app.calendar[event_id]["description"] == self.description 
        assert self.app.calendar[event_id]["location"] == self.location 
        assert self.app.calendar[event_id]["attendees"] == self.attendees
    
    def test_add_event_no_optional(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end)

        assert isinstance(event_id, uuid.UUID)

        assert self.app.calendar[event_id]["title"] == self.title
        assert self.app.calendar[event_id]["start_time"] == self.sample_start.isoformat()
        assert self.app.calendar[event_id]["end_time"] == self.sample_end.isoformat()

        assert "description" not in self.app.calendar 
        assert "location" not in self.app.calendar
        assert "attendees" not in self.app.calendar
    
    def test_add_event_some_optional(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, description=self.description, attendees=self.attendees)

        assert isinstance(event_id, uuid.UUID)

        assert self.app.calendar[event_id]["title"] == self.title
        assert self.app.calendar[event_id]["start_time"] == self.sample_start.isoformat()
        assert self.app.calendar[event_id]["end_time"] == self.sample_end.isoformat()

        assert self.app.calendar[event_id]["description"] == self.description 
        assert "location" not in self.app.calendar
        assert self.app.calendar[event_id]["attendees"] == self.attendees
    
    def test_add_event_with_invalid_dates(self):
        self.setup()
        event_id = self.app.addEvent(self.title, datetime.datetime(2025, 3, 4), datetime.datetime(2024, 4, 5), description=self.description, attendees=self.attendees)
        
        assert event_id is None
    
    def test_edit_event_title(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["title"] == self.title

        self.app.editEvent(event_id, title="[NEW] title")

        assert self.app.calendar[event_id]["title"] == "[NEW] title"
    
    def test_edit_event_start_time(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["start_time"] == self.sample_start.isoformat()

        self.app.editEvent(event_id, start_time=datetime.datetime(2024, 8, 7))

        assert self.app.calendar[event_id]["start_time"] == datetime.datetime(2024, 8, 7).isoformat()
    
    def test_edit_event_end_time(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["end_time"] == self.sample_end.isoformat()

        self.app.editEvent(event_id, end_time=datetime.datetime(2024, 8, 7))

        assert self.app.calendar[event_id]["end_time"] == datetime.datetime(2024, 8, 7).isoformat()
    
    def test_edit_event_description(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["description"] == self.description

        self.app.editEvent(event_id, description="[NEW] Description")
        
        assert self.app.calendar[event_id]["description"] == "[NEW] Description"
    
    def test_edit_event_location(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["location"] == self.location

        self.app.editEvent(event_id, location="[NEW] Location")
        
        assert self.app.calendar[event_id]["location"] == "[NEW] Location"
    
    def test_edit_event_attendees(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["attendees"] == self.attendees

        self.app.editEvent(event_id, attendees=["a", "b"])
        
        assert self.app.calendar[event_id]["attendees"] == ["a", "b"]
    
    def test_edit_multiple(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)

        assert self.app.calendar[event_id]["attendees"] == self.attendees
        assert self.app.calendar[event_id]["title"] == self.title
        assert self.app.calendar[event_id]["location"] == self.location

        self.app.editEvent(event_id, title="[NEW] title", location="[NEW] Location", attendees=["a", "b"])

        assert self.app.calendar[event_id]["attendees"] == ["a", "b"]
        assert self.app.calendar[event_id]["title"] == "[NEW] title"
        assert self.app.calendar[event_id]["location"] == "[NEW] Location"
    
    def test_delete_attendee_events(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)
        
        for attendee in self.attendees:
            assert self.app.attendee_events[attendee][0] == (self.sample_start, event_id)
        
        assert self.app.deleteAttendeeEvents("Me") == True
        
        assert "Me" not in self.app.attendee_events
        assert event_id not in self.app.calendar
    
    def test_delete_nonexistent_attendee(self):
        self.app = CalendarApp()
        assert self.app.deleteAttendeeEvents("Me") == False
    
    def test_get_existent_event(self):
        self.setup()
        event_id = self.app.addEvent(self.title, self.sample_start, self.sample_end, self.description, self.location, self.attendees)
        
        event_info = self.app.getEvent(event_id)
        assert event_info == { "title": self.title, "start_time": self.sample_start.isoformat(), "end_time": self.sample_end.isoformat(), "description": self.description, "location": self.location, "attendees": self.attendees}

    def test_get_nonexistent_event(self):
        event_id = uuid.uuid4()
        self.app = CalendarApp()
        
        event_info = self.app.getEvent(event_id)
        assert event_info is None

if __name__ == "__main__":
    unittest.main()
