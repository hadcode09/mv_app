from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_obj_name =f"{post.text}"
        self.assertEqual(expected_obj_name, "Just a test")

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objets.create(text="This is another test")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status.cde, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_ueses_crrect_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp, "home.html")