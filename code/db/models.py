from tortoise import models, fields

from db import custom_fields


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True)

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseModel(IdMixin, TimestampMixin):
    class Meta:
        abstract = True


class Tag(BaseModel):
    name = fields.CharField(max_length=100)
    articles = fields.ManyToManyField('models.Article', related_name='tags')


class Article(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    description = fields.TextField()
    author_id = fields.IntField()
    avatar = custom_fields.FileField(upload_to='media/avatars', null=True)
    
    class Meta:
        table = 'article'
