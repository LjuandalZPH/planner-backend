# Planner Backend (Django)

Backend mínimo en Django con estructura por apps y endpoints de verificación.

## Requisitos

- Python 3.11+ recomendado

## Instalación (Windows PowerShell)

Desde la carpeta `planner-backend`:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements\base.txt
```

## Correr el proyecto

```powershell
python manage.py migrate
python manage.py runserver
```

Al abrir `http://127.0.0.1:8000/` debes ver:

`Planner backend funcionando correctamente.`

Endpoints rápidos:

- `/api/users/`
- `/api/missions/`
- `/api/gamification/`

## Tests

```powershell
python manage.py test
```

