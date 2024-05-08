from rest_framework.serializers import ModelSerializer
from .models import Books,CommandBooks,ValidateCommands,Category,History

class BooksSerializer(ModelSerializer):
    class Meta:
        model=Books
        fields=['id','bookAuthor','addBy','cover','title','numPages','category']
        # depth=1



class BooksSerializerPost(ModelSerializer):
    class Meta:
        model=Books
        fields=['id','bookAuthor','cover','title','numPages','category']
        # depth=1
        


class CommandBookSerializer(ModelSerializer):
    class Meta:
        model=CommandBooks
        fields=['id','user','bookId','dateCommanded']
        # depth=1





class ValidateCommandSerializer(ModelSerializer):
    class Meta:
        model=ValidateCommands
        fields=['id','commandId','validator','dateValidated']
        # depth=1


class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','create_By']
        # depth=1




# list serializer




class BooksSerializerList(ModelSerializer):
    class Meta:
        model=Books
        fields=['id','bookAuthor','addBy','cover','title','numPages','category']
        depth=1



# class BooksSerializerList(ModelSerializer):
#     class Meta:
#         model=Books
#         fields=['id','bookAuthor','cover','title','numPages','category']
#         depth=1
        


class CommandBookSerializerList(ModelSerializer):
    class Meta:
        model=CommandBooks
        fields=['id','user','bookId','dateCommanded']
        depth=1





class ValidateCommandSerializerList(ModelSerializer):
    class Meta:
        model=ValidateCommands
        fields=['id','commandId','validator','dateValidated']
        depth=1


class CategorySerializerList(ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','create_By']
        depth=1



# New Operation!!!!!!!!!!!!!!!!!!!!!!!!

class HistorySerializer(ModelSerializer):
    class Meta:
        model=History
        fields=['id','user','book','validated_by']


class HistorySerializerList(ModelSerializer):
    class Meta:
        model=History
        fields=['id','user','book','validated_by']
        depth=1




