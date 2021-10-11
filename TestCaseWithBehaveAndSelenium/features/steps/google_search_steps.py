from behave import given, when, then
from features.page_objects.google_homepage import GoogleSearch


@given('Google homepage is open')
def google_homepage_is_open(context):
    context.homepage = GoogleSearch()
    context.homepage.confirm_cookies()
    context.homepage.select_language()


@when('Search word proba is entered')
def search_word_dupa_is_entered(context):
    context.homepage.input_search_text('proba')


@when('Button search is clicked')
def button_search_is_clicked(context):
    context.homepage.click_search_button()


@then('Webpage with results is visible')
def webpage_with_results_is_visible(context):
    context.homepage.clean_up()


@then('The following results are shown')
def the_following_results_are_shown(context):
    pass
