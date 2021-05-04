
[Return to Django main cheat sheet](../README.md)

### Register model in admin site:

in *myapp/admin.py*:

```python
from django.contrib import admin
from app.models import MyModel

admin.site.register(MyModel)
```
