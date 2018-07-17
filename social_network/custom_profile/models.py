from django.db import models

class CustomProfile(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    birthday_date = models.DateField('YYYY-MM-DD')

    def createDebugProfiles(self):
        print('Creating profiles for debug purpose!')
        CustomProfile(name = 'Ismael Filipe Mesquita Ribeiro', email = 'ismaelfilipe@gmail.com', birthday_date = '1987-03-20').save()
        CustomProfile(name = 'Luisa Fernanda Cabrera Dominguez', email = 'luisafernanda23@gmail.com', birthday_date = '1991-08-23').save()

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.birthday_date)

class FriendInvatation(models.Model):

    inviter = models.ForeignKey(CustomProfile, related_name = 'invitations', on_delete=models.CASCADE)
    inviter_friend = models.ForeignKey(CustomProfile, related_name = 'received_invitations', on_delete=models.CASCADE)

