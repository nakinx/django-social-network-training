from django.db import models

class CustomProfile(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    birthday_date = models.DateField('YYYY-MM-DD')
    friends = models.ManyToManyField('self')

    def inviteFriend(self, invited_friend):        
        FriendInvitation(inviter = self, invited_friend = invited_friend).save()

    @staticmethod
    def createDebugProfiles():
        print('Creating profiles for debug purpose!')
        CustomProfile(name = 'Ismael Filipe Mesquita Ribeiro', email = 'ismaelfilipe@gmail.com', birthday_date = '1987-03-20').save()
        CustomProfile(name = 'Luisa Fernanda Cabrera Dominguez', email = 'luisafernanda23@gmail.com', birthday_date = '1991-08-23').save()
        CustomProfile(name = 'Sara Mesquita Ribeiro', email = 'saramesquitar@gmail.com', birthday_date = '1988-06-10').save()
        CustomProfile(name = 'Rossana de Almeida Mesquita', email = 'rossanamesquita@gmail.com', birthday_date = '1964-07-02').save()
        CustomProfile(name = 'Jose Garcia Ribeiro Junior', email = 'josegarcia@gmail.com', birthday_date = '1961-10-13').save()

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.birthday_date)

class FriendInvitation(models.Model):
    inviter = models.ForeignKey(CustomProfile, related_name = 'invitations', on_delete=models.CASCADE)
    invited_friend = models.ForeignKey(CustomProfile, related_name = 'received_invitations', on_delete=models.CASCADE)

    def acceptFriend(self):
        self.invited_friend.friends.add(self.inviter)
        self.delete()
        
        # Check if invited made a invitation to the invitor.
        invited_invitation = FriendInvitation.objects.get(inviter = self.invited_friend, invited_friend = self.inviter)
        
        if invited_invitation:
            invited_invitation.delete()
        