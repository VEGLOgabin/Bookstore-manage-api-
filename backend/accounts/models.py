from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, password,email , **kwargs):
        """
        Creates and saves a User with the given phone and password.
        """
        email=self.normalize_email(email)
        if not email:
            raise ValueError('Users must have email')
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email=email
        )

        user.is_active = True
        user.admin = False
        user.staff = False

        user.set_password(password)
        user.save()

        return user
    

    def create_staffuser(self, first_name, last_name,password,email):

        email=self.normalize_email(email)
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email=email,
        )

        user.staff = True
        user.is_active = True
        user.set_password(password)

        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email,password):
        email=self.normalize_email(email)
        user = self.create_user(
            
            first_name = first_name,
            last_name = last_name,
            email=email,
            
            
        )

        user.admin = True
        user.staff = True
        user.is_active = True
        user.set_password(password)
        
        user.save()
        return user




class User(AbstractBaseUser,PermissionsMixin):

    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    ISADMIN=models.BooleanField(default=True)
    is_manager=models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
       return self.first_name



class Profil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='ProfilPhoto')
    image=models.ImageField(upload_to='images/', default='images/default.jpg')


    def __str__(self):
        return self.id





class AdminUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='Admin',blank=True)
    level=models.CharField(max_length=255,blank=False,null=False)
    profession=models.CharField(max_length=255,blank=True)
    # is_superadmin = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)



class BookManagerUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='BookManager',blank=True)
    degree=models.CharField(max_length=255,blank=False,null=False)
    AdminCreator=models.ForeignKey(AdminUser, on_delete=models.CASCADE,related_name='bookmanager_created',blank=True)
    experienceYears=models.IntegerField(blank=True)


    def __str__(self):
        return str(self.id)