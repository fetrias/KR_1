from pydantic import BaseModel, field_validator, ValidationError
import re

class User(BaseModel):
    name: str
    id: int

class UserWithAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if len(v) < 2:
            raise ValueError('Имя должно содержать минимум 2 символа')
        if len(v) > 50:
            raise ValueError('Имя должно содержать максимум 50 символов')
        return v
    
    @field_validator('message')
    @classmethod
    def validate_message(cls, v):
        if len(v) < 10:
            raise ValueError('Сообщение должно содержать минимум 10 символов')
        if len(v) > 500:
            raise ValueError('Сообщение должно содержать максимум 500 символов')
        
        forbidden_words = ['кринж', 'рофл', 'вайб']
        
        v_lower = v.lower()
        
        for word in forbidden_words:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        
        return v