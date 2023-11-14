from tortoise import models, fields


class Article(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
