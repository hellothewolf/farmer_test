# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

from django.core.urlresolvers import reverse

from django.utils.encoding import python_2_unicode_compatible
 
@python_2_unicode_compatible
class Plant(models.Model):
	name = models.CharField('植物名称',max_length=256)
	slug = models.CharField('植物名称拼音',max_length=256,db_index=True)
	path_picture = models.FilePathField('植物图片路径',path='static/plantpicture/',max_length=256)
	
	def get_absolute_url(self):
		return reverse('plant',args=(self.slug,))
	
	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = '植物'
		verbose_name_plural = '植物'
		ordering = ['name']
		
		
@python_2_unicode_compatible		
class Article(models.Model):
	title = models.CharField('标题',max_length=256)
	belongtoplant = models.ForeignKey('Plant',verbose_name='所属植物')
	slug = models.CharField('所属植物名称拼音',max_length=256)
	author = models.CharField('作者',blank=True,null=True,max_length=256)
	#intro = models.TextField('简介',default='',blank=True)
#	intro_picture_path = models.FilePathField('文章简介图片路径',path='uploads/images/',max_length=256)
	#content = models.TextField('内容',default='',blank=True)
	intro = UEditorField('intro',height=200,width=1000,default=u'',blank=True,imagePath="uploads/images/",toolbars='besttome',filePath='uploads/files/')
	content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')


	










	pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
	update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
	
	def get_absolute_url(self):
		return reverse('article',args=(self.pk,self.slug,))
	
	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'
	
	
	
		
		
		
		
	
