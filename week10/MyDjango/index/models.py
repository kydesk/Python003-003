# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 第 06 周作业创建的表
class Douban(models.Model):
    short = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comment_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban'

# 第 10 周作业创建，用于创建后台管理的表
class Post(models.Model):
    Username = models.CharField(max_length=20, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    short = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comment_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'