# HTMX combined with django



## Send a trigger from the server and capture it from the client later
* django view
```python
# myapp/htmx_views.py or myapp/views.py
@require_http_methods(["PUT", "POST"])
def add_to_basket(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.add(product=product)
    response = render(request, 'basket/_added2basketalready.html') # we respond with whatever http response
    trigger_client_event(response, "basketUpdatedEvent", { },) # this is the trigger event
    return response
```

* html (you can update as many elements as you want)
```html
<div class="row" id="basket-price" hx-get="{% url 'basket:update-price' %}"
    hx-trigger="load delay:0.5s, basketUpdatedEvent from:body" >
  {% include "basket/update_this_part_when_that_event_occurs.html" %}
</div>


<div class="row" id="basket-quantity" hx-get="{% url 'basket:update-quantity' %}"
    hx-trigger="load delay:0.5s, basketUpdatedEvent from:body" >
  {% include "basket/update_this_part_when_that_event_occurs.html" %}
</div>
```
