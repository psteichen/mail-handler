from django.db.models import Model, CharField, ManyToManyField, EmailField, Sum, Count


class Member(Model):
  first_name 	=  CharField(max_length=250)
  last_name 	=  CharField(max_length=250)
  email 	=  EmailField()

  def __str__(self):
    return self.email

class List(Model):
  desc		= CharField(max_length=550)
  email		= EmailField()
  members	= ManyToManyField(Member)

  def nb_members(self):
    return self.members.count()

  def __str__(self):
    return self.email
