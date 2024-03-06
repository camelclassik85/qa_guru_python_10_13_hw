from qa_guru_python_10_10.data import users
from qa_guru_python_10_10.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag('qa_guru_python_10_10_hw')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'AD')
@allure.feature('Student Registration Form')
@allure.story('Filling registration form')
def test_fill_registration_form():
    ad = users.ad
    registration_page = RegistrationPage()

    # open registration form
    registration_page.open()

    # accept consent
    registration_page.accept_consent()

    # WHEN
    registration_page.user_registration(ad)

    # THEN
    registration_page.should_registered_user_with(ad)
