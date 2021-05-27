
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

### Save POST request data from a form

```python
def myview(request):
  form = MyModelForm(request.POST or None, request.FILES or None)
  # request.FILES is for uploading media or files to the server
  if request.method == 'POST':
    if form.is_valid():
      instance = form.save()
      # After creating the object -> we redirect the user to a detail view of the created object (instance)
      # It is also possible to redirect the user to somewhere else
      return HttpResponseRedirect(instance.get_absolute_url())

  context = {'form': form}
  return render(request, 'myapp/mytemplate.html', context)

```

```html
<h1> to copy</h1>
```

## Class based views


### ListView, how can we list more than one model?

Let's suppose we want to display in the same template two models (Job and Category), we could use the following:

```python
class MyListView(ListView):
  template_name = 'myapp/mytemplate.html'
  model = Job
  context_object_name = 'jobs'

  def get_context_data(self, **kwargs):
    context = super(MyListView, self).get_context_data(**kwargs)
    context['categories'] = Category.objects.all() # other queries are possible and more
    # Now we have a dictionary of 'jobs' & 'categories' 
    return context


```
For example we could have in the template:

```html
<h1>Jobs</h1>
<ul>
  {% for job in jobs %}
  <li> {{ job.title }} </li>
  {% empty %}
  <li> No jobs found </li>
  {% endfor %}
</ul>


<h1>Categories</h1>
<ul>
  {% for category in categories %}
  <li> {{ category.title }} </li>
  {% empty %}
  <li> No categories found </li>
  {% endfor %}
</ul>

```


```python
# to copy
```
```html
<h1> to copy</h1>
```
