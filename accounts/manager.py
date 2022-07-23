from django.contrib.auth.base_user import BaseUserManager
import uuid 

class UserModel(BaseUserManager):
    user_in_migrations=True 

    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError("Email Field is required")
        
        email=self.normalize_email(email) 
        user=self.model(email=email,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault("is_superuser",True)
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_active",True)
        kwargs.setdefault("verify",True)
        kwargs.setdefault("token",str(uuid.uuid4())[:100].replace("-","")+str(uuid.uuid4())[:140].replace("-",""))

        if kwargs.get("is_staff") is not True:
            raise ValueError(('Super user must have Staff user'))

        return self.create_user(email,password,**kwargs)
