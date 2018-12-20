from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    catid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cname


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    vcnt= models.IntegerField(default=1)
    lcnt= models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='product_media', blank=True, null=True)

    def __str__(self):
        #return str(self.pid) + ' -- ' + self.pname +' -- ' + str(self.price) + ' -- ' + str(self.catid) + ' -- ' + str(self.available)
        return self.pname
