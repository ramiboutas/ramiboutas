
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




## Working with media

### Save a thumbnail
You can save space on server & speed up your speed by saving a thumbnail of an image. Sometimes we don't want to save images with size of 3 MB or  5 MB or even more, so can save just a thumbnail of that image for better performance of our app:



```python
from PIL import Image # pip install pillow

class Profile(models.Model):
  # other fields
  image = models.ImageField(upload_to="path/to/be/saved")

  def save(self, *args, **kwargs):
      super(Profile, self).save(*args, **kwargs)
      img = Image.open(self.image)
      if img.height > 200 or img.width > 200:
          new_size = (200, 200)
          # image proportion is manteined / we dont need to do extra work
          img.thumbnail(new_size)
          img.save(self.image.path)
```
