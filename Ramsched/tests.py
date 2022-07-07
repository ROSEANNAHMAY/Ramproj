from django.test import TestCase
from Ramsched.views import MainPage
from .models import ClientInformations


class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'new_mainpage.html')

    def test_save_POST_request(self):
        response = self.client.post('/', {'Client': 'Karl',
            'clientNo':'09184496418',
            'SessTime':'3:00pm',})

        self.assertEqual(ClientInformations.objects.count(),1)
        RamData = ClientInformations.objects.first()
        self.assertEqual(RamData.newClientName, 'Karl')
        self.assertEqual(RamData.newClientphoneNo, '09184496418')
        self.assertEqual(RamData.newtimeSession, '3:00pm')

    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(ClientInformations.objects.count(), 0)


class ORMTEST(TestCase):
    def test_saving_retrive(self):
        copy_of_ClientInformations = ClientInformations()
        copy_of_ClientInformations.newClientName = 'Karl'
        copy_of_ClientInformations.newClientphoneNo = '09184496418'
        copy_of_ClientInformations.newtimeSession = '3:00pm'

        copy_of_ClientInformations.save()

        copy_of_ClientInformations2 = ClientInformations()
        copy_of_ClientInformations2.newClientName = 'Kath'
        copy_of_ClientInformations2.newClientphoneNo = '09184496422'
        copy_of_ClientInformations2.newtimeSession = '6:00pm'
        copy_of_ClientInformations2.save()


        lists_of_ClientInfo = ClientInformations.objects.all()

        self.assertEqual(lists_of_ClientInfo.count(), 2)

        client1 = lists_of_ClientInfo[0]
        client2 = lists_of_ClientInfo[1]

        self.assertEqual(client1.newClientName, 'Karl')
        self.assertEqual(client1.newClientphoneNo, '09184496418')
        self.assertEqual(client1.newtimeSession, '3:00pm')

        self.assertEqual(client2.newClientName, 'Kath')
        self.assertEqual(client2.newClientphoneNo, '09184496422')
        self.assertEqual(client2.newtimeSession, '6:00pm')
        

    def test_template_display_list(self):
        ClientInformations.objects.create(newClientName='Symon',
            newClientphoneNo='0917777',
            newtimeSession='8:00pm',)

        ClientInformations.objects.create(newClientName='Johna',
            newClientphoneNo='098888',
            newtimeSession='1:00pm',)

        response = self.client.get('/')
        self.assertIn('Symon, 0917777, 8:00pm', response.content.decode())
        self.assertIn('Johna, 098888, 1:00pm', response.content.decode())
        
    # def test_responding_POST_request(self):
    #     resp = self.client.post('/', data={'customerName': 'newcustomerName',
    #         'customerNumber': 'newcustomerNumber', 'timeDelivery': 'newtimeDelivery'})
    #     self.assertIn('customerName', resp.content.decode())
    #     self.assertTemplateUsed(resp,'mainpage.html')