from django.db import models

class Request(models.Model):
      #request_id = models.IntegerField(primary_key=True, default=100)
      content = models.CharField(max_length=50)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      type = models.CharField(max_length=100)

      class Meta:
          db_table = 'Request'

      def __str__(self):
        return self.type    