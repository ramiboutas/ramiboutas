
[Return to Django main cheat sheet](../README.md)


## Default Model

```python

from app.models import MyModel


class MyModel(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  # more fields...

  def __str__(self):
    return self.title

```

## Abstract Model

to describe!

## Extend Model?

to describe!

## Proxy Model

to describe!
