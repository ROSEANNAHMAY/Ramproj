import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()
      
   def test_start_list_and_retrieve_it(self):
      self.browser.get(self.live_server_url)
      self.assertIn('Ramsched', self.browser.title)
      headerName = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Book Now!', headerName)

      name = self.browser.find_element_by_id('ClientName')
      name.send_keys('Tacorda')
      time.sleep(0.5)
      self.assertEqual(name.get_attribute('placeholder'),'Enter your name here.')


      phoneNo = self.browser.find_element_by_id('ClientNumber')
      phoneNo.send_keys('09085969285')
      time.sleep(0.5)
      self.assertEqual(phoneNo.get_attribute('placeholder'),'Enter your number here.')

      customersTimeofSession = self.browser.find_element_by_id('SessTime')
      customersTimeofSession.send_keys('3:00pm')
      time.sleep(0.5)


      btnram_button = self.browser.find_element_by_id('rambtn')
      btnram_button.click()
      time.sleep(0.5)



      self.browser.get(self.live_server_url)
      self.assertIn('Ramsched', self.browser.title)
      headerName = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Book Now!', headerName)

      name = self.browser.find_element_by_id('ClientName')
      name.send_keys('Dela Cruz')
      time.sleep(0.5)
      self.assertEqual(name.get_attribute('placeholder'),'Enter your name here.')


      phoneNo = self.browser.find_element_by_id('ClientNumber')
      phoneNo.send_keys('09186498814')
      time.sleep(0.5)
      self.assertEqual(phoneNo.get_attribute('placeholder'),'Enter your number here.')

      customersTimeofSession = self.browser.find_element_by_id('SessTime')
      customersTimeofSession.send_keys('2:00pm')
      time.sleep(0.5)


      btnram_button = self.browser.find_element_by_id('rambtn')
      btnram_button.click()
      time.sleep(0.5)
 

   def checks_the_table(self,row_test):
      table = self.browser.find_element_by_id('table')
      row_data = table.find_element_by_tag_name('tr')
      self.assertIn('1: Tacorda', [row.text for row in rows])
      # self.assertIn('1: Dela Cruz', [row.text for row in rows])


# if __name__ == '__main__':
#    unittest.main(warnings='ignore')
