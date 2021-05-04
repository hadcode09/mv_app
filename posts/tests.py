from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test")

    def test-text_content(self):
        post = Post.objects,get(id=1)
        expected_obj_name =f"{post.text}"
        self.assertEqual(expected_obj_name, "Just a test")
