from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    """Test that users can visit the website and make to-do items."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Jenn wants to be more organized, so she decides to try a hot
        # new to-do app. She starts by visiting the homepage:
        self.browser.get("http://localhost:8000")

        # The page title and header mention to-do lists.

        self.assertIn('To-Do', self.browser.title)

        # Jenn is invited to enter a to-do item straight away. Very hospitable.

        # Jenn likes to build blinky crafts, so she types "Buy EL wire and battery
        # pack" into a text box.

        # When Jenn hits enter, the page updates, and now the page lists--
        # "1: Buy EL wire and battery pack" as an item in a to-do list.

        # There is still a text box invited Jenn to add another to-do item. She
        # adds "Sew EL wire onto hat" to the list.

        # The page updates again, and now it shows both items on Jenn's list.

        # Jenn wonders whether the site will remember her list. Then she sees that
        # the site has generated a unique URL for her -- there is some explanatory text
        # to that effect.

        # Jenn visits that URL, and her to-do list is still there. Sweet!

        # Satisfied, she goes back to coding.


if __name__ == "__main__":
    unittest.main()
