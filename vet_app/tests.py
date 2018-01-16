from django.test import TestCase

from .models import People


class PeopleModeTest(TestCase):
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
