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

        self.assertEqual(services[0], {
            'category': 'Animaux de compagnie',
            'services': [{
                'title': 'Chirurgie - anesth\u00e9sie',
            }, {
                'title': 'Ophtalmologie',
            }, {
                'title': 'Pharmacie',
            }],
        })
