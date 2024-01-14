from django.db import models

# {
#      'id' : 1,
#      'client_name' : 'Nimap',
#      'created_at' : '2019-12-24T11:03:55.931739+05:30',
#      'created_by' : 'Rohit'
# },


class Clients(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True, unique=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name
