from django.db import models
from accounts.models import User,BookManagerUser
 


class Category(models.Model):
    name=models.CharField(max_length=255,blank=False,null=False,unique=True)
    create_By=models.ForeignKey(BookManagerUser, on_delete=models.CASCADE,related_name='manager_infos',blank=True)


    def __str__(self):
        return self.name

class Books(models.Model):
    cover=models.ImageField(upload_to='images')
    addBy=models.ForeignKey(BookManagerUser, blank=True,on_delete=models.CASCADE,related_name='books_of_a_user')
    bookAuthor=models.CharField(max_length=255,blank=False,null=False)
    title=models.CharField(max_length=1000,blank=False,null=False)
    numPages=models.IntegerField(blank=False,null=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='All_Books_Of_A_Category')



    def __str__(self):
        return str(self.id)
    

class CommandBooks(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Commends_Of_A_User',blank=True)
    bookId=models.OneToOneField(Books,on_delete=models.CASCADE,related_name='commands')
    dateCommanded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    
class ValidateCommands(models.Model):
    commandId=models.OneToOneField(CommandBooks,on_delete=models.CASCADE,related_name="validated")
    validator=models.ForeignKey(BookManagerUser, on_delete=models.CASCADE,related_name='All_Validated_Commands_Of_A_BookManagerUser',blank=True)
    dateValidated=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)



class History(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="Older_commands")
    book=models.ForeignKey(Books, on_delete=models.CASCADE,related_name="History_Commands_Of_this_Book")
    validated_by=models.ForeignKey(BookManagerUser, on_delete=models.CASCADE, related_name="command_validated")

    def __str__(self):
        return str(self.id)




    




    
    