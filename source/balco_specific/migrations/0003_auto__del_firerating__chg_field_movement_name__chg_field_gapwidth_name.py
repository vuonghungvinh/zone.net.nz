# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FireRating'
        db.delete_table(u'balco_specific_firerating')


        # Changing field 'Movement.name'
        db.alter_column(u'balco_specific_movement', 'name', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'GapWidth.name'
        db.alter_column(u'balco_specific_gapwidth', 'name', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):
        # Adding model 'FireRating'
        db.create_table(u'balco_specific_firerating', (
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'balco_specific', ['FireRating'])


        # Changing field 'Movement.name'
        db.alter_column(u'balco_specific_movement', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'GapWidth.name'
        db.alter_column(u'balco_specific_gapwidth', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'balco_specific.covertype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CoverType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'balco_specific.explainationcopy': {
            'Meta': {'ordering': "('field',)", 'object_name': 'ExplainationCopy'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'balco_specific.gapwidth': {
            'Meta': {'ordering': "('name',)", 'object_name': 'GapWidth'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'balco_specific.interiorexterior': {
            'Meta': {'ordering': "('name',)", 'object_name': 'InteriorExterior'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'balco_specific.movement': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Movement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'balco_specific.positionapplication': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PositionApplication'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['balco_specific']