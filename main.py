import random
class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class ApplicationSubmittedEvent(Event):
    def __init__(self, applicant_name, job_title):
        super().__init__("application_submitted", {"applicant_name": applicant_name, "job_title": job_title})

class ApplicationRejectedEvent(Event):
    def __init__(self, applicant_name, job_title):
        super().__init__("application_rejected", {"applicant_name": applicant_name, "job_title": job_title})

class ApplicationAcceptedEvent(Event):
    def __init__(self, applicant_name, job_title):
        super().__init__("application_accepted", {"applicant_name": applicant_name, "job_title": job_title})

communication_queue = []

class Applicant:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def apply_for_job(self, company, job_title):
        event = ApplicationSubmittedEvent(f"{self.first_name} {self.last_name}", job_title)
        communication_queue.append(event)
        print('Event', event.name, 'emitted!')
        company.handle_application(event)

class Company:
    def __init__(self, name):
        self.name = name

    def handle_application(self, event):
        print(f"Received application from: {event.payload['applicant_name']} for position: {event.payload['job_title']}")
        if random.choice([True, False]):
            confirmation_event = ApplicationAcceptedEvent(event.payload["applicant_name"], event.payload["job_title"])
            communication_queue.append(confirmation_event)
            print('Event', confirmation_event.name, 'emitted!')
        else:
            rejection_event = ApplicationRejectedEvent(event.payload["applicant_name"], event.payload["job_title"])
            communication_queue.append(rejection_event)
            print('Event', rejection_event.name, 'emitted!')

if __name__ == "__main__":
    Maksud = Applicant("Maksud", "Temel", "Maksud@.com")
    Iskhak = Applicant("Iskhak", "Tolibaev", "Iskhak@.com")
    tech_company = Company("Google.")
    Maksud.apply_for_job(tech_company, "Software Engineer")
    Iskhak.apply_for_job(tech_company, "Data Scientist")

