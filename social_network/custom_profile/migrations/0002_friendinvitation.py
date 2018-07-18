# Generated by Django 2.0.7 on 2018-07-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='custom_profile.CustomProfile')),
                ('inviter_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invitations', to='custom_profile.CustomProfile')),
            ],
        ),
    ]