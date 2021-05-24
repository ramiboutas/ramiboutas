
[Return to Django main cheat sheet](../README.md)


## Function based views


### Query search (like Google)

In our `views.py` we define the following:
```python
from myapp.models import MyModel

def my_view(request):
  instances = MyModel.objects.all() # This does not have to be like that, another kind of query can be applied
  query = request.GET.get('q') # 'q' -> name in search input (see html form)
  if query:
    instances = instances.filter(Q(title__icontains=query) | Q(description__icontains=query))
  ## continue with other stuff, creating the context, rendering templates, so on.
```

In our HTML, we need a form with a GET method:

```html
<form  method="get">
  <input type="search" name="q">
  <button type="submit">Search</button>
</form>

```
Keep the query in your pagination:

```html
<a>href="?page=X{%if request.GET.q%}&q={{ request.GET.q }}{%endif%}">Page X</a>

```




## Class based views
