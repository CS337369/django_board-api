from django.forms.widgets import Widget
from .models import Board, Comment
from django import forms


class BoardForm(forms.ModelForm):        
    b_title = forms.CharField(max_length=30, label="제목",
                              error_messages={
                                  'required': "제목을 입력하세요."
                              })
    b_writer = forms.CharField(max_length=10, label="작성자",
                              error_messages={
                                  'required': "작성자를 입력하세요."
                              })
    b_note = forms.CharField(max_length=None, widget=forms.Textarea, label="내용",
                              error_messages={
                                  'required': "내용을 입력하세요."
                              })
    
    
    
    def clean(self):
        clean_data = super().clean()
        b_title = clean_data.get('b_title')
        b_writer = clean_data.get('b_writer')
        b_note = clean_data.get('b_note')
        
    class Meta:
        model = Board
        fields = ['b_title', 'b_writer', 'b_note']
        

class CommentForm(forms.ModelForm):        
    c_note = forms.CharField(max_length=None,
                              error_messages={
                                  'required': "내용을 입력하세요."
                              })
    
    def clean(self):
        clean_data = super().clean()
        c_note = clean_data.get('c_note')
        
    class Meta:
        model = Comment
        fields = ['c_note']