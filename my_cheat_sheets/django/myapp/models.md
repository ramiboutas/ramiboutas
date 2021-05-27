
[Return to Django main cheat sheet](../README.md)


## Default Model

```python

class MyModel(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  # more fields...

  def __str__(self):
    return self.title

```

### Using choices in models & display values and keys



```python

MY_OPTIONS_IN_MY_MODEL=(
  ('key1', 'Value 1'),
  ('key2', 'Value 2'),
)

class MyModel(models.Model):
  title = models.CharField(max_length=100)
  type = models.CharField(max_length=20, choices=MY_OPTIONS_IN_MY_MODEL)

```
In the template, we can access either to the key values (key1, key2, ...) or to the values themself (Value 1, Value 2, ...):
```html
<p> Access to the key: {{ object.type }}</p>
<p> Access to the value: {{ object.get_type_display }}</p>

```

## Abstract Model

to describe!

## Extend Model?

to describe!

## Proxy Model

to describe!
