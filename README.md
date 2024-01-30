# django
 Aprendizado Django com python

## Projeto 1: Cadastro de usuarios simples
![image](https://github.com/Fabio-jr-SM/django/assets/91484736/be40658c-02d4-4e7d-a894-46d370ab3eec)


### 1. Instalação:
Certifique-se de ter o Python instalado em seu sistema. Em seguida, você pode instalar o Django usando o seguinte comando:

```md
pip install django
```

### 1. Criar um Projeto:
Depois de instalar o Django, crie um novo projeto usando o seguinte comando:

```md
django-admin startproject nome_do_projeto
```
Substitua "nome_do_projeto" pelo nome que você deseja dar ao seu projeto.

Navegar para o Diretório do Projeto:
Vá para o diretório recém-criado usando o comando cd nome_do_projeto.

### 2. Criar um Aplicativo:
Um projeto Django consiste em um ou mais aplicativos. Crie um aplicativo usando o seguinte comando:

```md
python manage.py startapp nome_do_aplicativo
```

Substitua "nome_do_aplicativo" pelo nome que você deseja dar ao seu aplicativo.

### 3. Definir Modelos:
Em seu aplicativo, defina os modelos que representam os dados que você deseja armazenar no banco de dados. Isso é feito no arquivo models.py.

### 4. Criar Migrações:
Após definir os modelos, crie migrações usando o seguinte comando:

```md
python manage.py makemigrations
```

### 5. Aplicar Migrações:
Aplique as migrações ao banco de dados com o comando:

```md
python manage.py migrate
```