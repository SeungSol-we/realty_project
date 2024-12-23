# Generated by Django 5.1.4 on 2024-12-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('우선순위', models.CharField(blank=True, choices=[('one', '1순위'), ('two', '2순위'), ('three', '3순위')], default='one', help_text='구매 우선순위를 결정해 주세요.', max_length=7)),
                ('이름', models.CharField(help_text='물건의 이름을 입력해 주세요.', max_length=200)),
                ('가격', models.IntegerField(help_text='물건의 가격을 입력해 주세요.')),
                ('이미지', models.ImageField(blank=True, null=True, upload_to='wish_images/')),
                ('정보', models.TextField(help_text='물건의 정보를 입력해주세요.', max_length=1000)),
                ('구매여부', models.CharField(blank=True, choices=[('false', '구매 X'), ('true', '구매 O')], default='false', help_text='구매 여부를 선택해 주세요.', max_length=100)),
                ('만족도', models.IntegerField(blank=True, choices=[(1, '불만족'), (2, '보통'), (3, '만족')], help_text='(구매 후) 만족도를 선택하세요.', null=True)),
            ],
        ),
    ]
