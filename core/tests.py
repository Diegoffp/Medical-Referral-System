from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class ReferralAPITests(TestCase):

    def test_unauthenticated_user_cannot_access_referrals(self):
        response = self.client.get(reverse("referral_api"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_staff_user_can_access_referrals(self):
        User = get_user_model()

        staff_user = User.objects.create_user(
            username="test_staff",
            password="test_password_123",
            is_staff=True
        )

        self.client.force_login(staff_user)

        response = self.client.get(reverse("referral_api"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"referrals": []})

    def test_non_staff_user_cannot_access_referrals(self):
        User = get_user_model()

        regular_user = User.objects.create_user(
            username="test_regular",
            password="test_password_123",
            is_staff=False
        )

        self.client.force_login(regular_user)

        response = self.client.get(reverse("referral_api"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)