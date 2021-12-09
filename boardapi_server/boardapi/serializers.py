from .models import Board, Comment, Account
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField

############ Comment ################


class CommentSerializer(serializers.ModelSerializer):
    c_date = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ['Board_id', 'id', 'c_writer', 'c_note', 'c_date', 'updated_at']
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['Board', 'c_writer', 'c_note', 'c_date', 'id']


############## Board #################


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['b_no', 'b_title', 'b_note', 'b_writer', 'parent_no', 'b_date', 'b_count', 'updated_at', 'comments']


class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['b_title', 'b_writer', 'b_note']


class BoardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['b_title',  'b_writer', 'b_note']


class BoardDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = ['b_no', 'b_title', 'b_note', 'b_writer', 'b_date', 'comments']