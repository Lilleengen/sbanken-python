# sbanken

A Python package for communicating with the Sbanken API.

## Usage
```python
from sbanken import SbankenAPI

client = SbankenAPI("client_id", "secret")

print(client.get_accounts("user id"))
```