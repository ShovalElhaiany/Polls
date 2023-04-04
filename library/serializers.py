from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Book
        fields = '__all__'

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

    # def create(self, validated_data):
    #     return models.Author.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)

    #     instance.save()
    #     return instance
