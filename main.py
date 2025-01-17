import user

import profile
from datetime import datetime, timedelta
from message import UNREAD_STATUS, Message
from user import User, STANDARD_TIER_NAME, PLUS_TIER_NAME, JOB_APPLIED_DELETED_BY_AUTHOR_MESSAGE
from collections import deque
import textwrap
from job import Job
from profile import Profile
from experience import Experience
from education import Education
from job_application import Job_Application
from datetime import datetime, timedelta

SKILLS = ["Communication", "Development", "Marketing", "Testing", "Equestrian"]
LANGUAGES = ["English", "Spanish"]
GO_BACK_KEY = "b"
TEXT_WIDTH = 120
MESSAGE_PREVIEW_WIDTH = 40

GO_BACK_MESSAGE = "To go back to the previous screen, press 'b': "
UNDER_CONSTRUCTION_MESSAGE = "Under Construction."
SELECT_NEW_SKILL_MESSAGE = "Select a new skill: "
TYPE_USERNAME_MESSAGE = "Username: "
TYPE_PASSWORD_MESSAGE = "Password: "
TYPE_FIRST_NAME_MESSAGE = "First Name: "
TYPE_LAST_NAME_MESSAGE = "Last Name: "
EDIT_PROFILE_MESSAGE = "Please select what field you would like to edit: "
TYPE_TITLE_MESSAGE = "Title(e.g. 3rd year computer science student: "
TYPE_MAJOR_MESSAGE = "Major: "
TYPE_NAME_OF_UNIVERSITY = "Current university: "
TYPE_SUMMARY_MESSAGE = "Summary: "
UPDATE_WARRNING = "Warning: You will be updating this field\n"
LOGIN_SUCCESSFUL_MESSAGE = "You have successfully logged in"
USER_CREATED_MESSAGE = "User created successfully."
SELECT_OPTION_MESSAGE = "Please, choose which action you would like to take: "
SELECT_LANGUAGE_MESSAGE = "Please, choose which language you want to use: "
VIDEO_PLAYNG_MESSAGE = "Video is now playing"
INVALID_INPUT_ERROR_MESSAGE = "Please type a valid value."
INVALID_SKILL_ERROR_MESSAGE = "Error: Please select a valid skill between 0 and 4"
LOGIN_ERROR_MESSAGE = "Incorrect username / password, please try again"
CONTACT_FOUND_MESSAGE = "They are a part of the InCollege system."
CONTACT_NOT_FOUND_MESSAGE = "They are NOT a part of the InCollege system yet."
JOB_SAVED_MESSAGE = "Job has been saved!"
TYPE_JOB_TITLE_MESSAGE = "Enter title of Job: "
TYPE_JOB_DESCRIPTION_MESSAGE = "Enter a brief description of Job: "
TYPE_JOB_EMPLOYER_MESSAGE = "Employer: "
TYPE_JOB_LOCATION_MESSAGE = "Location of Job: "
TYPE_JOB_SALARY_MESSAGE = "Estimated Salary: "
TYPE_JOB_TITLE_MESSAGE = "Job Title: "
TYPE_DATE_STARTED_MESSAGE = "Date Started: "
TYPE_DATE_ENDED_MESSAGE = "Date Ended: "
HELP_CENTER_MESSAGE = "We're here to help!"
GENERAL_OPTION_ABOUT_MESSAGE = "In College: Welcome to In College, the world's largest " \
                               "college student network with many users in many countries and territories worldwide"
PRESS_MESSAGE = "In College Pressroom: Stay on top of the latest news, updates, " \
                "and reports!"
EXPERIENCE_ADDED_MESSAGE = "Experience added succesfully!"
EXPERIENCE_REMOVED_MESSAGE = "Experience removed successful!"
TYPE_SCHOOL_NAME_MESSAGE = "School Name: "
TYPE_DEGREE_MESSAGE = "Degree: "
TYPE_YEARS_ATTENDED_MESSAGE = "Years Attended: "
EDUCATION_ADDED_MESSAGE = "Education added succesfully!"
EDUCATION_REMOVED_MESSAGE = "Education removed successful!"
NO_PROFILE_YET_MESSAGE = "You do not have a profile to view yet. " \
                         "Please return to dashboard and select 'Edit Profile'"
CONNECTION_REQUESTED_MESSAGE = "Connection requested!"
CONNECTION_ACEPTED_MESSAGE = "Connection acepted!"
CONNECTION_REJECTED_MESSAGE = "Connection rejected."
DISCONNECTED_MESSAGE = "Disconnected."
PENDING_FRIEND_REQUEST_MESSAGE = "You have a pending friend request."
UNREAD_MESSAGES_MESSAGE = "You have messages waiting for you."
JOB_ADDED_TO_SAVED_JOBS_MESSAGE = "Job added to saved jobs."
JOB_REMOVED_FROM_SAVED_JOBS_MESSAGE = "Job removed from saved jobs."
JOB_DELETED_MESSAGE = "Job deleted."
JOB_APPLIED_MESSAGE = "Job applied."
TYPE_GRADUATION_DATE_MESSAGE = "Type graduation date: "
TYPE_START_DATE_MESSAGE = "Type start date: "
TYPE_COVER_LETTER_MESSAGE = "Type you are a fit for this job: "
SELECT_SUSCRIPTION_TYPE = "Select suscription type: "
TYPE_MESSAGE_CONTENT = "Type the message content: "
MESSAGE_SENT_MESSAGE = "Message sent successfully!"
MESSAGE_DELETED_MESSAGE = "Message deleted."
ONLY_CAN_MESSAGE_YOUR_FRIENDS_ERROR_MESSAGE = "I'm sorry, you are not friends with that person."
DO_NOT_FORGET_PROFILE_MESSAGE =  "Don't forget to create a profile."
LAST_APPLICATION_SEVEN_DAYS_AGO_MESSAGE = "Remember – you're going to want to \
have a job when you graduate. Make sure that you start to apply for jobs today!"

