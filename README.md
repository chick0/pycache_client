# PyCache Client

client for [PyCache](https://github.com/chick0/pycache/)

### hello_world.py
```python
from pycache_client import Client

client = Client(
    host="127.0.0.1",
    port=5521
)

client.set("say", b"Hello, World!")
print(client.get("say"))
```
