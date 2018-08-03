# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InteriorExterior'
        db.create_table(u'catalogue_interiorexterior', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'catalogue', ['InteriorExterior'])

        # Adding model 'FireRating'
        db.create_table(u'catalogue_firerating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'catalogue', ['FireRating'])

        # Adding model 'PositionApplication'
        db.create_table(u'catalogue_positionapplication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'catalogue', ['PositionApplication'])

        # Adding model 'CoverType'
        db.create_table(u'catalogue_covertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'catalogue', ['CoverType'])

        # Adding field 'ProductGapWidth.position_application'
        db.add_column(u'catalogue_productgapwidth', 'position_application',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='position_applications', null=True, to=orm['catalogue.PositionApplication']),
                      keep_default=False)

        # Adding field 'ProductGapWidth.interior_exterior'
        db.add_column(u'catalogue_productgapwidth', 'interior_exterior',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='interior_exteriors', null=True, to=orm['catalogue.InteriorExterior']),
                      keep_default=False)

        # Adding field 'ProductGapWidth.cover_type'
        db.add_column(u'catalogue_productgapwidth', 'cover_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cover_types', null=True, to=orm['catalogue.CoverType']),
                      keep_default=False)

        # Adding field 'ProductGapWidth.fire_rating'
        db.add_column(u'catalogue_productgapwidth', 'fire_rating',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fire_ratings', null=True, to=orm['catalogue.FireRating']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'InteriorExterior'
        db.delete_table(u'catalogue_interiorexterior')

        # Deleting model 'FireRating'
        db.delete_table(u'catalogue_firerating')

        # Deleting model 'PositionApplication'
        db.delete_table(u'catalogue_positionapplication')

        # Deleting model 'CoverType'
        db.delete_table(u'catalogue_covertype')

        # Deleting field 'ProductGapWidth.position_application'
        db.delete_column(u'catalogue_productgapwidth', 'position_application_id')

        # Deleting field 'ProductGapWidth.interior_exterior'
        db.delete_column(u'catalogue_productgapwidth', 'interior_exterior_id')

        # Deleting field 'ProductGapWidth.cover_type'
        db.delete_column(u'catalogue_productgapwidth', 'cover_type_id')

        # Deleting field 'ProductGapWidth.fire_rating'
        db.delete_column(u'catalogue_productgapwidth', 'fire_rating_id')


    models = {
        u'catalogue.category': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Category'},
            'colour_ranges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['colours.Range']", 'symmetrical': 'False', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.categoryimage': {
            'Meta': {'ordering': "('id',)", 'object_name': 'CategoryImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_images'", 'to': u"orm['catalogue.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.covertype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CoverType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.file': {
            'Meta': {'ordering': "('order',)", 'object_name': 'File'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['catalogue.Product']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.filegapwidth': {
            'Meta': {'ordering': "('order',)", 'object_name': 'FileGapWidth'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'product_gap_width': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gap_width_files'", 'to': u"orm['catalogue.ProductGapWidth']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.firerating': {
            'Meta': {'ordering': "('name',)", 'object_name': 'FireRating'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.group': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': u"orm['catalogue.SubCategory']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.image': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['catalogue.Product']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.imagegapwidth': {
            'Meta': {'ordering': "('id',)", 'object_name': 'ImageGapWidth'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'product_gap_width': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gap_width_images'", 'to': u"orm['catalogue.ProductGapWidth']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.interiorexterior': {
            'Meta': {'ordering': "('name',)", 'object_name': 'InteriorExterior'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.positionapplication': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PositionApplication'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.product': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Product'},
            'colour_ranges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['colours.Range']", 'symmetrical': 'False', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gapwidth': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'gapwidth_products'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['catalogue.ProductGapWidth']"}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalogue.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Entry']", 'symmetrical': 'False', 'blank': 'True'}),
            'related_products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalogue.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['catalogue.SubCategory']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.productgapwidth': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ProductGapWidth'},
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cover_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cover_types'", 'null': 'True', 'to': u"orm['catalogue.CoverType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fire_rating': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fire_ratings'", 'null': 'True', 'to': u"orm['catalogue.FireRating']"}),
            'gap_width': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interior_exterior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interior_exteriors'", 'null': 'True', 'to': u"orm['catalogue.InteriorExterior']"}),
            'movement': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'position_application': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'position_applications'", 'null': 'True', 'to': u"orm['catalogue.PositionApplication']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogue.subcategory': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sub_categories'", 'to': u"orm['catalogue.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'colours.range': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Range'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.entry': {
            'Meta': {'ordering': "['-published']", 'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['projects.Category']"}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'product_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'case_studies'", 'symmetrical': 'False', 'to': u"orm['catalogue.Category']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'related_projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Entry']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['catalogue']