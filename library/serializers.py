from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


"""Another way to create functions that aim to create and update,
This way is done in the serializers file, the second way is done through the Api Views file"""
# def create(self, validated_data):
#     return models.Book.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.book_name = validated_data.get('book_name', instance.book_name)
#     instance.author_name = validated_data.get('author_name', instance.author_name)
#     instance.pub_date = validated_data.get('pub_date', instance.pub_date)

#     instance.save()
#     return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


"""Same as the class above"""
# def create(self, validated_data):
#     return models.Author.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.last_name = validated_data.get('last_name', instance.last_name)
#     instance.email = validated_data.get('email', instance.email)

#     instance.save()
#     return instance
