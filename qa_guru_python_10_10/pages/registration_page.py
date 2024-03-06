from selene import browser, be, have, command
from qa_guru_python_10_10 import resource
import allure
from qa_guru_python_10_10.data.users import User, date


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.phone_number = browser.element('#userNumber')
        self.subjects_input = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.submit = browser.element("#submit")
        self.current_address = browser.element("#currentAddress")
        self.submit_button = browser.element('#submit')

    @allure.step('Open practice-form')
    def open(self):
        browser.open("automation-practice-form")

    @allure.step('Accept consent')
    def accept_consent(self):
        browser.element('.fc-cta-consent').click()

    @allure.step('Fill first name')
    def fill_first_name(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)

    @allure.step('Fill last name')
    def fill_last_name(self, user: User):
        self.last_name.should(be.blank).type(user.last_name)

    @allure.step('Fill email')
    def fill_user_email(self, user: User):
        self.email.should(be.blank).type(user.email)

    @allure.step('Choose gender')
    def choose_gender(self, user: User):
        self.gender.element_by(have.exact_text(user.gender)).click()

    @allure.step('Fill phone number')
    def fill_phone_number(self, user: User):
        self.phone_number.should(be.blank).type(user.phone_number)

    @allure.step('Fill date of birth')
    def fill_date_of_birth(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{user.birth_year}"]').perform(
            command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element(
            f'[value="{user.birth_month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

    @allure.step('Fill subjects')
    def fill_subjects(self, user: User):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        self.subjects_input.should(be.blank).type(user.subjects[0]).press_enter()
        if len(user.subjects) >= 2:
            for sub in user.subjects[1:]:
                self.subjects_input.type(sub)
                browser.element('#react-select-2-option-0').click()

    @allure.step('Choose hobbies')
    def choose_hobbies(self, user: User):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        for hobby in user.hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(
                have.exact_text(hobby)).click()

    @allure.step('Upload picture')
    def upload_picture(self, user: User):
        self.picture.send_keys(resource.path(user.picture))

    @allure.step('Fill current address')
    def fill_current_address(self, user: User):
        self.current_address.should(be.blank).type(user.current_address)

    @allure.step('Fill state')
    def fill_state(self, user: User):
        browser.element('#state').click()
        browser.all("[id^='react-select-3-option']").element_by(
            have.exact_text(user.state)).click()

    @allure.step('Fill city')
    def fill_city(self, user: User):
        browser.element('#city').click()
        browser.all("[id^='react-select-4-option']").element_by(
            have.exact_text(user.city)).click()

    @allure.step('Submit')
    def click_submit_button(self):
        self.submit_button.perform(command.js.click)

    @allure.step('{user} registration')
    def user_registration(self, user: User):
        self.fill_first_name(user)
        self.fill_last_name(user)
        self.fill_user_email(user)
        self.choose_gender(user)
        self.fill_phone_number(user)
        self.fill_date_of_birth(user)
        self.fill_subjects(user)
        self.choose_hobbies(user)
        self.upload_picture(user)
        self.fill_current_address(user)
        self.fill_state(user)
        self.fill_city(user)
        self.click_submit_button()

    @allure.step('Check data correctness after registration')
    def should_registered_user_with(self, user: User):
        browser.element('.modal-dialog').should(be.existing)
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone_number,
                f"{user.birth_day} {date.strftime('%B')},{user.birth_year}",
                ', '.join(user.subjects),
                ', '.join(user.hobbies),
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            ))