CREATE_PROFILE_NOTIF = "Don't forget to create a profile!"
APPLIED_OVER_SEVEN_DAYS = "Remember – you're going to want to have a job when you graduate. " \
                     "Make sure that you start to apply for jobs today!"
MESSAGES_WAITING = "You have messages waiting for you."

def screen(method):
    def wrapper(app, *args):
        app.history.append((method.__name__, args))
        print(f"\n{'=' * TEXT_WIDTH}\n")
        return method(app, *args)

    return wrapper


class App:
    SUCCESS_STORY_FILE_NAME = "./resources/success_story.txt"
    COPYRIGHT_NOTICE_FILE_NAME = "./resources/copyright_notice.txt"
    ABOUT_MESSAGE_FILE_NAME = "./resources/about_message.txt"
    ACCESSIBILITY_MESSAGE_FILE_NAME = "./resources/accessibility_message.txt"
    USER_AGREEMENT_FILE_NAME = "./resources/user_agreement.txt"
    PRIVACY_POLICY_FILE_NAME = "./resources/privacy_policy.txt"
    COOKIE_POLICY_FILE_NAME = "./resources/cookie_policy.txt"
    COPYRIGHT_POLICY_FILE_NAME = "./resources/copyright_policy.txt"
    BRAND_POLICY_FILE_NAME = "./resources/brand_policy.txt"

    success_story = ""
    copyright_notice = ""
    about_message = ""
    accessibility_message = ""
    user_agreement = ""
    privacy_policy = ""
    cookie_policy = ""
    copyright_policy = ""
    brand_policy = ""

    def __init__(self):
        self.history = deque()
        self.current_user = None
        self.search_term = ""

    @staticmethod
    def load_success_story():
        with open(App.SUCCESS_STORY_FILE_NAME) as success_story_file:
            App.success_story = success_story_file.read()

    @staticmethod
    def load_copyright_notice():
        with open(App.COPYRIGHT_NOTICE_FILE_NAME) as copyright_notice_file:
            App.copyright_notice = copyright_notice_file.read()

    @staticmethod
    def load_about_message():
        with open(App.ABOUT_MESSAGE_FILE_NAME) as about_message_file:
            App.about_message = about_message_file.read()

    @staticmethod
    def load_accessibility_message():
        with open(App.ACCESSIBILITY_MESSAGE_FILE_NAME) as accessability_message_file:
            App.accessibility_message = accessability_message_file.read()

    @staticmethod
    def load_user_agreement():
        with open(App.USER_AGREEMENT_FILE_NAME) as user_agreement_file:
            App.user_agreement = user_agreement_file.read()

    @staticmethod
    def load_privacy_policy():
        with open(App.PRIVACY_POLICY_FILE_NAME) as privacy_policy_file:
            App.privacy_policy = privacy_policy_file.read()

    @staticmethod
    def load_cookie_policy():
        with open(App.COOKIE_POLICY_FILE_NAME) as cookie_policy_file:
            App.cookie_policy = cookie_policy_file.read()

    @staticmethod
    def load_copyright_policy():
        with open(App.COPYRIGHT_POLICY_FILE_NAME) as copyright_policy_file:
            App.copyright_policy = copyright_policy_file.read()

    @staticmethod
    def load_brand_policy():
        with open(App.BRAND_POLICY_FILE_NAME) as brand_policy_file:
            App.brand_policy = brand_policy_file.read()

    def go_back(self):
        """
        Function to run the previous function name saved in the
        history stack.
        """
        try:
            self.history.pop()
            function_name, args = self.history.pop()
        except IndexError:
            return None

        back = getattr(self, function_name)
        return back(*args)

    def reload_screen(self):
        """
        Function to reload the last function name saved in the
        history stack.
        """
        if len(self.history) == 0:
            return None

        function_name, args = self.history.pop()
        current_screen = getattr(self, function_name)
        return current_screen(*args)

    def handle_input(self, prompt, input_type=str):
        """
        :param key: The user's input
        :param prompt: The prompt to pass to handle_input recursively in the event of an error
        :param input_type: The expected input type
        :return: The user's input
        """
        key = input(prompt)
        if input_type != int or key.isnumeric() or key == GO_BACK_KEY:
            return key

        print(INVALID_INPUT_ERROR_MESSAGE)
        return self.handle_input(prompt, input_type)

    def handle_go_back(self, choice):
        if choice == GO_BACK_KEY:
            return self.go_back()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def add_experience_screen(self):
        print("Add Experience", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        profile = self.current_user.profile

        title = input(TYPE_JOB_TITLE_MESSAGE)
        employer = input(TYPE_JOB_EMPLOYER_MESSAGE)
        date_started = input(TYPE_DATE_STARTED_MESSAGE)
        date_ended = input(TYPE_DATE_ENDED_MESSAGE)
        location = input(TYPE_JOB_LOCATION_MESSAGE)
        description = input(TYPE_JOB_DESCRIPTION_MESSAGE)

        experience = Experience(
            title,
            employer,
            date_started,
            date_ended,
            location,
            description
        )

        error_message = profile.add_experience(experience)
        if error_message:
            print(error_message)
        else:
            print(EXPERIENCE_ADDED_MESSAGE)

        return self.go_back()

    @screen
    def delete_experience_screen(self):
        print("Delete Experience", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        print("Which experience would you like to delete?")
        for index, experience in enumerate(self.current_user.profile.experience):
            print(f"{index}. {experience.title} at {experience.employer} ", end="")
            print(f"{experience.date_started} - {experience.date_ended}")
        print("b. Go Back")

        experience_index = self.handle_input(SELECT_OPTION_MESSAGE, int)
        if experience_index == GO_BACK_KEY:
            return self.go_back()

        experience_index = int(experience_index)
        error_message = self.current_user.profile.delete_experience(experience_index)
        if error_message:
            print(error_message)
        else:
            print(EXPERIENCE_REMOVED_MESSAGE)

        return self.reload_screen()

    @screen
    def experience_screen(self):
        print("Experience", end="\n\n")
        print("0. Add experience")
        print("1. Delete experience")
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        elif option == "0":
            return self.add_experience_screen()

        elif option == "1":
            return self.delete_experience_screen()

        return self.reload_screen()

    @screen
    def education_screen(self):
        print("Education", end="\n\n")
        print("0. Add education")
        print("1. Delete education")
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        elif option == "0":
            return self.add_education_screen()

        elif option == "1":
            return self.delete_education_screen()

        return self.reload_screen()

    @screen
    def add_education_screen(self):
        print("Add Education", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        schoolName = input(TYPE_SCHOOL_NAME_MESSAGE)
        degree = input(TYPE_DEGREE_MESSAGE)
        yearsAttended = input(TYPE_YEARS_ATTENDED_MESSAGE)

        education = Education(
            schoolName,
            degree,
            yearsAttended,
        )

        error_message = self.current_user.profile.add_education(education)
        if error_message:
            print(error_message)
        else:
            print(EDUCATION_ADDED_MESSAGE)

        return self.go_back()

    @screen
    def delete_education_screen(self):
        print("Delete Education", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        print("Which education section would you like to delete?")
        for index, education in enumerate(self.current_user.profile.education):
            print(f"{index}. {education.degree} at {education.school_name} ", end="")
            print(education.years_attended)
        print("b. Go back")

        education_index = self.handle_input(SELECT_OPTION_MESSAGE, int)
        if education_index == GO_BACK_KEY:
            return self.go_back()

        education_index = int(education_index)
        error_message = self.current_user.profile.delete_education(education_index)
        if error_message:
            print(error_message)
        else:
            print(EDUCATION_REMOVED_MESSAGE)

        return self.reload_screen()

    @screen
    def edit_profile_title_screen(self):
        print("Edit profile title", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        if self.current_user.profile.title:
            print(f"Current title: {self.current_user.profile.title}")
            print(UPDATE_WARRNING)

        self.current_user.profile.title = input(TYPE_TITLE_MESSAGE)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_major_screen(self):
        print("Edit profile major", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        if self.current_user.profile.major:
            print(f"Current major: {self.current_user.profile.major}")
            print(UPDATE_WARRNING)

        major = input(TYPE_MAJOR_MESSAGE)
        self.current_user.profile.major = str.title(major)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_university_screen(self):
        print("Edit profile university", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        if self.current_user.profile.university:
            print(f"Current university: {self.current_user.profile.university}")
            print(UPDATE_WARRNING)

        university = input(TYPE_NAME_OF_UNIVERSITY)
        self.current_user.profile.university = str.title(university)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_summary_screen(self):
        print("Edit profile summary", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        if self.current_user.profile.about:
            print(f"Current summary: {self.current_user.profile.about}")
            print(UPDATE_WARRNING)

        self.current_user.profile.about = input(TYPE_SUMMARY_MESSAGE)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_screen(self):
        print("Edit Profile", end="\n\n")
        print("0. Title")
        print("1. Major")
        print("2. University Name")
        print("3. Summary")
        print("4. Experience")
        print("5. Education")
        print("b. Go Back")
        option = self.handle_input(EDIT_PROFILE_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.edit_profile_title_screen()
        elif option == "1":
            return self.edit_profile_major_screen()
        elif option == "2":
            return self.edit_profile_university_screen()
        elif option == "3":
            return self.edit_profile_summary_screen()
        elif option == "4":
            return self.experience_screen()
        elif option == "5":
            return self.education_screen()

        return self.reload_screen()

    @screen
    def show_profile_screen(self, user):
        print("Profile", end="\n\n")
        profile = user.profile

        if profile:
            print(user.first_name, user.last_name)
            print("Title: ", profile.title)
            print("Major: ", profile.major)
            print("University: ", profile.university)
            print("Summary: ", profile.about)
            print("\nEXPERIENCE:\n")
            for experience in profile.experience:
                print("\tJob Title: ", experience.title)
                print("\tEmployer: ", experience.employer)
                print("\tDate Started: ", experience.date_started)
                print("\tDate Ended: ", experience.date_ended)
                print("\tLocation: ", experience.location)
                print("\tDescription:", experience.description)
                print("==========================")

            print("\nEDUCATION:\n")
            for education in profile.education:
                print("\tUniversity: ", education.school_name)
                print("\tDegree: ", education.degree)
                print("\tYears Attended:", education.years_attended)
                print("==========================")
        elif user == self.current_user:
            print(NO_PROFILE_YET_MESSAGE)

        option = self.handle_input(GO_BACK_MESSAGE)
        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def register_user_screen(self):
        print("Create Account", end="\n\n")
        print("Select your suscription type: ")
        print("0. Standard to send messages to friends")
        print("1. Plus to send messages to everyone for $10/month")
        print("b. Go back")
        option = self.handle_input(SELECT_SUSCRIPTION_TYPE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            user_tier = STANDARD_TIER_NAME
        elif option == "1":
            user_tier = PLUS_TIER_NAME
        else:
            return self.reload_screen()

        first_name = input(TYPE_FIRST_NAME_MESSAGE)
        last_name = input(TYPE_LAST_NAME_MESSAGE)
        username = input(TYPE_USERNAME_MESSAGE)
        password = input(TYPE_PASSWORD_MESSAGE)
        user = User(username, password, first_name, last_name, LANGUAGES[0], user_tier)

        error_message = user.save()
        if error_message == None:
            user.broadcast_new_user_notification()
            print(USER_CREATED_MESSAGE)
        else:
            print(error_message)

        return self.go_back()

    @screen
    def under_construction_screen(self):
        print(UNDER_CONSTRUCTION_MESSAGE, end="\n\n")
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def new_skills_screen(self):
        print("Learn a New Skill", end="\n\n")
        print(*[f"{index}: {skill}" for index, skill in enumerate(SKILLS)], sep="\n")
        print("b. Go back")
        option = self.handle_input(SELECT_NEW_SKILL_MESSAGE, int)

        if option == GO_BACK_KEY:
            return self.go_back()

        skill = int(option)
        if skill in range(len(SKILLS)):
            return self.under_construction_screen()

        print(f"\n{INVALID_SKILL_ERROR_MESSAGE}")
        return self.reload_screen()

    @screen
    def find_someone_screen(self):
        print("Find Someone You Know", end="\n\n")
        search_first = input(TYPE_FIRST_NAME_MESSAGE)
        search_last = input(TYPE_LAST_NAME_MESSAGE)
        user = User.find_by_name(search_first, search_last)

        if user == None:
            print(CONTACT_NOT_FOUND_MESSAGE)
            return self.go_back()

        print(CONTACT_FOUND_MESSAGE)
        if self.current_user != None:
            return self.go_back()

        # Removes this screen from the history
        self.history.pop()
        return self.join_your_friends_screen()

    @screen
    def join_your_friends_screen(self):
        print("Connect", end="\n\n")
        print("0. Login to an existing account to connect!")
        print("1. Sign up and join your friends!")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.login_screen()
        elif option == "1":
            return self.register_user_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def login_screen(self):
        print("Please enter your login information: ", end="\n\n")
        username = input(TYPE_USERNAME_MESSAGE)
        password = input(TYPE_PASSWORD_MESSAGE)
        user = User.login(username, password)
        if not user:
            print(LOGIN_ERROR_MESSAGE)
            return self.go_back()

        self.current_user = user
        print(LOGIN_SUCCESSFUL_MESSAGE)
        # Removes this screen from the history
        self.history.pop()
        return self.user_dashboard()

    @screen
    def play_video(self):
        print(VIDEO_PLAYNG_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def job_menu_screen(self):
        print("Job Search/Internship", end="\n\n")

        number_applied_jobs = len(self.current_user.applied_jobs)
        print(f"You have currently applied for {number_applied_jobs} jobs.", end="\n\n")
        
        deleted_job_ids = self.current_user.applied_jobs - Job.jobs.keys()
        if len(deleted_job_ids) > 0:
            print(f"{JOB_APPLIED_DELETED_BY_AUTHOR_MESSAGE}.", end="\n\n")
            
            for job_id in deleted_job_ids:
                self.current_user.remove_applied_job(job_id)
        
        print("0. List All")
        print("1. Post a Job")
        print("2. Applied Jobs")
        print("3. Not Applied Yet Jobs")
        print("4. Saved Jobs")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        if option == "0":
            return self.list_all_jobs_screen()
        elif option == "1":
            return self.post_job()
        elif option == "2":
            return self.list_applied_jobs_screen()
        elif option == "3":
            return self.list_not_applied_jobs_screen()
        elif option == "4":
            return self.list_saved_jobs_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def list_all_jobs_screen(self):
        print("All Jobs", end="\n\n")
        job_keys = list(Job.jobs.keys())
        for index, job_key in enumerate(job_keys):
            job = Job.jobs[job_key]
            print(f"{index}. {job.title}")

        print("b. Go Back")
        job_index = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if job_index == GO_BACK_KEY:
            return self.go_back()

        job_index = int(job_index)
        if job_index >= 0 and job_index < len(job_keys):
            job = Job.jobs[job_keys[job_index]]
            return self.show_job_options(job)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def list_applied_jobs_screen(self):
        print("Applied Jobs", end="\n\n")

        deleted_job_ids = self.current_user.applied_jobs - Job.jobs.keys()
        for job_id in deleted_job_ids:
            self.current_user.remove_applied_job(job_id)

        job_keys = list(self.current_user.applied_jobs)
        for index, job_key in enumerate(job_keys):
            job = Job.jobs[job_key]
            print(f"{index}. {job.title}")

        print("b. Go Back")
        job_index = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if job_index == GO_BACK_KEY:
            return self.go_back()

        job_index = int(job_index)
        if job_index >= 0 and job_index < len(job_keys):
            job = Job.jobs[job_keys[job_index]]
            return self.show_job_options(job)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def list_not_applied_jobs_screen(self):
        print("Not Applied Yet Jobs", end="\n\n")

        deleted_job_ids = self.current_user.applied_jobs - Job.jobs.keys()
        for job_id in deleted_job_ids:
            self.current_user.remove_applied_job(job_id)

        job_keys = list(Job.jobs.keys() - self.current_user.applied_jobs)
        for index, job_key in enumerate(job_keys):
            job = Job.jobs[job_key]
            print(f"{index}. {job.title}")

        print("b. Go Back")
        job_index = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if job_index == GO_BACK_KEY:
            return self.go_back()

        job_index = int(job_index)
        if job_index >= 0 and job_index < len(job_keys):
            job = Job.jobs[job_keys[job_index]]
            return self.show_job_options(job)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def list_saved_jobs_screen(self):
        print("Saved Jobs", end="\n\n")

        deleted_job_ids = self.current_user.saved_jobs - Job.jobs.keys()
        for job_id in deleted_job_ids:
            self.current_user.remove_saved_job(job_id)

        job_keys = list(self.current_user.saved_jobs)
        for index, job_key in enumerate(job_keys):
            job = Job.jobs[job_key]
            print(f"{index}. {job.title}")

        print("b. Go Back")
        job_index = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if job_index == GO_BACK_KEY:
            return self.go_back()

        job_index = int(job_index)
        if job_index >= 0 and job_index < len(job_keys):
            job = Job.jobs[job_keys[job_index]]
            return self.show_job_options(job)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def show_job_options(self, job):
        print(f"Job {job.title}", end="\n\n")

        options = [{
            "message": "Job information",
            "function": self.show_job_information
        }]

        if job.id not in self.current_user.saved_jobs:
            options.append({
                "message": "Save job",
                "function": self.save_job_screen
            })
        else:
            options.append({
                "message": "Unsave job",
                "function": self.unsave_job_screen
            })

        if self.current_user.username == job.author_username:
            options.append({
                "message": "Delete job",
                "function": self.delete_job_screen
            })
        elif job.id not in self.current_user.applied_jobs:
            options.append({
                "message": "Apply",
                "function": self.apply_job_screen
            })

        for index, option in enumerate(options):
            print(f"{index}. {option['message']}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(options):
            option = options[choice]
            return option["function"](job)

        print("Invalid choice. Try again.")

    @screen
    def show_job_information(self, job):
        print("Job Information", end="\n\n")
        print(f"Title: {job.title}")
        print(f"Description: {job.description}")
        print(f"Employer: {job.employer}")
        print(f"Location: {job.location}")
        print(f"Salary: {job.salary}")
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def post_job(self):
        print("Post a Job", end="\n\n")
        title = input(TYPE_JOB_TITLE_MESSAGE)
        description = input(TYPE_JOB_DESCRIPTION_MESSAGE)
        employer = input(TYPE_JOB_EMPLOYER_MESSAGE)
        location = input(TYPE_JOB_LOCATION_MESSAGE)
        salary = input(TYPE_JOB_SALARY_MESSAGE)

        new_job = Job(
            title,
            description,
            employer,
            location,
            salary,
        )

        error_message = new_job.save(self.current_user.username)
        if error_message == None:
            self.current_user.broadcast_new_job_notification(new_job)
            print(JOB_SAVED_MESSAGE)
        else:
            print(error_message)

        return self.go_back()

    @screen
    def save_job_screen(self, job):
        print(f"Save Job {job.title}", end="\n\n")
        error_message = self.current_user.save_job(job.id)
        if error_message:
            print(error_message)
        else:
            print(JOB_ADDED_TO_SAVED_JOBS_MESSAGE)

        return self.go_back()

    @screen
    def unsave_job_screen(self, job):
        print(f"Unsave Job {job.title}", end="\n\n")
        error_message = self.current_user.remove_saved_job(job.id)
        if error_message:
            print(error_message)
        else:
            print(JOB_REMOVED_FROM_SAVED_JOBS_MESSAGE)

        return self.go_back()

    @screen
    def delete_job_screen(self, job):
        print(f"Delete Job {job.title}", end="\n\n")
        error_message = Job.delete(job.id, self.current_user.username)
        if error_message:
            print(error_message)
        else:
            self.current_user.broadcast_job_applied_deleted_notification(job)
            print(JOB_DELETED_MESSAGE)

        self.history.pop()
        return self.go_back()

    @screen
    def apply_job_screen(self, job):
        print(f"Apply Job {job.title}", end="\n\n")

        graduation_date = input(TYPE_GRADUATION_DATE_MESSAGE)
        start_date = input(TYPE_START_DATE_MESSAGE)
        cover_letter = input(TYPE_COVER_LETTER_MESSAGE)
        apply_date = datetime.now()

        application = Job_Application(
            self.current_user.username,
            graduation_date,
            start_date,
            cover_letter,
            apply_date
        )

        error_message = job.add_application(application)
        if error_message:
            print(error_message)
        else:
            print(JOB_APPLIED_MESSAGE)
            self.current_user.save_applied_job(job.id)
        return self.go_back()

    @screen
    def guest_controls_screen(self):
        print("Guest controls", end="\n\n")
        email_toggle = "ON" if self.current_user.email_notifications else "OFF"
        sms_toggle = "ON" if self.current_user.sms_notifications else "OFF"
        targeted_ads_toggle = "ON" if self.current_user.targeted_ads else "OFF"

        print("Please select option if you would like to toggle feature ON/OFF")
        print("0. Email Notifications: ", email_toggle)
        print("1. SMS Notifications: ", sms_toggle)
        print("2. Targeted Advertisment: ", targeted_ads_toggle)
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            self.current_user.toggle_email_notifications()
        elif option == "1":
            self.current_user.toggle_sms_notifications()
        elif option == "2":
            self.current_user.toggle_targeted_ads()
        else:
            print("Invalid choice. Try again.")

        return self.reload_screen()

    @screen
    def languages_screen(self):
        print("Languages screen", end="\n\n")
        print("You are currently using", self.current_user.app_language)
        for index, language in enumerate(LANGUAGES):
            print(f"{index}: {language}")
        print("b. Go Back")
        option = self.handle_input(SELECT_LANGUAGE_MESSAGE, int)

        if option == GO_BACK_KEY:
            return self.go_back()

        language_index = int(option)
        if language_index >= 0 and language_index < len(LANGUAGES):
            self.current_user.app_language = LANGUAGES[language_index]
            User.update_users_file()
        else:
            print("Invalid choice. Try again.")

        return self.reload_screen()

    @screen
    def copyright_notice_screen(self):
        print("Copyright notice", end="\n\n")
        print(textwrap.fill(App.copyright_notice, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def about_screen(self):
        print("About", end="\n\n")
        print(textwrap.fill(App.about_message, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def accessibility_screen(self):
        print("Accessibility", end="\n\n")
        print(textwrap.fill(App.accessibility_message, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def user_agreement_screen(self):
        print("User agreenment", end="\n\n")
        print(textwrap.fill(App.user_agreement, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def privacy_policy_screen(self):
        print("Privacy policy", end="\n\n")
        print(textwrap.fill(App.privacy_policy, TEXT_WIDTH))

        if self.current_user != None:
            print("0. Guest Controls")
            print("b. Go back")
            choice = self.handle_input(SELECT_OPTION_MESSAGE)

            if choice == "0":
                return self.guest_controls_screen()

        else:
            choice = self.handle_input(GO_BACK_MESSAGE)

        return self.handle_go_back(choice)

    @screen
    def cookie_policy_screen(self):
        print("Cookie policy", end="\n\n")
        print(textwrap.fill(App.cookie_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def copyright_policy_screen(self):
        print("Copyright policy", end="\n\n")
        print(textwrap.fill(App.copyright_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def brand_policy_screen(self):
        print("Brand policy", end="\n\n")
        print(textwrap.fill(App.brand_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def important_links_screen(self):
        print("Important links", end="\n\n")
        print("0. Copyright Notice")
        print("1. About")
        print("2. Accessibility")
        print("3. User Agreement")
        print("4. Privacy Policy")
        print("5. Cookie Policy")
        print("6. Copyright Policy")
        print("7. Brand Policy")
        if self.current_user != None:
            print("8. Language")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.copyright_notice_screen()
        elif option == "1":
            return self.about_screen()
        elif option == "2":
            return self.accessibility_screen()
        elif option == "3":
            return self.user_agreement_screen()
        elif option == "4":
            return self.privacy_policy_screen()
        elif option == "5":
            return self.cookie_policy_screen()
        elif option == "6":
            return self.copyright_policy_screen()
        elif option == "7":
            return self.brand_policy_screen()
        elif option == "8" and self.current_user != None:
            return self.languages_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def useful_links_screen(self):
        print("Useful links", end="\n\n")
        print("0. General")
        print("1. Browse InCollege")
        print("2. Business Solutions")
        print("3. Directories")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.general_option_screen()
        elif option == "1":
            return self.under_construction_screen()
        elif option == "2":
            return self.under_construction_screen()
        elif option == "3":
            return self.under_construction_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def general_option_screen(self):
        print("General option", end="\n\n")
        print("0. Sign Up")
        print("1. Help Center")
        print("2. About")
        print("3. Press")
        print("4. Blog")
        print("5. Careers")
        print("6. Developers")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.register_user_screen()
        elif option == "1":
            return self.help_center_screen()
        elif option == "2":
            return self.general_option_about_screen()
        elif option == "3":
            return self.press_screen()
        elif option == "4":
            return self.under_construction_screen()
        elif option == "5":
            return self.under_construction_screen()
        elif option == "6":
            return self.under_construction_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def help_center_screen(self):
        print("Help center", end="\n\n")
        print(HELP_CENTER_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def general_option_about_screen(self):
        print("About", end="\n\n")
        print(GENERAL_OPTION_ABOUT_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def press_screen(self):
        print("Press", end="\n\n")
        print(PRESS_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def main_menu(self):
        print(textwrap.fill(App.success_story, TEXT_WIDTH))
        print("\nWelcome to InCollege!", end="\n\n")
        print("0. Login")
        print("1. Create account")
        print("2. Video: Why InCollege is the best option for you")
        print("3. Connect with Someone You Know")
        print("4. Useful Links")
        print("5. InCollege Important Links")
        print("b. Exit")
        choice = self.handle_input(SELECT_OPTION_MESSAGE)

        if choice == GO_BACK_KEY:
            return self.go_back()
        elif choice == "0":
            return self.login_screen()
        elif choice == "1":
            return self.register_user_screen()
        elif choice == "2":
            return self.play_video()
        elif choice == "3":
            return self.find_someone_screen()
        elif choice == "4":
            return self.useful_links_screen()
        elif choice == "5":
            return self.important_links_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def search_students_screen(self):
        print("Search students", end="\n\n")
        print("0. Search by last name")
        print("1. Search by university")
        print("2. Search by major")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE)

        if choice == GO_BACK_KEY:
            return self.go_back()
        elif choice == "0":
            return self.search_students_by_last_name_screen()
        elif choice == "1":
            return self.search_students_by_university_screen()
        elif choice == "2":
            return self.search_students_by_major_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def search_students_by_last_name_screen(self):
        print("Search students by last name", end="\n\n")
        last_name = input(TYPE_LAST_NAME_MESSAGE)
        users_list = User.find_users_by_last_name(last_name)

        # Removes this screen from the history
        self.history.pop()
        return self.search_students_result_screen(users_list)

    @screen
    def search_students_by_university_screen(self):
        print("Search students by university", end="\n\n")
        university = input(TYPE_NAME_OF_UNIVERSITY)
        users_list = User.find_users_by_university(university)

        # Removes this screen from the history
        self.history.pop()
        return self.search_students_result_screen(users_list)

    @screen
    def search_students_by_major_screen(self):
        print("Search students by major", end="\n\n")
        major = input(TYPE_MAJOR_MESSAGE)
        users_list = User.find_users_by_major(major)

        # Removes this screen from the history
        self.history.pop()
        return self.search_students_result_screen(users_list)

    @screen
    def search_students_result_screen(self, users_list):
        print("Search students results", end="\n\n")
        for index, user in enumerate(users_list):
            print(f"{index}. {user.first_name} {user.last_name}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(users_list):
            return self.show_student_options(users_list[choice])

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def show_student_options(self, user):
        print(f"Student {user.first_name} {user.last_name}", end="\n\n")

        is_self = self.current_user == user
        is_friend = user.username in self.current_user.friends
        is_plus = user.tier == PLUS_TIER_NAME
        sent_request = user.username in self.current_user.sent_friend_requests
        received_request = user.username in self.current_user.received_friend_requests

        options = []
        if received_request:
            options.append({
                "message": "Accept connection",
                "function": self.accept_connection_screen,
            })
            options.append({
                "message": "Reject connection",
                "function": self.reject_connection_screen,
            })

        if (is_friend or is_self) and user.profile:
            options.append({
                "message": "Show profile",
                "function": self.show_profile_screen,
            })

        if is_friend:
            options.append({
                "message": "Disconnect",
                "function": self.disconnect_screen,
            })

        if not is_self:
            options.append({
                "message": "Send message",
                "function": self.send_message_input_screen,
            })

        if not is_self and not is_friend and not sent_request and not received_request:
            options.append({
                "message": "Request connection",
                "function": self.request_connection_screen,
            })

        for index, option in enumerate(options):
            print(f"{index}. {option['message']}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(options):
            option = options[choice]
            return option["function"](user)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def request_connection_screen(self, user):
        print(f"Request connection with {user.first_name}", end="\n\n")
        error_message = self.current_user.request_connection(user)
        if error_message:
            print(error_message)
        else:
            print(CONNECTION_REQUESTED_MESSAGE)

        return self.go_back()

    @screen
    def accept_connection_screen(self, user):
        print(f"Accept connection with {user.first_name}", end="\n\n")
        error_message = self.current_user.accept_connection(user)
        if error_message:
            print(error_message)
        else:
            print(CONNECTION_ACEPTED_MESSAGE)

        return self.go_back()

    @screen
    def reject_connection_screen(self, user):
        print(f"Reject connection with {user.first_name}", end="\n\n")
        error_message = self.current_user.reject_connection(user)
        if error_message:
            print(error_message)
        else:
            print(CONNECTION_REJECTED_MESSAGE)

        return self.go_back()

    @screen
    def disconnect_screen(self, user):
        print(f"Disconnect from {user.first_name}", end="\n\n")
        error_message = self.current_user.disconnect(user)
        if error_message:
            print(error_message)
        else:
            print(DISCONNECTED_MESSAGE)

        return self.go_back()

    @screen
    def my_network_screen(self):
        users_list = self.current_user.friends

        print("My network", end="\n\n")
        for index, username in enumerate(users_list):
            user = User.users[username]
            print(f"{index}. {user.first_name} {user.last_name}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(users_list):
            user = User.users[users_list[choice]]
            return self.show_student_options(user)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def pending_friend_requests_screen(self):
        users_list = self.current_user.received_friend_requests

        print("Pending friend requests", end="\n\n")
        for index, username in enumerate(users_list):
            user = User.users[username]
            print(f"{index}. {user.first_name} {user.last_name}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(users_list):
            user = User.users[users_list[choice]]
            return self.show_student_options(user)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def read_message_screen(self, message):
        print(f"Message", end="\n\n")

        user = User.users[message.sender_username]
        print(f"From: {user.first_name} {user.last_name}")
        print(textwrap.shorten(message.content, width=TEXT_WIDTH))
        self.current_user.mark_message_on_inbox_as_read(message.id)
        choice = self.handle_input(GO_BACK_MESSAGE)

        if choice == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def send_message_input_screen(self, user, message=None):
        if message is None:
            print(f"Send Message to {user.first_name} {user.last_name}", end="\n\n")
        else:
            print("Reply", end="\n\n")
            print(f"From: {user.first_name} {user.last_name}")
            print(f"Preview: {textwrap.shorten(message.content, width=MESSAGE_PREVIEW_WIDTH)}", end="\n\n")

        is_friend = user.username in self.current_user.friends
        is_plus = self.current_user.tier == PLUS_TIER_NAME
        if message is None and not is_friend and not is_plus:
            print(ONLY_CAN_MESSAGE_YOUR_FRIENDS_ERROR_MESSAGE)
            return self.go_back()

        content = input(TYPE_MESSAGE_CONTENT)

        error_message = self.current_user.send_message(user, content)
        if error_message is not None:
            print(error_message)
        else:
            print(MESSAGE_SENT_MESSAGE)

        return self.go_back()

    @screen
    def delete_message_from_inbox_screen(self, message):
        print(f"Delete Message", end="\n\n")

        user = User.users[message.sender_username]
        print(f"From: {user.first_name} {user.last_name}")
        print(f"Preview: {textwrap.shorten(message.content, width=MESSAGE_PREVIEW_WIDTH)}", end="\n\n")

        error_message = self.current_user.delete_message_from_inbox(message.id)
        if error_message is not None:
            print(error_message)
        else:
            print(MESSAGE_DELETED_MESSAGE)

        self.history.pop()
        return self.go_back()

    @screen
    def show_message_options(self, message):
        print(f"Message", end="\n\n")

        user = User.users[message.sender_username]
        print(f"From: {user.first_name} {user.last_name}")
        print(f"Preview: {textwrap.shorten(message.content, width=MESSAGE_PREVIEW_WIDTH)}", end="\n\n")

        print("0. Read")
        print("1. Reply")
        print("2. Delete")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE)

        if choice == GO_BACK_KEY:
            return self.go_back()
        elif choice == "0":
            return self.read_message_screen(message)
        elif choice == "1":
            return self.send_message_input_screen(user, message)
        elif choice == "2":
            return self.delete_message_from_inbox_screen(message)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def inbox_screen(self):
        messages_id = list(self.current_user.inbox.keys())

        print("Inbox", end="\n\n")
        for index, message_id in enumerate(messages_id):
            message = self.current_user.inbox[message_id]
            user = User.users[message.sender_username]

            print(f"{index}. {user.first_name} {user.last_name} - ", end="")
            print(textwrap.shorten(message.content, width=MESSAGE_PREVIEW_WIDTH), end="")
            if message.status == UNREAD_STATUS:
                print(f" ({message.status})")
            else:
                print("")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(messages_id):
            message = self.current_user.inbox[messages_id[choice]]
            return self.show_message_options(message)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def send_message_screen(self):
        if self.current_user.tier == PLUS_TIER_NAME:
            users_list = set(User.users.keys())
            users_list.remove(self.current_user.username)
            users_list = list(users_list)
        else:
            users_list = self.current_user.friends

        print("Send message", end="\n\n")
        for index, username in enumerate(users_list):
            user = User.users[username]
            print(f"{index}. {user.first_name} {user.last_name}")
        print("b. Go back")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()

        choice = int(choice)
        if choice >= 0 and choice < len(users_list):
            user = User.users[users_list[choice]]
            return self.send_message_input_screen(user)

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def user_dashboard(self):
        print("Welcome to InCollege!", end="\n\n")

        if self.current_user.profile is None:
            print(DO_NOT_FORGET_PROFILE_MESSAGE, end="\n\n")

        last_application_date = datetime.now() - timedelta(days=8)
        for job_id in self.current_user.applied_jobs:
            job = Job.jobs[job_id]
            application = job.applications[self.username]
            if not last_application_date or application.apply_date > last_application_date:
                last_application_date = application.apply_date
        
        elapsed_time = datetime.now() - last_application_date
        if elapsed_time >= timedelta(days=7):
            print(LAST_APPLICATION_SEVEN_DAYS_AGO_MESSAGE, end="\n\n")

        if len(self.current_user.received_friend_requests) > 0:
            print(PENDING_FRIEND_REQUEST_MESSAGE, end="\n\n")

        inbox = self.current_user.inbox
        if any([inbox[message_key].status == UNREAD_STATUS for message_key in inbox]):
            print(UNREAD_MESSAGES_MESSAGE, end="\n\n")

        while len(self.current_user.notifications) > 0:
            notification = self.current_user.pop_notification()
            print(notification, end="\n\n")

        print("0. Job Search/Internship")
        print("1. Search students")
        print("2. Learn a New Skill")
        print("3. Useful Links")
        print("4. InCollege Important Links")
        print("5. Edit Profile")
        print("6. View Profile")
        print("7. Show my network")
        print("8. Pending friend requests")
        print("9. Inbox")
        print("10. Send message")
        print("b. Sign Out")
        choice = self.handle_input(SELECT_OPTION_MESSAGE)

        if choice == GO_BACK_KEY:
            self.current_user = None
            return self.go_back()
        elif choice == "0":
            return self.job_menu_screen()
        elif choice == "1":
            return self.search_students_screen()
        elif choice == "2":
            return self.new_skills_screen()
        elif choice == "3":
            return self.useful_links_screen()
        elif choice == "4":
            return self.important_links_screen()
        elif choice == "5":
            return self.edit_profile_screen()
        elif choice == "6":
            return self.show_profile_screen(self.current_user)
        elif choice == "7":
            return self.my_network_screen()
        elif choice == "8":
            return self.pending_friend_requests_screen()
        elif choice == "9":
            return self.inbox_screen()
        elif choice == "10":
            return self.send_message_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()


if __name__ == "__main__":
    # Loads the registered users to memory
    User.load_users_file()
    # Loads the saved jobs to memory
    Job.load_jobs_file()
    # Loads the saved next_job_id to memory
    Job.load_next_job_id_file()
    # Loads the saved next_message_id to memory
    Message.load_next_message_id_file()
    # Loads the success story
    App.load_success_story()
    # Loads the copyright notice
    App.load_copyright_notice()
    # Loads the about message
    App.load_about_message()
    # Loads the accessibility message
    App.load_accessibility_message()
    # Loads the user agreement
    App.load_user_agreement()
    # Loads the privacy policy
    App.load_privacy_policy()
    # Loads the cookie policy
    App.load_cookie_policy()
    # Loads the copyright policy
    App.load_copyright_policy()
    # Loads the brand policy
    App.load_brand_policy()
    # Starts the app
    app = App()
    app.main_menu()
