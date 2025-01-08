
# API de Tarefas (Django)

Esta é uma API simples de gerenciamento de tarefas construída com Django Rest Framework (DRF). A API permite que os usuários se autentiquem, criem suas tarefas e visualizem, atualizem ou excluam suas próprias tarefas.

## Funcionalidades

- **Autenticação de Usuário**: Permite que os usuários façam login e autentiquem suas solicitações.
- **Gerenciamento de Tarefas**: Usuários autenticados podem criar, listar, atualizar e excluir suas próprias tarefas.

## Endpoints da API

### 1. **Registro de Usuário**
   - **URL**: `/api/register/`
   - **Método**: `POST`
   - **Descrição**: Registra um novo usuário.
   - **Parâmetros**:
     - `username` (string): Nome de usuário.
     - `password` (string): Senha do usuário.
     - `email` (string): E-mail do usuário.
   - **Resposta**:
     - `201 Created` quando o usuário for registrado com sucesso.

### 2. **Login de Usuário**
   - **URL**: `/api/login/`
   - **Método**: `POST`
   - **Descrição**: Faz login do usuário e retorna um token JWT para autenticação.
   - **Parâmetros**:
     - `username` (string): Nome de usuário.
     - `password` (string): Senha do usuário.
   - **Resposta**:
     - `200 OK` com o token JWT.
     - `401 Unauthorized` se o login falhar.

### 3. **Listar Tarefas**
   - **URL**: `/api/tasks/`
   - **Método**: `GET`
   - **Descrição**: Lista todas as tarefas do usuário autenticado.
   - **Autenticação**: O usuário deve enviar o token JWT nos cabeçalhos de autorização.
   - **Resposta**:
     - `200 OK`: Lista de tarefas do usuário.

### 4. **Criar Tarefa**
   - **URL**: `/api/tasks/`
   - **Método**: `POST`
   - **Descrição**: Cria uma nova tarefa associada ao usuário autenticado.
   - **Autenticação**: O usuário deve enviar o token JWT nos cabeçalhos de autorização.
   - **Parâmetros**:
     - `title` (string): Título da tarefa.
     - `description` (string): Descrição da tarefa.
   - **Resposta**:
     - `201 Created` com os dados da tarefa criada.

### 5. **Detalhes da Tarefa**
   - **URL**: `/api/tasks/{id}`
   - **Método**: `GET`
   - **Descrição**: Exibe os detalhes de uma tarefa específica.
   - **Autenticação**: O usuário deve enviar o token JWT nos cabeçalhos de autorização.
   - **Resposta**:
     - `200 OK`: Detalhes da tarefa.

### 6. **Atualizar Tarefa**
   - **URL**: `/api/tasks/{id}`
   - **Método**: `PUT` ou `PATCH`
   - **Descrição**: Atualiza os dados de uma tarefa específica.
   - **Autenticação**: O usuário deve enviar o token JWT nos cabeçalhos de autorização.
   - **Parâmetros**:
     - `title` (string): Novo título da tarefa (opcional).
     - `description` (string): Nova descrição da tarefa (opcional).
     - `completed` (boolean): Marca a tarefa como concluída (opcional).
   - **Resposta**:
     - `200 OK`: Tarefa atualizada com sucesso.
     - `400 Bad Request` caso o formato ou parâmetros estejam errados.

### 7. **Excluir Tarefa**
   - **URL**: `/api/tasks/{id}`
   - **Método**: `DELETE`
   - **Descrição**: Exclui uma tarefa específica.
   - **Autenticação**: O usuário deve enviar o token JWT nos cabeçalhos de autorização.
   - **Resposta**:
     - `204 No Content`: Tarefa excluída com sucesso.

## Como Usar a API

### 1. **Instalar as dependências**

Clone o repositório e instale as dependências necessárias.

```bash
git clone https://github.com/Gabriel-Gald1n0/API_DJANGO_TASK.git
cd API_DJANGO_TASK
pip install -r requirements.txt
```

### 2. **Configurar o banco de dados**

Migrate o banco de dados:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 3. **Criar Superusuário (opcional)**

Se você quiser criar um superusuário para acessar o Django Admin, use o seguinte comando:

```bash
python manage.py createsuperuser
```

### 4. **Rodar o servidor**

Para rodar o servidor localmente, execute:

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

### 5. **Autenticação**

Para autenticar o usuário, faça uma requisição `POST` para `/api/login/` com o nome de usuário e senha. O servidor retornará um token JWT.

### 6. **Realizar Requisições**

Agora, use o token JWT para fazer requisições autenticadas.

- **Exemplo de cabeçalho de autorização para requisições autenticadas**:

```bash
Authorization: Bearer <seu_token_jwt>
```

### Exemplos de Requisição com o Postman

#### Login (POST)

- **URL**: `http://127.0.0.1:8000/api/login/`
- **Body** (JSON):
  ```json
  {
    "username": "seu_username",
    "password": "sua_senha"
  }
  ```

#### Criar Tarefa (POST)

- **URL**: `http://127.0.0.1:8000/api/tasks/`
- **Body** (JSON):
  ```json
  {
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
  }
  ```

#### Listar Tarefas (GET)

- **URL**: `http://127.0.0.1:8000/api/tasks/`
- **Cabeçalho**:
  ```bash
  Authorization: Bearer <seu_token_jwt>
  ```


