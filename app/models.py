from bridger.search import register as search_register
from django.db import models

# Create your models here.

@search_register(endpoint="student-list")
class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    student_details = models.TextField()
    age = models.CharField(max_length=100, blank=True, null=True)
    religion = models.ForeignKey("Religion", on_delete=models.CASCADE, null=True, blank=True)
    
    @classmethod
    def get_endpoint_basename(cls):
        return "student"

    @classmethod
    def get_endpoint(cls):
        return "student-list"

    def get_tag_detail_endpoint(self):
        return reverse("student-detail", args=[self.id])
    

class Religion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_endpoint_basename(cls):
        return "religion"

    @classmethod
    def get_endpoint(cls):
        return "religion-list"

    def get_tag_detail_endpoint(self):
        return reverse("religion-detail", args=[self.id])

    def get_tag_representation(self):
        return self.name

    @property
    def upper_char_field(self):
        return self.name.upper()

    @classmethod
    def get_representation_endpoint(cls):
        return "religion-list"

    @classmethod
    def get_representation_value_key(cls):
        return "id"

    @classmethod
    def get_representation_label_key(cls):
        return "{{name}}"

