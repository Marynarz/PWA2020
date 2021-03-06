from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)                       # Board owner, only one,
    create_time = models.DateTimeField(auto_now_add=True)                           # create time, not null
    participants = models.ManyToManyField(User, related_name='+')                   # board pariticipants
    board_name = models.CharField(max_length=20)                                    # board name, max 20 signs
    description = models.TextField()

    def __str__(self):
        return 'Board: %s, create time: %s, owner: %s' % (self.board_name, self.create_time, self.owner)


# Class Tab - class represents one tab in board
class Tab(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)   # Tab owner
    tab_name = models.CharField(max_length=20)                   # Tab name, max 20 signs
    position = models.IntegerField()                             # Position on board
    no_of_elems = models.IntegerField(default=0)                 # Number of elements in tab

    def __str__(self):
        return 'Tab: %s, Elems: %s, Board: %s' % (self.tab_name, self.no_of_elems, self.board)


# Class Element - basic element of Tab
class Element(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)                               # Element owner
    create_time = models.DateTimeField(auto_now_add=True)                                                 # Create time
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)                       # Creator
    elem_name = models.CharField(max_length=20)                                          # Name of element
    description = models.TextField()                                                     # Task description
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='+', default=None, null=True)

    def __str__(self):
        return 'Element: %s\n\tDescription: %s' % (self.elem_name, self.description)

