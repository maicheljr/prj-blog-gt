# Generated by Django 2.2 on 2020-09-16 22:01

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_master', '0002_auto_20200829_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('criado', models.DateTimeField(auto_now=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publicado']},
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('object_list', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=250, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(related_name='get_posts', to='blog_master.Category'),
        ),
    ]
