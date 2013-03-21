# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Subscription'
        db.create_table('djpubsubhubbub_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hub', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('topic', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('verify_token', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('lease_expires', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_subscribed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('djpubsubhubbub', ['Subscription'])


    def backwards(self, orm):
        
        # Deleting model 'Subscription'
        db.delete_table('djpubsubhubbub_subscription')


    models = {
        'djpubsubhubbub.subscription': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Subscription'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'hub': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lease_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'topic': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verify_token': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['djpubsubhubbub']
