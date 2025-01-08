from rest_framework import serializers
from tasks.models import Task
from users.models import User

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # Para exibir id e username do usuário

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'user']

    def get_user(self, obj):
        # Retorna um dicionário com o id e o username do usuário associado
        return {
            'id': obj.user.id,
            'username': obj.user.username
        }

    def create(self, validated_data):
        # Associa automaticamente o usuário autenticado à tarefa
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # Define o usuário autenticado
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Atualiza os campos normalmente
        for attr, value in validated_data.items():
            if attr != 'user':  # Não atualiza o campo 'user' se ele já foi tratado
                setattr(instance, attr, value)

        instance.save()  # Salva as alterações no banco de dados
        return instance

