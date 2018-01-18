from django.test import TestCase

from .models import People
from .models import Service


class PeopleModelTest(TestCase):
    fixtures = ['people']

    def test_people_get_in_right_order(self):
        names = [
            (person.name, person.role)
            for person in People.objects.get_ordered_people()
        ]

        self.assertEqual(names, [
            ('Albion perfide', 'Docteur Vétérinaire Associé(e)'),
            ('Riton la foudre', 'Docteur Vétérinaire Associé(e)'),
            ('El castor', 'Docteur Vétérinaire'),
            ('Yop la', 'ASV'),
            ('Miss Penny', 'Secrétaire comptable'),
        ])


class ServiceModelTest(TestCase):
    fixtures = ['service']

    def test_get_services_return_three_list_of_services(self):
        services = Service.objects.get_services()

        self.assertEqual(len(services), 3)

    def test_get_services_return_services_for_puppet(self):
        services = Service.objects.get_services()
        self.assertEqual(services[0]['category'], 'Animaux de compagnie')
        self.assertEqual([service.title for service in services[0]['services']], [
            'Alimentation',
            'Analyses médicales',
            'Chirurgie - anesthésie',
            'Consultation des NAC',
            'Consultation vaccinale',
            'Dermatologie',
            'Echographie',
            'Hospitalisation',
            'Médecine interne',
            'Ophtalmologie',
            'Pharmacie',
            'Radiographie',
        ])

    def test_get_services_return_services_for_rural(self):
        services = Service.objects.get_services()

        self.assertEqual(services[1]['category'], 'Rurale')
        self.assertEqual([service.title for service in services[1]['services']], [
            'Alimentation bovine',
            'Boiteries / Parage',
            'Chirurgie',
            'Elevage des veaux',
            'Laboratoire',
            'La qualité du lait',
            'Location de matériel',
            'Nos Services Elevage',
            'Ramassage des Fûts Eleveurs 2017',
            'Suivi de reproduction sur mesure',
        ])

    def test_get_services_return_services_for_equine(self):
        services = Service.objects.get_services()

        self.assertEqual(services[2]['category'], 'Equine')
        self.assertEqual([service.title for service in services[2]['services']], [
            'Chirurgies',
            'La saison de reproduction',
            'Le pack vermifugation équides',
            'Location de mat\u00e9riel: N\u00e9bulisateur pour probl\u00e8mes respiratoires',
        ])
