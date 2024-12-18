
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpTestCase(TestCase):
    def test_user_signup(self):
        # Envoie une requête POST avec des données valides
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'testuser@example.com',
        })

        # Vérifie que l'utilisateur a été créé
        self.assertEqual(User.objects.count(), 1)  # Vérifie qu'il y a 1 utilisateur dans la DB
        self.assertEqual(User.objects.first().username, 'testuser')  # Vérifie que c'est le bon utilisateur
        self.assertRedirects(response, reverse('login'))  # Vérifie qu'on est redirigé vers la page de login
