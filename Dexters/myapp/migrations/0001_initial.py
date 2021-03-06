# Generated by Django 2.0.1 on 2018-01-28 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('date', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('no_of_upvotes', models.BigIntegerField(null=True)),
                ('no_of_downvotes', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('no_of_upvotes', models.BigIntegerField(null=True)),
                ('no_of_downvotes', models.BigIntegerField(null=True)),
                ('no_of_views', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('no_of_upvotes', models.BigIntegerField(null=True)),
                ('no_of_downvotes', models.BigIntegerField(null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Answer')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('date', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('topic', models.CharField(max_length=50)),
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tags'),
        ),
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Question'),
        ),
    ]
