from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name    

class Table(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.name    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL,null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_complete = models.BooleanField(default=False)
    serve_complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total 

# class Board(models.Model):
#     """
#         title: 제목
#         content: 내용
#         author: 작성자
#         like_count: 좋아요 카운트
#         pub_date: 배포일
#     """
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=500)
#     author = models.CharField(max_length=100)
#     like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
#     pub_date = models.DateTimeField()

#     def __str__(self):
#         return self.title

# class Reply(models.Model):
#     """
#         reply: Reply -> Board 연결관계
#         comment: 댓글내용
#         rep_date: 작성일
#     """
#     reply = models.ForeignKey(Board, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=200)
#     rep_date = models.DateTimeField()

#     def __str__(self):
#         return self.comment

