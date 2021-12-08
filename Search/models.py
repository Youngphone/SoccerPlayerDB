# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib import admin


class Country(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='名称')
    name_cn = models.CharField(max_length=10, null=True, verbose_name='中文名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'
        verbose_name = '国家'
        verbose_name_plural = verbose_name


class League(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='联赛名称')
    name_cn = models.CharField(max_length=50, null=True, verbose_name='联赛中文名称')
    countryid = models.ForeignKey(Country, on_delete=models.SET_NULL, db_column='countryid', blank=True, null=True,
                                  verbose_name='所属国家')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'league'
        verbose_name = '联赛'
        verbose_name_plural = verbose_name


class Players(models.Model):
    firstname = models.CharField(max_length=20, null=True, verbose_name='名')
    familyname = models.CharField(max_length=20, null=True, verbose_name='姓')
    shortname = models.CharField(max_length=20, null=True, verbose_name='简称')
    firstname_cn = models.CharField(max_length=20, null=True, verbose_name='中文名')
    familyname_cn = models.CharField(max_length=20, null=True, verbose_name='中文姓')
    shortname_cn = models.CharField(max_length=10, null=True, verbose_name='中文简称')
    originname = models.CharField(max_length=40, null=True, verbose_name='全名')
    yearofbirth = models.IntegerField(null=True, verbose_name='出生年份')
    countryid = models.ForeignKey(Country, on_delete=models.SET_NULL, db_column='countryid', null=True,
                                  verbose_name='国籍')

    @admin.display(ordering=Concat('firstname', Value(' '), 'familyname'), description='全称')
    def full_name(self):
        return self.firstname + ' ' + self.familyname

    @admin.display(ordering=Concat('firstname_cn', Value(' '), 'familyname_cn'), description='中文全称')
    def full_name_cn(self):
        return self.firstname_cn + ' ' + self.familyname_cn

    def __str__(self):
        return self.firstname + ' ' + self.familyname

    class Meta:
        db_table = 'players'
        verbose_name = '球员'
        verbose_name_plural = verbose_name


class Team(models.Model):
    fullname_en = models.CharField(max_length=50, null=True, verbose_name='全称')
    shortname_en = models.CharField(max_length=10, null=True, verbose_name='简称')
    fullname_cn = models.CharField(max_length=30, null=True, verbose_name='中文全称')
    shortname_cn = models.CharField(max_length=10, null=True, verbose_name='中文简称')
    countryid = models.ForeignKey(Country, on_delete=models.SET_NULL, db_column='countryid', null=True,
                                  verbose_name='所属国家')

    def __str__(self):
        return self.fullname_en

    class Type(models.IntegerChoices):
        club = 0        # 俱乐部
        national = 1    # 国家队

    type = models.IntegerField(choices=Type.choices, default=Type.club, verbose_name='球队类型')

    class Meta:
        db_table = 'team'
        verbose_name = '球队'
        verbose_name_plural = verbose_name


class Playertoteam(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE, verbose_name='球员全称')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='球队全称')
    num = models.IntegerField(null=True, verbose_name='球衣号码')
    pos = models.CharField(max_length=5, blank=True, null=True, verbose_name='球员位置')
    time_join = models.DateField(blank=True, null=True, verbose_name='加入球队时间')
    time_leave = models.DateField(blank=True, null=True, verbose_name='离开球队时间')

    class Type(models.IntegerChoices):
        local = 0   # 本队球员
        born = 1    # 租借球员

    type = models.IntegerField(choices=Type.choices, default=Type.local, verbose_name='球员类型')

    class Meta:
        db_table = 'playertoteam'
        unique_together = (('player', 'team', 'time_join'),)
        verbose_name = '球员球队关系'
        verbose_name_plural = verbose_name


class Teamtoleague(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='球队全称')
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='联赛名称')
    season_start = models.DateField(blank=True, null=True, verbose_name='赛季开始时间')
    season_end = models.DateField(blank=True, null=True, verbose_name='赛季结束时间')

    class Meta:
        db_table = 'teamtoleague'
        unique_together = (('team', 'league', 'season_start'),)
        verbose_name = '球队联赛关系'
        verbose_name_plural = verbose_name
