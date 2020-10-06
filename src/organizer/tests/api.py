"""
    Tests for organizer
    Covering:
        Tags

"""
from test_plus.test import TestCase


class OrganizerAPITests(TestCase):
    """ Testing Organizer API """

    def test_status_get(self):
        """ Testing status page """
        response = self.get_check_200("site_status")
        templates = [
            "base.html",
            "organizer/base.html",
            "organizer/status.html",
        ]
        for t in templates:
            with self.subTest(template=t):
                self.assertTemplateUsed(response, t)
        self.assertInContext("status")
        self.assertContext("status", "Good")
        self.assertResponseContains(
            "Connection: Good", html=False
        )

    def test_ping_get(self):
        """ Testing GET """
        response = self.client.get("/api/v1/tag/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content.decode("utf8"),
            "[]"
        )

    def test_ping_head(self):
        """ Testing HEAD """
        response = self.client.head("/api/v1/tag/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")
        self.assertGreater(
            int(response["Content-Length"]),
            0
        )

    def test_ping_options(self):
        """ Testing OPTIONS """
        response = self.client.options("/api/v1/tag/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(int(response["Content-Length"]), 0)

        for method in ["GET", "HEAD", "OPTIONS"]:
            with self.subTest(method=method):
                self.assertIn(
                    method,
                    response["Allow"],
                    f"{method} not in ALLOW header",
                )

    def test_ping_not_allowed_methods(self):
        """ Testing not allowed methods """
        not_allowed = [
            "delete",
            "patch",
            "post",
            "put",
            "trace",
        ]
        for method in not_allowed:
            with self.subTest(method=method):
                call_method = getattr(self.client, method)
                response = call_method("/api/v1/tag/")
                self.assertTrue(
                    400 <= response.status_code <= 405,
                    f"{method} should not be allowed"
                )

