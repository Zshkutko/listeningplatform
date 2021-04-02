# Generated by Django 3.1.3 on 2021-03-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=20, null=True)),
                ('var', models.IntegerField(blank=True, null=True)),
                ('a1', models.CharField(blank=True, max_length=50, null=True)),
                ('a2', models.CharField(blank=True, max_length=50, null=True)),
                ('a3', models.CharField(blank=True, max_length=50, null=True)),
                ('a4', models.CharField(blank=True, max_length=50, null=True)),
                ('a5', models.CharField(blank=True, max_length=50, null=True)),
                ('a6', models.CharField(blank=True, max_length=50, null=True)),
                ('a7', models.CharField(blank=True, max_length=50, null=True)),
                ('a8', models.CharField(blank=True, max_length=50, null=True)),
                ('a9', models.CharField(blank=True, max_length=50, null=True)),
                ('a10', models.CharField(blank=True, max_length=50, null=True)),
                ('a11', models.CharField(blank=True, max_length=50, null=True)),
                ('a12', models.CharField(blank=True, max_length=50, null=True)),
                ('a13', models.CharField(blank=True, max_length=50, null=True)),
                ('a14', models.CharField(blank=True, max_length=50, null=True)),
                ('a15', models.CharField(blank=True, max_length=50, null=True)),
                ('a16', models.CharField(blank=True, max_length=50, null=True)),
                ('a17', models.CharField(blank=True, max_length=50, null=True)),
                ('a18', models.CharField(blank=True, max_length=50, null=True)),
                ('a19', models.CharField(blank=True, max_length=50, null=True)),
                ('a20', models.CharField(blank=True, max_length=50, null=True)),
                ('a21', models.CharField(blank=True, max_length=50, null=True)),
                ('a22', models.CharField(blank=True, max_length=50, null=True)),
                ('a23', models.CharField(blank=True, max_length=50, null=True)),
                ('a24', models.CharField(blank=True, max_length=50, null=True)),
                ('a25', models.CharField(blank=True, max_length=50, null=True)),
                ('a26', models.CharField(blank=True, max_length=50, null=True)),
                ('a27', models.CharField(blank=True, max_length=50, null=True)),
                ('a28', models.CharField(blank=True, max_length=50, null=True)),
                ('a29', models.CharField(blank=True, max_length=50, null=True)),
                ('a30', models.CharField(blank=True, max_length=50, null=True)),
                ('a31', models.CharField(blank=True, max_length=50, null=True)),
                ('a32', models.CharField(blank=True, max_length=50, null=True)),
                ('a33', models.CharField(blank=True, max_length=50, null=True)),
                ('a34', models.CharField(blank=True, max_length=50, null=True)),
                ('a35', models.CharField(blank=True, max_length=50, null=True)),
                ('a36', models.CharField(blank=True, max_length=50, null=True)),
                ('a37', models.CharField(blank=True, max_length=50, null=True)),
                ('a38', models.CharField(blank=True, max_length=50, null=True)),
                ('a39', models.CharField(blank=True, max_length=50, null=True)),
                ('a40', models.CharField(blank=True, max_length=50, null=True)),
                ('points', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('task1', models.IntegerField(blank=True, null=True)),
                ('task2', models.IntegerField(blank=True, null=True)),
                ('task3', models.IntegerField(blank=True, null=True)),
                ('task4', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RightAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var', models.IntegerField()),
                ('a1', models.CharField(max_length=50)),
                ('a2', models.CharField(max_length=50)),
                ('a3', models.CharField(max_length=50)),
                ('a4', models.CharField(max_length=50)),
                ('a5', models.CharField(max_length=50)),
                ('a6', models.CharField(max_length=50)),
                ('a7', models.CharField(max_length=50)),
                ('a8', models.CharField(max_length=50)),
                ('a9', models.CharField(max_length=50)),
                ('a10', models.CharField(max_length=50)),
                ('a11', models.CharField(max_length=50)),
                ('a12', models.CharField(max_length=50)),
                ('a13', models.CharField(max_length=50)),
                ('a14', models.CharField(max_length=50)),
                ('a15', models.CharField(max_length=50)),
                ('a16', models.CharField(max_length=50)),
                ('a17', models.CharField(max_length=50)),
                ('a18', models.CharField(max_length=50)),
                ('a19', models.CharField(max_length=50)),
                ('a20', models.CharField(max_length=50)),
                ('a21', models.CharField(max_length=50)),
                ('a22', models.CharField(max_length=50)),
                ('a23', models.CharField(max_length=50)),
                ('a24', models.CharField(max_length=50)),
                ('a25', models.CharField(max_length=50)),
                ('a26', models.CharField(max_length=50)),
                ('a27', models.CharField(max_length=50)),
                ('a28', models.CharField(max_length=50)),
                ('a29', models.CharField(max_length=50)),
                ('a30', models.CharField(max_length=50)),
                ('a31', models.CharField(max_length=50)),
                ('a32', models.CharField(max_length=50)),
                ('a33', models.CharField(max_length=50)),
                ('a34', models.CharField(max_length=50)),
                ('a35', models.CharField(max_length=50)),
                ('a36', models.CharField(max_length=50)),
                ('a37', models.CharField(max_length=50)),
                ('a38', models.CharField(max_length=50)),
                ('a39', models.CharField(max_length=50)),
                ('a40', models.CharField(max_length=50)),
            ],
        ),
    ]